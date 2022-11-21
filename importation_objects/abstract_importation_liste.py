"""classe abstraite pour l'importation des fichiers
classe mère de ImportationJson, Importation_csv et ImportationManuelle
"""
from abc import ABC, abstractmethod

class AbstractImportationListe(ABC):
    """classe abstraite pour l'importation des listes
    """
    #pylint: disable=unnecessary-pass
    #pylint: disable=too-few-public-methods
    @abstractmethod
    def __init__(self):
        """_summary_
        """
        pass


    @abstractmethod
    def creer(self):
        """renvoie une Liste
        """
        pass
