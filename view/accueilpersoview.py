from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

from business_objects.joueur import Joueur


class AccueilPersoView (AbstractView) :

    def __init__(self):
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
        elif reponse== 'Jouer':
            from view.jouerview import JouerView
            return JouerView()
        elif reponse== 'Créer une liste perso':
            from view.creerlistepersoview import CreerListePersoView
            return CreerListePersoView()
        elif reponse== 'Consulter une liste perso':
            from view.consulterlistepersoview import ConsulterListePersoView
            return ConsulterListePersoView()
        elif reponse == 'Meilleurs scores' :
            from view.toptenpersoview import TopTenPersoView
            return TopTenPersoView()
        elif reponse == 'Se déconnecter' :
            from view.accueilkataview import AccueilKataView
            return AccueilKataView()