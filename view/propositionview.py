from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstractview import AbstractView
from view.session import Session

from business_objects.partie import Partie
from business_objects.difficultes import Difficultes

prop_faites = len(Session().partie.liste_mots_proposes)
nb_tentatives = int(Session().partie.difficultes.nb_tentatives)

nb_prop_restantes = nb_tentatives - prop_faites
ASK_PROPOSITION =inquirer.text(message = f'Quel mot veux tu proposer? Il te reste {nb_prop_restantes} proposition(s)')



class PropositionView(AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        mot = ASK_PROPOSITION.execute()
        
        from business_objects.proposition import Proposition
        proposition = Proposition(mot)
        print(proposition)
        from business_objects.proposition_verifiee import PropositionVerifiee
        
        partie = Session().partie
        propositionverifiee = partie.verifie_proposition(proposition)
        print(Session().partie.liste_mots_proposes)
        Session().partie.liste_mots_proposes.append(proposition.mot) 
        print(Session().partie.liste_mots_proposes)
        prop_faites = len(Session().partie.liste_mots_proposes)
        nb_prop_restantes = nb_tentatives - prop_faites
        print(propositionverifiee)

        mot_obj = Proposition(partie.mot_objectif)
        print(mot_obj.mot)
        if mot_obj.mot == proposition.mot :
            print("Félicitations, vous avez trouvé le mot")
            partie.calcul_score()
            score = str(partie.score)
            print(f'Votre score est de {score} points')
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
        
        if len(Session().partie.liste_mots_proposes) == partie.difficultes.nb_tentatives :
            print("Tu as perdu car tu as dépassé le nombre de tentatives autorisé")
            from view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()

        else :
            return PropositionView()
            

        



        
        