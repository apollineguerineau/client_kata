"""classe pour importer des fichiers CSV
structurés :
"Apolinne"
"Linh-Da"
"Mathieu"
"Mathis"
"Oussama"
"""

import csv
from importation_objects.abstract_importation_liste import AbstractImportationListe

class ImportationCsv(AbstractImportationListe):
    """permet d'importer des Csv (au format simpliste: pas
    de titre, mots mis ligne à ligne entre '"')

    Parameters
    ----------
    Example
    -------
    """
    #pylint: disable=too-few-public-methods
    #pylint: disable=super-init-not-called
    def __init__(self):
        """_summary_

        Parameters
        ----------
        fichier : str
            nom du fichier avec l'extension .csv
        dossier : str
            chemin du dossier
        encodage : str, optional
            encodage du fichier, by default ' utf-8'

        Example
        -------
        >>> import json
        >>> from importation_objects.abstract_importation_liste import AbstractImportationListe
        >>> ma_liste = ImportationCsv()
        >>> isinstance(ma_liste, ImportationCsv)
        True
        """

    #pylint: disable=arguments-differ
    def creer(self,  fichier : str, dossier : str,
              encodage: str = ' utf-8', separateur : str = ','):
        """retourne une liste de mos à partir d'un fichier CSV

        Parameters
        ----------
        fichier : str
            nom du fichier
        dossier : str
            nom du dossier
        encodage : str, optional
            encodage, by default ' utf-8'
        separateur : str, optional
            séparateur, by default ','

        Returns
        -------
        liste_mots : list[str]

        Examples
        --------
        >>> import csv
        >>> from importation_objects.abstract_importation_liste import AbstractImportationListe
        >>> ma_liste = ImportationCsv()
        >>> chemin = "C:/Users/mathi/Documents/Ensai/2A/S1/Projet informatique"
        >>> res = ma_liste.creer("listeformatCSV.csv", chemin)
        >>> print(res)
        ['Apolinne', 'Mathis', 'Mathieu', 'Linh-da', 'Oussama']
        >>> ma_liste2 = ImportationCsv()
        >>> chemin = "mauvais_chemin"
        >>> res = ma_liste.creer("listeformatCSV.csv", chemin)
        Le lien donné est invalide.
        """
        liste_res = []
        try:
            with open(f'{dossier}/{fichier}','r', newline='', encoding= encodage) as csvfile:
                reader = csv.reader(csvfile, delimiter= separateur)
                for row in reader:
                    liste_res.append(row[0])
            return liste_res
        except FileNotFoundError:
            print('Le lien donné est invalide.')
            return None

if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)
