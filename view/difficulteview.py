"""gère l'affichage pour le choix des difficultés du jeu
"""
import re
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

ASK_NB_TENTATIVES=inquirer.text(
    message = 'Quel est le nombre maximum de tentatives que tu veux?')
ASK_TEMPS=inquirer.text(
    message = 'Quel est le temps maximum souhaité pour faire une proposition?')
ASK_NB_LETTRES=inquirer.text(
    message = 'Combien veux tu que ton mot comporte de lettres? (15 maximum)')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
#pylint: disable=no-value-for-parameter
# justification: la Session a bien un Joueur
# et listes est une liste de Liste(s)
class DifficulteView (AbstractView) :
    """gère l'affichage pour le choix des difficultés du jeu
    """
    def __init__(self):
        self.__questions1 = inquirer.select(
            message='Veux tu connaitre la première lettre du mot?'
            , choices=[
                Choice('Oui')
                ,Choice('Non')
            ])

        id_joueur = Session().joueur.id_joueur
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        #pylint: disable=unused-import
        #justification: get_listes() renvoie une liste de Liste(s)
        from business_objects.liste import Liste
        listes = clientjoueur.get_listes(id_joueur)

        choix = [Choice("Choisir un mot aléatoire")]
        if listes is not None :
            for liste in listes :
                choix.append(Choice(liste.nom))
        self.__questions2 = inquirer.select(
            message='Quelle liste veux tu sélectionner?'
            , choices = choix
        )

    def display_info(self):
        pass

    def make_choice(self):
        #pylint: disable=too-many-locals
        #justification: on a besoin de ces variables
        #pylint: disable=too-many-branches
        #justification: les difficultés ont des paramètres essentiels
        reponse2 = self.__questions2.execute()
        if reponse2 == 'Choisir un mot aléatoire' :
            est_liste_perso = False
            id_liste = None
            nb_lettres = ASK_NB_LETTRES.execute()
            exp_reg = r'1[0-5]|[0-9]'
            if re.fullmatch(exp_reg, nb_lettres) is None:
                print("Le nombre de lettres donné est incorrect."+
                      " La partie se jouera donc avec un mot de 6 lettres")
                nb_lettres = 6
            else :
                int(nb_lettres)
        else :
            est_liste_perso = True
            id_joueur = Session().joueur.id_joueur
            from client_joueur import ClientJoueur
            clientjoueur = ClientJoueur()
            listes = clientjoueur.get_listes(id_joueur)
            nb_lettres = 0
            for liste in listes :
                if liste.nom == reponse2 :
                    id_liste = liste.id_liste

        reponse1 = self.__questions1.execute()
        #pylint: disable=simplifiable-if-statement
        #justification: ça ne simplifie pas la lecture
        if reponse1 == 'Oui' :
            indice = True
        else :
            indice = False

        exp_reg_int = r'[1-9][0-9]*'
        nb_tentatives = ASK_NB_TENTATIVES.execute()
        # pour contrôler les chaînes de caractères malicieusement introduites
        if re.fullmatch(exp_reg_int, nb_tentatives) is None :
            print("Le nombre de tentatives donné est incorrect."+
                  " La partie se jouera en 6 tentatives")
            nb_tentatives = 6
        else :
            int(nb_tentatives)
        temps = ASK_TEMPS.execute()
        if re.fullmatch(exp_reg_int, temps) is None :
            print("Le temps donné est incorrect. Tu auras 10 secondes entre chaque proposition")
            temps = 10
        else :
            int (temps)

        from business_objects.difficultes import Difficultes
        difficultes = Difficultes(nb_tentatives, temps, indice, nb_lettres)

        from business_objects.partie import Partie

        partie = Partie(liste_mots_proposes=[],
                        difficultes=difficultes,
                        est_liste_perso = est_liste_perso,
                        id_liste = id_liste,
                        mot_objectif = None )
        partie.difficultes.nb_lettres = len(partie.mot_objectif)
        print(f"Le mot à trouver est de {partie.difficultes.nb_lettres} lettres")
        Session().partie = partie
        if indice :
            print(partie.mot_objectif[0])
        from view.pauseview import PauseView
        return PauseView()
