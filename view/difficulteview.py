from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

from business_objects.liste import Liste

ASK_NB_TENTATIVES=inquirer.text(message = 'Quel est le nombre maximum de tentatives que tu veux?')
ASK_TEMPS=inquirer.text(message = 'Quel est le temps maximum souhaité pour faire une proposition?')
ASK_NB_LETTRES=inquirer.text(message = 'Combien veux tu que ton mot comporte de lettres? (15 maximum)')


class DifficulteView (AbstractView) :
    def __init__(self):
        self.__questions1 = inquirer.select(
            message=f'Veux tu connaitre la première lettre du mot?'
            , choices=[
                Choice('Oui')
                ,Choice('Non')
            ])
        
        id_joueur = Session().joueur.id_joueur
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        listes = clientjoueur.get_listes(id_joueur)

        from business_objects.liste import Liste
        choix = [Choice("Choisir un mot aléatoire")]
        for liste in listes :
            choix.append(Choice(liste.nom))
        self.__questions2 = inquirer.select(
            message=f'Quelle liste veux tu sélectionner?'
            , choices = choix
        )
    
    def display_info(self):
        pass

    def make_choice(self):

        reponse2 = self.__questions2.execute()
        if reponse2 == 'Choisir un mot aléatoire' :
            est_liste_perso = False
            id_liste = None
            reponse1 = self.__questions1.execute()
            if reponse1 == 'Oui' :
                indice = True
            else :
                indice = False
            
            nb_lettres = int(ASK_NB_LETTRES.execute())
            if type(nb_lettres) != int and (nb_lettres < 1 or nb_lettres > 15):
                print("Le nombre de lettres donné est incorrect. La partie se jouera avec un mot de 6 lettres")
                nb_lettres = 6
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
        nb_tentatives = ASK_NB_TENTATIVES.execute()
        if type(int(nb_tentatives)) != int :
            print("Le nombre de tentatives donné est incorrect. La partie se jouera en 6 tentatives")
            nb_tentatives = 6
        temps = ASK_TEMPS.execute()
        if type(int(temps)) != int :
            print("Le temps donné est incorrect. Tu auras 8 secondes entre chaque proposition")
            temps = 8
        
        from business_objects.difficultes import Difficultes
        difficultes = Difficultes(nb_tentatives, temps, indice, nb_lettres)

        from business_objects.partie import Partie
        partie = Partie(nom = "partie", liste_mots_proposes=[], difficultes=difficultes, est_liste_perso = est_liste_perso, id_liste = id_liste, mot_objectif = None )
        Session().partie = partie
        if indice :
            print(partie.mot_objectif[0])
        from view.pauseview import PauseView
        return PauseView()

            
        