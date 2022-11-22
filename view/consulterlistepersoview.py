"""permet d'afficher les listes de mots personnalisées
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

#pylint: disable=unused-import
# vient de get_listes ligne 43, qui retourne une liste de Listes OU None
from business_objects.liste import Liste

from client_joueur import ClientJoueur

from view.abstractview import AbstractView
from view.session import Session

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
#pylint: disable=no-value-for-parameter
class ConsulterListePersoView (AbstractView) :
    """gère la vue en console de l'affichage des listes de mots personnalisées
    """
    def __init__(self):
        #pylint: disable=no-value-for-parameter
        id_joueur = Session().joueur.id_joueur

        clientjoueur = ClientJoueur()
        listes = clientjoueur.get_listes(id_joueur)


        if listes is not None :
            self.__questions = inquirer.select(
                message='Quelle liste veux tu sélectionner?'
                , choices = [Choice(liste.nom) for liste in listes]
            )

    def display_info(self):
        pass

    def make_choice(self):
        id_joueur = Session().joueur.id_joueur

        clientjoueur = ClientJoueur()
        listes = clientjoueur.get_listes(id_joueur)
        if listes is not None :
            nom_liste = self.__questions.execute()

            id_joueur = Session().joueur.id_joueur

            clientjoueur = ClientJoueur()
            listes = clientjoueur.get_listes(id_joueur)

            for liste in listes :
                if liste.nom == nom_liste :
                    # id_liste = liste.id_liste code mort
                    Session().liste = liste
                    liste_mots = liste.liste
            for mot in liste_mots :
                print(mot)

            from view.modificationlisteview import ModificationListeView
            return ModificationListeView()

        print("Tu n'as pas encore de liste perosnnalisée")

        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()
