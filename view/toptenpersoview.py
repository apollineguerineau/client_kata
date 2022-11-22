"""gère l'affichage des 10 meilleurs scores du joueur en cours
"""

from view.abstractview import AbstractView
from view.session import Session


#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class TopTenPersoView(AbstractView):
    """gère l'affichage des 10 meilleurs scores du joueur en cours
    """
    def display_info(self):
        print("Voici tes 10 meilleurs scores")

    def make_choice(self):
        #pylint: disable=unused-import
        #justification: on utilise des objets à importer quand même. cf amélioration possible
        from business_objects.joueur import Joueur
        meilleurs_scores = Session().joueur.topten
        for score in meilleurs_scores :
            print(score)
        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()
