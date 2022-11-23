""" Importation des modules et classes suivantes :
    - TestCase
    - Partie
    - Proposition
    - Difficultes
    - colorama
"""
from unittest import TestCase
from colorama import init
from business_objects.partie import Partie
from business_objects.proposition import Proposition
from business_objects.difficultes import Difficultes
init()

class TestPartie(TestCase) :
    """ Cette classe sert à tester les méthodes suivantes de la classe Partie :
    - occurence_lettres()
    - verifie_proposition()
    """
    def test_occurence_lettres(self) :
        """ test de la méthode : occurence_lettres()
        """
        liste_mots_proposes = []
        est_liste_perso = False
        difficultes = Difficultes()
        mot_objectif = 'ANIMAL'
        id_liste = 1
    
        partie1 = Partie(liste_mots_proposes, est_liste_perso, difficultes, mot_objectif, id_liste)

        self.assertEqual([['A',2],['N',1],['I',1],['M',1],['L',1]], partie1.occurence_lettres())

    def test_verifie_proposition(self) :
        """ test de la méthode : verifie_proposition()
        """
        liste_mots_proposes = []
        est_liste_perso = False
        difficultes = Difficultes()
        mot_objectif = 'OISEAU'
        id_liste = 2
        mot_propose = Proposition('BUREAU')
        
        #couleur_noir = '\x1b[1;37;40m'
        #couleur_jaune = '\x1b[1;30;43m'
        #couleur_vert = '\x1b[1;37;42m'
        #reset_style = '\x1b[0m'

        resultat_attendu = '\x1b[1;37;40m' + ' B '+ '\x1b[0m'+'\x1b[1;30;43m' +' U '+ '\x1b[0m'+'\x1b[1;37;40m'+ ' R ' + '\x1b[0m'+'\x1b[1;37;42m' + ' E '+ '\x1b[0m'+'\x1b[1;37;42m'+' A '+'\x1b[0m'+'\x1b[1;37;42m'+' U '+'\x1b[0m'
    
        partie1 = Partie(liste_mots_proposes, est_liste_perso, difficultes, mot_objectif, id_liste)
        
        self.assertEqual(resultat_attendu, f'{partie1.verifie_proposition(mot_propose)}')
        
        #print(resultat_attendu)
        #print(f'{partie1.verifie_proposition(mot_propose)}')


if __name__ =="__main__" :
    test = TestPartie()
    print(test.test_occurence_lettres())
    print(test.test_verifie_proposition())