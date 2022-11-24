"""permet de gérer l'affichage quand on lance une partie
"""

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session


#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class JouerView (AbstractView) :
    """affiche en console si on veut faire une nouvelle partie ou reprendre l'ancienne
    """
    def __init__(self):
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        partie = clientjoueur.get_partie(Session().joueur.id_joueur)
        if partie is not None :

            self.__questions = inquirer.select(
                message='Que souhaites-tu faire?'
                , choices=[
                    Choice('Nouvelle partie')
                    ,Choice('Reprendre la partie')
                ]
        )

    def display_info(self):
        pass

    def make_choice(self):
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        id_joueur = Session().joueur.id_joueur
        partie_ = clientjoueur.get_partie(id_joueur)
        if partie_ is not None :
            reponse = self.__questions.execute()
        else :
            reponse = 'Nouvelle partie'

        clientjoueur = ClientJoueur()

        if reponse == 'Nouvelle partie':
            clientjoueur.supprime_partie_en_cours(id_joueur)
            from view.difficulteview import DifficulteView
            return DifficulteView()

        # elif reponse == 'Reprendre la partie':
        
        partie = clientjoueur.get_partie(id_joueur)
        clientjoueur.supprime_partie_en_cours(id_joueur)
        Session().partie = partie
        from business_objects.proposition import Proposition
        for mot in partie.liste_mots_proposes :
            mot_propose = Proposition(mot)
            if mot_propose.est_autorise() :
                proposition = partie.verifie_proposition(mot_propose)
                print(proposition)
        from view.pauseview import PauseView
        return PauseView()
