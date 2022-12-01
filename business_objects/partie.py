"""gère la classe Partie
"""

from business_objects.proposition import Proposition
from business_objects.code_lettre import CodeLettre
from business_objects.proposition_verifiee import PropositionVerifiee
#pylint: disable=unused-import
#justification: on s'en sert, cf axe à améliorer.
from business_objects.difficultes import Difficultes
from business_objects.generer_mot_api import GenererMotApi
from business_objects.generer_mot_liste_perso import GenererMotListePerso

class Partie :
    '''Classe implémentant une partie

    attributes
    ----------
    liste_mots_proposes : list(Proposition)
    est_liste_perso : bool
    id_liste : int
    difficultes : Difficultes
    score : float
    mot_objectif : str

    Examples
    --------
    >>> from business_objects.proposition import Proposition
    >>> from business_objects.difficultes import Difficultes
    >>> partie1 = Partie(liste_mots_proposes="[]",
    ... est_liste_perso= True,
    ... difficultes= Difficultes(None, None ,False,8),
    ... mot_objectif="Mathieu",
    ... id_liste = 42)
    '''
    #pylint: disable=too-many-arguments
    #justification: on est obligé, sinon il faudrait un objet... Partie! :)
    def __init__(self, liste_mots_proposes, est_liste_perso, difficultes, mot_objectif, id_liste):
        self.liste_mots_proposes=liste_mots_proposes
        self.est_liste_perso=est_liste_perso
        self.difficultes=difficultes
        self.score=0
        self.id_liste=id_liste
        if mot_objectif is None:
            self.mot_objectif=self.donne_mot_obj()
        else:
            self.mot_objectif=mot_objectif


    def donne_mot_obj(self):
        '''donne le mot objectif de la partie, soit par l'api random-word-api,
        soit un mot dans la liste perso
        return
        ------
        le mot objectif  : str
        '''


        if self.est_liste_perso:
            generer=GenererMotListePerso(self.id_liste)
            mot = generer.generer()
        else :
            mot_existe = False

            while not mot_existe :
                generer=GenererMotApi(self.difficultes.nb_lettres)
                mot = generer.generer()

                mot_propose = Proposition(mot)
                mot_existe = mot_propose.est_autorise()

        return mot


    def occurence_lettres(self):
        '''retourne une liste avec pour chaque lettre apparaissant
        dans le mot objectif, le nombre d'occurences de cette lettre dans le mot objectif

        Examples
        --------
        >>> from business_objects.proposition import Proposition
        >>> from business_objects.difficultes import Difficultes
        >>> partie1 = Partie(liste_mots_proposes="[]",
        ... est_liste_perso= True,
        ... difficultes= Difficultes(None, None ,False,8),
        ... mot_objectif="MATHIEU",
        ... id_liste = 42)
        >>> partie1.occurence_lettres()
        [['M', 1], ['A', 1], ['T', 1], ['H', 1], ['I', 1], ['E', 1], ['U', 1]]
        '''
        lettres=[] #prépare la liste des lettres du mot objectif
        for lettre in self.mot_objectif:#itère à travers le mot objectif
            if lettre not in lettres: # si la lettre n'est pas déjà dans la liste
                lettres.append(lettre)# alors on la met dedans
        #soit N=le nombre de lettres différentes du mot objectif
        nombre_lettres_differentes = len(lettres)
        #création d'une liste de N listes
        liste_lettre_occurrences=[[]*i for i in range(nombre_lettres_differentes)]
        for i in range(nombre_lettres_differentes):#on itère sur chacune des sous-listes
            # dans chaque sous-liste, on place une des lettres (différentes) du mot objectif
            liste_lettre_occurrences[i].append(lettres[i])
            #dans cette même sous-liste, on place un zéro en deuxième position, c'est un compteur
            liste_lettre_occurrences[i].append(0)
            #on itère dans les lettres du mot objectif
            for lettre in self.mot_objectif:
                #si la lettre est égale à celle de la sous-liste
                if lettre==lettres[i]:
                    #alors on incrémente le compteur de 1
                    liste_lettre_occurrences[i][1]+=1
        return liste_lettre_occurrences


    def lettres_bien_placees(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot_propose et
        True si la lettre est bien placee et False sinon
        '''
        liste_lettres_bien_placees=[]
        longueur_mot_propose = len(mot_propose.mot)
        for i in range(longueur_mot_propose):
            if mot_propose.mot[i]==self.mot_objectif[i]:
                liste_lettres_bien_placees.append([mot_propose.mot[i], True])
            else:
                liste_lettres_bien_placees.append([mot_propose.mot[i], False])
        return liste_lettres_bien_placees


    def lettres_mal_placees(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot propose,
        True si la lettre est bien placée,
        'Mal placée' si mal placée et
        False si la lettre n'est pas dans le mot objectif
        '''
        bien_placees=self.lettres_bien_placees(mot_propose)
        occurence=self.occurence_lettres()
        for i in range(len(mot_propose.mot)):
            lettre=bien_placees[i][0]
            if bien_placees[i][1]:
                for elm in occurence:
                    if elm[0]==lettre:
                        elm[1]-=1
            if not bien_placees[i][1]:
                for elm in occurence:
                    if elm[0]==lettre:
                        if elm[1]!=0:
                            bien_placees[i][1]="Mal placee"
                            elm[1]-=1
        return bien_placees

    def verifie_proposition(self, mot_propose):
        '''Vérifie une proposition
        return
        ------
        La proposition vérifiée (PropositionVerifiee)
        '''
        verification=self.lettres_mal_placees(mot_propose)
        liste_lettres=[]
        for elt in verification:
            lettre=CodeLettre(elt[0],elt[1])
            liste_lettres.append(lettre)
        return PropositionVerifiee(liste_lettres)

    def calcul_score(self):
        '''calcul le score selon les paramètres de difficulté de la partie
        '''
        coeff_tentatives_max = 1 + 0.1 * (6 - int(self.difficultes.nb_tentatives))
        coeff_longueur = 1 + 0.1 *int((self.difficultes.nb_lettres - 6))
        coeff_limite_temps = int(self.difficultes.temps) - 8 / 8
        self.score=100 + coeff_tentatives_max * coeff_tentatives_max * \
            coeff_longueur * coeff_limite_temps

    def __str__(self):
        """affichage d'une Partie

        Returns
        -------
        str
            affiche une partie

        Examples
        --------
        >>> from business_objects.proposition import Proposition
        >>> from business_objects.difficultes import Difficultes
        >>> partie1 = Partie(liste_mots_proposes="[]",
        ... est_liste_perso= True,
        ... difficultes= Difficultes(6, 8 ,False,7),
        ... mot_objectif="Mathieu",
        ... id_liste = 42)
        >>> print(partie1)
        Mot objectif : Mathieu,
        mots proposés : [],
        score : 0,
        difficultés :6 tentatives, 8 secondes par tentatives, sans indice, mot de 7 lettres

        """
        return (f"Mot objectif : {self.mot_objectif},\n"
                f"mots proposés : {self.liste_mots_proposes},\n"
                f"score : {self.score},\n"
                f"difficultés :{self.difficultes}")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)

