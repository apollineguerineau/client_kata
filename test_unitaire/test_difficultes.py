""" Importation des classes TestCase et Difficultes
"""
from unittest import TestCase
from business_objects.difficultes import Difficultes


class TestJoueur(TestCase) :
    """ Cette classe sert à tester les méthodes __init__() et __str__ de la classe Difficultes
    """

    def test__init__difficultes(self) :
        """ test de la méthode __init__()
        """
        nb_tentatives = 4
        indice = False

        difficultes1 = Difficultes(nb_tentatives=nb_tentatives, indice=indice)

        self.assertEqual(4, difficultes1.nb_tentatives)
        self.assertEqual(8, difficultes1.temps)
        self.assertEqual(False, difficultes1.indice)
        self.assertAlmostEqual(6, difficultes1.nb_lettres)

    def test__str__difficultes(self) :
        """ test de la méthode __str__
        """
        temps = 10
        nb_lettres = 7

        difficultes2 = Difficultes(temps=temps, nb_lettres=nb_lettres)

        self.assertEqual('6 tentatives, 10 secondes par tentatives, avec indice, mot de 7 lettres'
                         , str(difficultes2))

if __name__ == "__main__" :
    print(TestJoueur().test__init__difficultes())
    print(TestJoueur().test__str__difficultes())
