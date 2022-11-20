"""permet d'avoir une classe mère abstraite pour générer des mots
"""
from abc import ABC, abstractmethod

class AbstractGenererMot(ABC):
    # pylint: disable=too-few-public-methods
    """classe abstraite mère pour la génération de mot

    Parameters
    ----------
    ABC : ABC
        la classe de base du package abc
    """
    def __init__(self):
        """constructeur abstrait vide
        """

    @abstractmethod
    def generer(self):
        """méthode abstraite vide
        """
