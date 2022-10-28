

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

class AccueilKataView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour'
            , choices=[
                Choice('Se connecter')
                ,Choice('Créer un compte')
                ,Choice("Consulter les 10 meilleurs scores")]
        )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Se connecter' :
            from view.connectionview import ConnectionView
            return ConnectionView()
        elif reponse == 'Créer un compte' :
            from view.creercompteview import CreerCompteView
            return CreerCompteView()
        elif reponse == "Consulter les 10 meilleurs scores" :
            from view.toptenview import ViewTopTen
            return ViewTopTen()




