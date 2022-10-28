from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session


class ConsulterListePersoView (AbstractView) :
    
    def __init__(self):
        id_joueur = Session().joueur.id_joueur
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        listes = clientjoueur.get_listes(id_joueur)

        from business_objects.liste import Liste
        self.__questions = inquirer.select(
            message=f'Quelle liste veux tu sélectionner?'
            , choices = [Choice(liste.nom) for liste in listes]
        )

    def display_info(self):
        pass

    def make_choice(self):
        nom_liste = self.__questions.execute()

        id_joueur = Session().joueur.id_joueur
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        listes = clientjoueur.get_listes(id_joueur)

        for liste in listes :
            if liste.nom == nom_liste :
                id_liste = liste.id_liste
                Session().liste = liste
                liste_mots = liste.liste
        for mot in liste_mots :
            print(mot)
        from view.modificationlisteview import ModificationListeView
        return ModificationListeView()
        
