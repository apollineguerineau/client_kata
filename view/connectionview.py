"""permet de gérer la connexion d'un joueur à son compte
"""

from InquirerPy import inquirer

from client_joueur import ClientJoueur

from view.abstractview import AbstractView
from view.session import Session
from view.accueilkataview import AccueilKataView
from view.accueilpersoview import AccueilPersoView




ASK_PSEUDO=inquirer.text(message = 'Quel est ton pseudo?')



class ConnectionView(AbstractView):
    """permet de gérer la connexion d'un joueur à son compte

    """

    def display_info(self):
        print("Connexion au compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()

        clientjoueur = ClientJoueur()
        print(clientjoueur.get_id(pseudo))
        if isinstance(clientjoueur.get_id(pseudo), int)  :
            #Compléter les infos de la session

            #TODO Axe d'amélioration: faire des blocs TRY Except + doc API
            # pour éviter d'avoir get_joueur qui peut retourner None ou Joueur
            # d'où les disable pylint
            #pylint: disable=unused-variable
            joueur = clientjoueur.get_joueur(pseudo)
            session = Session(joueur)

            return AccueilPersoView()

        print("Le pseudo n'existe pas")

        return AccueilKataView()
