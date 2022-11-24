""" Importation des classes TestCase et Proposition
"""
from unittest import TestCase
from business_objects.proposition import Proposition

class TestProposition(TestCase) :
    """ Cette classe sert à tester les méthodes :
    - est_autorise()
    - majuscule()
    - supprime_accent()
    - transforme_proposition
    de la classe Proposition
    """
    def test_est_autorise(self) :
        """ test de la méthode : est_autorise()
        """
        mot1 = "uhujhbj"
        mot2 = "Sky"

        prop1 = Proposition(mot1)
        prop2 = Proposition(mot2)

        self.assertEqual(False, prop1.est_autorise())
        self.assertEqual(True, prop2.est_autorise())

    def test_majuscule(self) :
        """test de la méthode : majuscule()
        """
        mot = "hEllOWorLD"

        prop = Proposition(mot)

        self.assertEqual("HELLOWORLD", prop.majuscule())

    def test_supprime_accent(self) :
        """ test de la méthode : supprime_accent()
        """
        mot = "éàlîêmc"

        prop = Proposition(mot)

        self.assertEqual("ealiemc", prop.supprime_accent())

    def test_transforme_proposition(self) :
        """ test de la méthode : transforme_proposition()
        """
        mot = "EyêLmîkà"

        prop = Proposition(mot)
        prop.transforme_proposition()

        self.assertEqual("EYELMIKA", prop.mot)


if __name__ == "__main__" :
    test = TestProposition()

    print("test est_autorise()")
    print(test.test_est_autorise())

    print("test majuscule()")
    print(test.test_majuscule())

    print("test supprime_accent()")
    print(test.test_supprime_accent())

    print("test transforme_proposition()")
    print(test.test_transforme_proposition())
