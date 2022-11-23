""" Importation des classes TestCase et Joueur
"""
from unittest import TestCase
from business_objects.joueur import Joueur


class TestJoueur(TestCase) :
    """ Cette classe sert à tester les méthodes __init__() et __str__ de la classe Joueur
    """

    def test__init__joueur(self) :
        """ test de la méthode __init__()
        """
        id_joueur = 10
        nom_joueur = "Toto"
        topten = []

        joueur1 = Joueur(id_joueur, nom_joueur, topten)

        self.assertEqual(10, joueur1.id_joueur)
        self.assertEqual('Toto', joueur1.nom_joueur)
        self.assertEqual([], joueur1.topten)

    def test__str__joueur(self) :
        """ test de la méthode __str__
        """
        id_joueur = 9
        nom_joueur = "OUSSAMA"
        topten = []

        joueur2 = Joueur(id_joueur, nom_joueur, topten)

        self.assertEqual("l'identifiant du joueur est 9" +
        "\nle nom du joueur est OUSSAMA" +
        "\nla liste des top ten est []", str(joueur2))
    
if __name__ == "__main__" :
    print(TestJoueur().test__init__joueur())
    print(TestJoueur().test__str__joueur())