from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session




ASK_PSEUDO=inquirer.text(message = 'Entre un pseudo')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)

class CreerCompteView(AbstractView):


    def display_info(self):
        print(f"Création du compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        if clientjoueur.get_id(pseudo) == None :
            #Le joueur est inséré dans la base de données
            clientjoueur.create_joueur(pseudo = pseudo)
        else :
            #Message d'erreur
            print("Le pseudo existe déjà")
        #Dans tous les cas, on revient ensuite à l'écran d'accueil
        from view.accueilkataview import AccueilKataView
        return AccueilKataView()