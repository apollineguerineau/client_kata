from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

from business_objects.partie import Partie
from business_objects.difficultes import Difficultes



class PropositionView(AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        prop_faites = len(Session().partie.liste_mots_proposes)
        nb_tentatives = int(Session().partie.difficultes.nb_tentatives)

        nb_prop_restantes = nb_tentatives - prop_faites
        ASK_PROPOSITION =inquirer.text(message = f'Quel mot veux tu proposer? Il te reste {nb_prop_restantes} proposition(s)')

        mot = ASK_PROPOSITION.execute()
        
        from business_objects.proposition import Proposition
        proposition = Proposition(mot)
        print(proposition)
        from business_objects.proposition_verifiee import PropositionVerifiee
        
        partie = Session().partie
        if proposition.est_autorise() and len(proposition.mot) == partie.difficultes.nb_lettres :
            propositionverifiee = partie.verifie_proposition(proposition)
            Session().partie.liste_mots_proposes.append(proposition.mot) 
            prop_faites = len(Session().partie.liste_mots_proposes)
            nb_prop_restantes = nb_tentatives - prop_faites
            print(propositionverifiee)
        else :
            print("Le mot proposé n'est pas autorisé") 


        mot_obj = Proposition(partie.mot_objectif)
        print(mot_obj.mot)
        if mot_obj.mot == proposition.mot :
            print("Félicitations, vous avez trouvé le mot")
            partie.calcul_score()
            score = str(partie.score)
            print(f'Votre score est de {score} points')
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
        
        elif nb_prop_restantes == 0 :
            print("Tu as perdu car tu as dépassé le nombre de tentatives autorisé")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        else :
            from view.pauseview import PauseView
            return PauseView()
            

        



        
        