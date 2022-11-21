"""classe ImportationManuelle pour créer une liste personnalisée à la main
"""

from business_objects.proposition import Proposition
from importation_objects.abstract_importation_liste import AbstractImportationListe

class ImportationManuelle(AbstractImportationListe):
    """permet d'importer une liste manuellement
    """
    #pylint: disable=unnecessary-pass
    #pylint: disable=super-init-not-called
    def __init__(self):
        """_summary_
        """
        pass

    #pylint: disable=no-self-use
    def ajouter_mot(self, nouveau_mot):
        """permet d'ajouter un mot.

        Parameters
        ----------
        nouveau_mot : str
            le mot à ajouter

        Returns
        -------
        str
            le mot ajouté par l'utilisateur
        """
        #on réutilise la classe Proposition pour gérer les accents et minuscules
        mon_mot = Proposition(nouveau_mot)

        return mon_mot.mot
