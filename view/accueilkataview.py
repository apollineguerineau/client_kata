"""module pour l'accueil du jeu
"""

import sys
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from view.abstractview import AbstractView
from view.connectionview import ConnectionView
from view.creercompteview import CreerCompteView
from view.toptenview import ViewTopTen

class AccueilKataView (AbstractView) :
    """permet d'afficher le menu d'accueil

    Parameters
    ----------
    AbstractView : AbstractView mère
        classe mère

    """
    def __init__(self):
        self.__questions = inquirer.select(
            message='Bonjour'
            , choices=[
                Choice('Se connecter')
                ,Choice('Créer un compte')
                ,Choice("Consulter les 10 meilleurs scores")
                ,Choice('Quitter le jeu')]
        )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Se connecter' :
            return ConnectionView()
        if reponse == 'Créer un compte' :
            return CreerCompteView()
        if reponse == "Consulter les 10 meilleurs scores" :
            return ViewTopTen()
        # if reponse == "Quitter le jeu":
        print('Au revoir')
        sys.exit(1)
