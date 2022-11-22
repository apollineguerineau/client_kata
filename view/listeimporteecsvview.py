"""gère l'affichage lors de l'importation des listes au format CSV
"""


from InquirerPy import inquirer

from view.abstractview import AbstractView
from view.session import Session

#TODO code à finir


ASK_NOM_LISTE=inquirer.text(message = 'Quel est le nom de ta nouvelle liste?')
ASK_LIEN_dossier=inquirer.text(message = 'Quel est le lien du dossier où se trouve ta liste?')
ASK_LIEN_fichier=inquirer.text(message = 'Quel est le lien du fichier où se trouve ta liste?')
ASK_SEPARATEUR=inquirer.text(message = 'Quel est le séparateur dans ton fichier CSV?')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class ListeImporteeCSVView(AbstractView):
    """gère l'affichage pour l'import des listes au format CSV
    """
    def display_info(self):
        print("Création d'une liste CSV")

    def make_choice(self):
        #pylint: disable=too-many-locals
        #justification: on en a besoin
        nom_liste = ASK_NOM_LISTE.execute()
        lien_dossier = ASK_LIEN_dossier.execute()
        lien_fichier = ASK_LIEN_fichier.execute()

        from importation_objects.importation_csv import ImportationCsv
        importation = ImportationCsv()
        liste_mots = importation.creer(lien_fichier, lien_dossier)

        # from src.dao.joueur_dao import JoueurDAO
        joueurdao = JoueurDAO()
        id_joueur = joueurdao.get_id_by_pseudo(Session().pseudo)

        # from src.dao.liste_dao import ListeDAO
        listedao = ListeDAO()
        listedao.creer(id_joueur, nom_liste)
        id_liste = listedao.id(Session().liste)


        from src.dao.mot_dao import MotDAO
        motdao = MotDAO()
        from business_objects.proposition import Proposition
        for mot in liste_mots :
            #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule
            mot = Proposition(mot)
            mot = Proposition.mot


            if not motdao.find(mot) :
                motdao.creer(mot)
            id_mot = motdao.get_id_by_mot(mot)
            listedao.ajouter_mot(self, id_liste, id_mot)

        from src.view.listeimporteejsonview import ListeImporteeJSONView
        return ListeImporteeJSONView()
