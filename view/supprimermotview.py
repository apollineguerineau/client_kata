from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

class SupprimerMotView (AbstractView) :
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
        taille_liste = len(liste_mots.liste)
        from client_liste import ClientListe
        clientliste = ClientListe()
        id_liste = liste_mots.id_liste
        clientliste.supprimer_mot(id_liste, id_mot)

        if len(liste_mots.liste) == 1 :
            clientliste.supprimer_liste(id_liste)
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        from view.modificationlisteview import ModificationListeView
        return ModificationListeView()

        
