"""gère l'affichage pour la création d'une liste de mots personnalisée
"""
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class CreerListePersoView (AbstractView) :
    """gère l'affichage pour créer une liste de mots personnalisée
    """
    def __init__(self):
        #pylint: disable=no-value-for-parameter
        # justification: la Session a bien un Joueur
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().joueur.nom_joueur}'
            , choices=[
                Choice('Créer une liste manuellement')
                ,Choice('Importer une liste CSV')
                ,Choice('Importer une liste JSON')]
        )

    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse== 'Créer une liste manuellement':
            from view.creerlistemanuelleview import CreerListeManuelleView
            return CreerListeManuelleView()
        if reponse== 'Importer une liste CSV':
            from view.listeimporteecsvview import ListeImporteeCSVView
            return ListeImporteeCSVView()
        # if reponse== 'Importer une liste JSON':
        from view.listeimporteejsonview import ListeImporteeJSONView
        return ListeImporteeJSONView()
