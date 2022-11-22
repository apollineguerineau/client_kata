"""gère l'affichage lors de la suppression d'un mot d'une liste
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class SupprimerMotView (AbstractView) :
    """gère l'affichage lors de la suppression d'un mot d'une liste
    """
    def __init__(self):

        self.__questions = inquirer.select(
            message=f'Quel mot veux tu supprimer à ta liste {Session().liste.nom}?'
            , choices = [Choice(mot) for mot in Session().liste.liste]
        )


    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()

        from client_mot import ClientMot
        clientmot = ClientMot()
        id_mot = clientmot.get_id(reponse)

        liste_mots = Session().liste
        from client_liste import ClientListe
        clientliste = ClientListe()
        id_liste = liste_mots.id_liste
        clientliste.supprimer_mot(id_liste, id_mot)
        #pylint: disable=unused-import
        #justification: on utilise des objets à importer quand même. cf amélioration possible
        from business_objects.proposition import Proposition

        #A revoir cette partie
        #pylint: disable=consider-using-enumerate
        #justification: ne renvoie pas le même type
        for i in range (0, len(Session().liste.liste)) :
            if Session().liste.liste[i] == reponse :
                Session().liste.liste.pop(i)

        if len(liste_mots.liste) == 1 :
            clientliste.supprimer_liste(id_liste)
            print("La liste a été supprimée")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        from view.modificationlisteview import ModificationListeView
        return ModificationListeView()
