from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session




ASK_PSEUDO=inquirer.text(message = 'Quel est ton pseudo?')



class ConnectionView(AbstractView):


    def display_info(self):
        print(f"Connexion au compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        if type(clientjoueur.get_id(pseudo)) == int :
            #Compléter les infos de la session
            from view.session import Session
            joueur = clientjoueur.get_joueur(pseudo)
            session = Session(joueur)
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
           
        else :
            print("Le pseudo n'existe pas") 
            from view.accueilkataview import AccueilKataView
            return AccueilKataView()
            
        
        
