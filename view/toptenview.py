from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session



class ViewTopTen(AbstractView):


    def display_info(self):
        print(f"Voici les 10 meilleurs scores") 

    def make_choice(self):
        from client_top_ten_general import ClientTopTen
        clienttopten = ClientTopTen()
        scores = clienttopten.consulter_top_ten_general()
        for score in scores :
            print(score)
        from view.accueilkataview import AccueilKataView
        return AccueilKataView()
            
        
        
