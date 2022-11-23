"""Importation des classe TestCase et Liste
"""
from unittest import TestCase
from business_objects.liste import Liste

class TestListe(TestCase) :
    """ Cette classe sert à tester les méthode __init__ et __str__ de la classe liste
    """
    def test__init__liste(self) :
        """ test de la méthode __init__
        """
        id_liste = 10
        liste = ["jouer","tester"]
        nom = "liste_oussama"

        liste1 = Liste(id_liste, liste, nom)

        self.assertEqual(10, liste1.id_liste)
        self.assertEqual(["jouer","tester"], liste1.liste)
        self.assertEqual("liste_oussama", liste1.nom)

    def test__str__liste(self) :
        """ test de la méthode __str__
        """
        id_liste = 9
        liste = ["jouer","tester"]
        nom = "liste_toto"

        liste2 = Liste(id_liste, liste, nom)
        
        self.assertEqual("l'identifiant de la liste est : 9" +
        "\nle nom de la liste est : liste_toto" +
        "\nla liste des mots est : ['jouer', 'tester']", str(liste2))
    
if __name__ == "__main__" :
    print(TestListe().test__init__liste())
    print(TestListe().test__str__liste())
