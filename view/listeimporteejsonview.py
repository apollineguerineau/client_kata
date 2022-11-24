from email.message import Message
from pprint import pprint


from InquirerPy import inquirer

from client_joueur import ClientJoueur

from view.abstractview import AbstractView
from view.session import Session

#TODO code à finir


ASK_NOM_LISTE=inquirer.text(message = 'Quel est le nom de ta nouvelle liste?')
ASK_LIEN_dossier=inquirer.text(message = 'Quel est le lien du dossier où se trouve ta liste?')
ASK_LIEN_fichier=inquirer.text(message = 'Quel est le lien du fichier où se trouve ta liste?')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class ListeImporteeJSONView(AbstractView):
    """gère l'affichage des listes importées au format JSON
    """

    def display_info(self):
        print("Création d'une liste JSON")

    def make_choice(self):
        nom_liste = ASK_NOM_LISTE.execute()
        lien_dossier = ASK_LIEN_dossier.execute()
        lien_fichier = ASK_LIEN_fichier.execute()

        if re.fullmatch(exp_reg1, nom_liste) is None :
            print("Le nom de liste n'est pas autorisé. Seuls les lettres et les chiffres sont autorisés")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        from importation_objects.importation_json import ImportationJson
        importation = ImportationJson()
        liste_mots = importation.creer(lien_fichier, lien_dossier)
        if liste_mots != None :
            
            clientjoueur = ClientJoueur()
            id_joueur = Session().joueur.id_joueur

            clientjoueur.create_liste(id_joueur, nom_liste)

            from business_objects.proposition import Proposition
            from client_mot import ClientMot
            clientmot = ClientMot()
            for mot in liste_mots :
                clientmot.add_mot_to_liste(mot, nom_liste, Session().joueur.id_joueur)
        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()
