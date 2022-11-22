from unittest import TestCase
from business_objects.partie import Partie
from business_objects.proposition import Proposition
from business_objects.difficultes import Difficultes
from colorama import init
init()

class TestPartie(TestCase) :
    def test_occurence_lettres(self) :
        liste_mots_proposes = []
        est_liste_perso = False
        difficultes = Difficultes()
        mot_objectif = 'ANIMAL'
    
        partie1 = Partie(liste_mots_proposes, est_liste_perso, difficultes, mot_objectif)

        self.assertEqual([['A',2],['N',1],['I',1],['M',1],['L',1]], partie1.occurence_lettres())

    def test_verifie_proposition(self) : 
        liste_mots_proposes = []
        est_liste_perso = False
        difficultes = Difficultes()
        mot_objectif = 'OISEAU'
        mot_propose = Proposition('BUREAU')
        
        #couleur_noir = '\x1b[1;37;40m'
        #couleur_jaune = '\x1b[1;30;43m'
        #couleur_vert = '\x1b[1;37;42m'
        #reset_style = '\x1b[0m'

        resultat_attendu = '\x1b[1;37;40m' + ' B '+ '\x1b[0m'+'\x1b[1;30;43m' +' U '+ '\x1b[0m'+'\x1b[1;37;40m'+ ' R ' + '\x1b[0m'+'\x1b[1;37;42m' + ' E '+ '\x1b[0m'+'\x1b[1;37;42m'+' A '+'\x1b[0m'+'\x1b[1;37;42m'+' U '+'\x1b[0m'
    
        partie1 = Partie(liste_mots_proposes, est_liste_perso, difficultes, mot_objectif)
        
        self.assertEqual(resultat_attendu, f'{partie1.verifie_proposition(mot_propose)}')
        
        #print(resultat_attendu)
        #print(f'{partie1.verifie_proposition(mot_propose)}')

if __name__ =="__main__" :
    test = TestPartie()
    print(test.test_occurence_lettres())
    print(test.test_verifie_proposition())