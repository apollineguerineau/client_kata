from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
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
            from client_joueur import ClientJoueur
            clientjoueur = ClientJoueur()
            clientjoueur.create_partie_en_cours(Session().joueur.id_joueur, Session().partie)
            for mot in Session().partie.liste_mots_proposes :
                clientjoueur.ajoute_proposition(Session().joueur.id_joueur, mot)
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()