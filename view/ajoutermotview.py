from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

ASK_MOT=inquirer.text(message = f'Quel mot veux tu ajouter à ta liste {Session().liste.nom}?')


class AjouterMotView (AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        mot = ASK_MOT.execute()
        #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule
        from business_objects.proposition import Proposition
        proposition = Proposition(mot)
        mot = proposition.mot
        
        from client_mot import ClientMot
        clientmot = ClientMot()
        clientmot.add_mot_to_liste(mot, Session().liste.nom, Session().joueur.id_joueur)
        
        from view.modificationlisteview import ModificationListeView
        return ModificationListeView()
        
