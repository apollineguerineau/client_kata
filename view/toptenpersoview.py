from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session



class ViewTopTenPerso(AbstractView):


    def display_info(self):
        print(f"Voici tes 10 meilleurs scores") 

    def make_choice(self):
        from business_objects.joueur import Joueur
        meilleurs_scores = Session().joueur.topten
        for score in meilleurs_scores :
            print(score)
        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()