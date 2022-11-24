"""gère l'affichage pour créer une liste manuellement
"""

from InquirerPy import inquirer
import re

from view.abstractview import AbstractView
from view.session import Session


ASK_NOM_LISTE=inquirer.text(message = 'Quel est le nom de ta nouvelle liste?')
ASK_PREMIER_MOT=inquirer.text(message = 'Quel est le premier mot de la liste?')

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
#pylint: disable=no-value-for-parameter
# justification : voir axe d'amélioration sur les bloc TRY Except + doc API
class CreerListeManuelleView(AbstractView):
    """permet de créer des listes manuellement en console
    """

    def display_info(self):
        print("Création d'une liste")

    def make_choice(self):
        nom_liste = ASK_NOM_LISTE.execute()
        mot = ASK_PREMIER_MOT.execute()

        exp_reg1 = r'\w+'
        exp_reg2 = r'\D*'
        if re.fullmatch(exp_reg1, nom_liste) is None :
            print("Le nom de liste n'est pas autorisé. Seuls les lettres et les chiffres sont autorisés")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        if re.fullmatch(exp_reg1, mot) is None or re.fullmatch(exp_reg2, mot) is None :
            print("Le mot ajouté n'est pas valide. Il ne doit contenir que des lettres")
        
        else :
            #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule
            from business_objects.proposition import Proposition
            proposition = Proposition(mot)
            mot = proposition.mot

            #On récupère ensuite le nom de toutes les listes du
            # joueur pour ne pas créer deux listes avec le même nom
            id_joueur = (Session().joueur.id_joueur)
            from client_joueur import ClientJoueur
            clientjoueur = ClientJoueur()
            #pylint: disable=unused-import
            #justification: get_listes retourne une liste de Liste(s)
            if re.fullmatch(exp_reg1, nom_liste) is None :
                print ("Le nom de la liste est invalide." +
                        "Ce nom ne doit contenir que des chiffres et des lettres")
                
            else :   
                listes = clientjoueur.get_listes(id_joueur)
                from business_objects.liste import Liste
                if listes is not None :
                    for liste in listes :
                        if liste.nom == nom_liste :
                            print("Tu as déjà une liste avec ce nom")
                            from view.accueilpersoview import AccueilPersoView
                            return AccueilPersoView()

                clientjoueur.create_liste(id_joueur, nom_liste)

                from client_mot import ClientMot
                clientmot = ClientMot()
                clientmot.add_mot_to_liste(mot, nom_liste, Session().joueur.id_joueur)

        from view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()
