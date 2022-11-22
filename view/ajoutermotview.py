"""permet de gérer e nconsole l'ajout d'un mot
"""
from InquirerPy import inquirer
# from InquirerPy.base.control import Choice

from client_mot import ClientMot

from business_objects.proposition import Proposition

from view.abstractview import AbstractView
from view.session import Session

#pylint: disable=no-value-for-parameter
# justification : voir axe d'amélioration sur les bloc TRY Except + doc API
ASK_MOT=inquirer.text(message = f'Quel mot veux tu ajouter à ta liste {Session().liste.nom}?')
#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)

class AjouterMotView (AbstractView) :
    """_summary_

    Parameters
    ----------
    AbstractView : _type_
        _description_
    """
    def display_info(self):
        pass

    def make_choice(self):
        mot = ASK_MOT.execute()
        #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule

        proposition = Proposition(mot)
        mot = proposition.mot

        clientmot = ClientMot()
        clientmot.add_mot_to_liste(mot, Session().liste.nom, Session().joueur.id_joueur)
        Session().liste.liste.append(mot)


        from view.modificationlisteview import ModificationListeView
        return ModificationListeView()
