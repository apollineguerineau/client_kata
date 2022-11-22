"""gère la vue e nconsole pour l'accueil personnalisé
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session


class AccueilPersoView (AbstractView) :
    """permet de gérer l'accueil personnalisé
    """
    def __init__(self):
        #pylint: disable=no-value-for-parameter
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().joueur.nom_joueur}'
            , choices=[
                Choice('Jouer')
                ,Choice('Créer une liste perso')
                ,Choice('Consulter une liste perso')
                ,Choice('Meilleurs scores')
                ,Choice('Se déconnecter')]
        )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        if reponse== 'Jouer':
            from view.jouerview import JouerView
            return JouerView()
        if reponse== 'Créer une liste perso':
            from view.creerlistepersoview import CreerListePersoView
            return CreerListePersoView()
        if reponse== 'Consulter une liste perso':
            from view.consulterlistepersoview import ConsulterListePersoView
            return ConsulterListePersoView()
        if reponse == 'Meilleurs scores' :
            from view.toptenpersoview import TopTenPersoView
            return TopTenPersoView()
        # if reponse == 'Se déconnecter' :
        from view.accueilkataview import AccueilKataView
        return AccueilKataView()
