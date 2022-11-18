from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

class PauseView (AbstractView) :
    def __init__(self):
        self.__questions = inquirer.select(
                message=f'Que souhaites-tu faire?'
                , choices=[
                    Choice('Faire une nouvelle proposition')
                    ,Choice('Pause')
                ]
            )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Faire une nouvelle proposition' :
            from view.propositionview import PropositionView
            return PropositionView()
        elif reponse == 'Pause' :
            #create_partie_en_cours(Session)
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()