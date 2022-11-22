"""gère l'affichage des 10 meilleurs scores globaux
"""
from view.abstractview import AbstractView


#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class ViewTopTen(AbstractView):
    """gère l'affichage des 10 meilleurs scores globaux
    """


    def display_info(self):
        print("Voici les 10 meilleurs scores")

    def make_choice(self):
        from client_top_ten_general import ClientTopTen
        clienttopten = ClientTopTen()
        scores = clienttopten.consulter_top_ten_general()
        for score in scores :
            print(score)
        from view.accueilkataview import AccueilKataView
        return AccueilKataView()
