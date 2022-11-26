"""gère l'affichage pour faire une proposition au cours d'une partie
"""
import time
import re
from InquirerPy import inquirer

#pylint: disable=unused-import
#justification: on utilise des objets à importer quand même. cf amélioration possible
from business_objects.partie import Partie
from business_objects.difficultes import Difficultes

from view.abstractview import AbstractView
from view.session import Session


#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class PropositionView(AbstractView) :

    """gère l'affichage pour faire une proposition au cours d'une partie
    """
    def display_info(self):
        pass

    def make_choice(self):
        #pylint: disable=too-many-locals
        #justification: on a besoin de ces variables locales
        prop_faites = len(Session().partie.liste_mots_proposes)
        nb_tentatives = int(Session().partie.difficultes.nb_tentatives)
        nb_prop_restantes = nb_tentatives - prop_faites
        
        if nb_prop_restantes == 0 :
            print("Tu as perdu car tu as dépassé le nombre de tentatives autorisé")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        temps = time.time()
        ask_proposition =inquirer.text(
            message = f'Quel mot veux tu proposer? Il te reste {nb_prop_restantes} proposition(s)')
        mot = ask_proposition.execute()
        temps2 = time.time()
        if temps2 - temps > float(Session().partie.difficultes.temps) :
            print("Tu as dépassé le temps autorisé pour faire une proposition")
            Session().partie.liste_mots_proposes.append("Proposition invalide")
            from view.pauseview import PauseView
            return PauseView()

        exp_reg1 = r'\w+'
        exp_reg2 = r'\D*'
        if re.fullmatch(exp_reg1, mot) is None or re.fullmatch(exp_reg2, mot) is None :
            print("Le mot ajouté n'est pas valide. Il ne doit contenir que des lettres")
            Session().partie.liste_mots_proposes.append("Proposition invalide")

        else :
            from business_objects.proposition import Proposition
            proposition = Proposition(mot)
            print(proposition)
            from business_objects.proposition_verifiee import PropositionVerifiee

            partie = Session().partie
            Session().partie.liste_mots_proposes.append(proposition.mot)
            prop_faites = len(Session().partie.liste_mots_proposes)
            nb_prop_restantes = nb_tentatives - prop_faites
            if (proposition.est_autorise() or partie.est_liste_perso) \
            and len(proposition.mot) == partie.difficultes.nb_lettres  :
                propositionverifiee = partie.verifie_proposition(proposition)
                print(propositionverifiee)
            else :
                print("Le mot proposé n'est pas autorisé. " +
                    f"Le mot attendu est de {partie.difficultes.nb_lettres} lettres")


            mot_obj = Proposition(partie.mot_objectif)
            if mot_obj.mot == proposition.mot :
                print("Félicitations, tu as trouvé le mot")
                if not Session().partie.est_liste_perso :
                    partie.calcul_score()
                    score = str(partie.score)
                    from client_joueur import ClientJoueur
                    clientjoueur = ClientJoueur()
                    clientjoueur.ajoute_score(Session().joueur.id_joueur, partie.score)
                    Session().joueur = clientjoueur.get_joueur(Session().joueur.nom_joueur)
                    print(f'Ton score est de {score} points')
                from view.accueilpersoview import AccueilPersoView
                return AccueilPersoView()

        if nb_prop_restantes == 0 :
            print("Tu as perdu car tu as dépassé le nombre de tentatives autorisé")
            print(f"Le mot à trouver étatit {Session().partie.mot_objectif}")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        from view.pauseview import PauseView
        return PauseView()
