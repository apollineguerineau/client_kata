from compileall import compile_dir

from business_objects.proposition import Proposition
from business_objects.code_lettre import CodeLettre
from business_objects.proposition_verifiee import PropositionVerifiee
from business_objects.difficultes import Difficultes
from business_objects.generer_mot_api import GenererMotApi
from business_objects.generer_mot_liste_perso import GenererMotListePerso

class Partie :
    '''Classe implémentant une partie

    attributes
    ----------
    mot_objectif : str
    liste_mots_proposes : list(str)
    est_liste_perso : bool
    id_liste : int
    difficultes : Difficultes
    score : float
    '''
    def __init__(self, liste_mots_proposes, est_liste_perso, difficultes, mot_objectif, id_liste):
        self.liste_mots_proposes=liste_mots_proposes
        self.est_liste_perso=est_liste_perso
        self.difficultes=difficultes
        self.score=0
        self.id_liste=id_liste
        if mot_objectif == None:
            self.mot_objectif=self.donne_mot_obj()
        else:
            self.mot_objectif=mot_objectif


    def donne_mot_obj(self):
        '''donne le mot objectif de la partie, soit par l'api random-word-api, soit un mot dans la liste perso
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
                from business_objects.proposition import Proposition
                mot_propose = Proposition(mot)
                mot_existe = mot_propose.est_autorise()
            
        return mot


    def occurence_lettres(self):
        '''retourne une liste avec pour chaque lettre apparaissant dans le mot objectif, l'occurence de cette lettre dans le mot objectif
        '''
        lettres=[]
        for lettre in self.mot_objectif:
            if lettre not in lettres:
                lettres.append(lettre)
        L=[[]*i for i in range(len(lettres))]
        for i in range(len(lettres)):
            L[i].append(lettres[i])
            L[i].append(0)
            for lettre in self.mot_objectif:
                if lettre==lettres[i]:
                    L[i][1]+=1
        return(L)


    def lettres_bien_placees(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot_propose et True si la lettre est bien placee et False sinon
        '''
        L=[]
        for i in range(len(mot_propose.mot)):
            if mot_propose.mot[i]==self.mot_objectif[i]:
                L.append([mot_propose.mot[i], True])
            else:
                L.append([mot_propose.mot[i], False])
        return L


    def lettres_mal_placees(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot propose, True si la lettre est bien placée, 'Mal placée' si mal placée et False si la lettre n'est pas dans le mot objectif
        '''
        bien_placees=self.lettres_bien_placees(mot_propose)
        occurence=self.occurence_lettres()
        for i in range(len(mot_propose.mot)):
            lettre=bien_placees[i][0]
            if bien_placees[i][1]==True:
                for elm in occurence:
                    if elm[0]==lettre:
                        elm[1]-=1
            if bien_placees[i][1]==False:
                for elm in occurence:
                    if elm[0]==lettre:
                        if elm[1]!=0:
                            bien_placees[i][1]="Mal placee"
                            elm[1]-=1
        return(bien_placees)

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
        return(PropositionVerifiee(liste_lettres))

    def calcul_score(self):
        '''calcul le score selon les paramètres de difficulté de la partie
        '''
        coeff_tentatives_max = 1 + 0.1 * (6 - int(self.difficultes.nb_tentatives))
        coeff_longueur = 1 + 0.1 *int((self.difficultes.nb_lettres - 6))
        coeff_limite_temps = int(self.difficultes.temps) - 8 / 8
        self.score=100 + coeff_tentatives_max * coeff_tentatives_max * coeff_longueur * coeff_limite_temps

    def __str__(self):
        return("Mot objectif : {}, mots proposés : {}, score : {}, difficultés :{}".format(self.mot_objectif, self.liste_mots_proposes,self.score, self.difficultes))

