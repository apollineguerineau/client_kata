from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

class JouerView (AbstractView) :
    def __init__(self):
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        partie = clientjoueur.get_partie(Session().joueur.id_joueur)
        if partie != None :

            self.__questions = inquirer.select(
                message=f'Que souhaites-tu faire?'
                , choices=[
                    Choice('Nouvelle partie')
                    ,Choice('Reprendre la partie')
                ]
        )
        else :
            from view.difficulteview import DifficulteView
            return DifficulteView()
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nouvelle partie':
            from view.difficulteview import DifficulteView
            return DifficulteView()
        elif reponse == 'Reprendre la partie':
            from client_joueur import ClientJoueur
            clientjoueur = ClientJoueur()
            partie = clientjoueur.get_partie(Session().joueur.id_joueur)
            Session().partie = partie
            from business_objects.proposition import Proposition
            for mot in partie.liste_mots_proposes :
                mot_propose = Proposition(mot)
                proposition = partie.verifie_proposition(mot_propose)
                print(proposition)
            from view.propositionview import PropositionView
            return PropositionView()
            
        
