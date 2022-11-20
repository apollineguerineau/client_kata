"""contient la classe Difficultes
"""
class Difficultes:
    # pylint: disable=too-few-public-methods
    """C'est la classe qui définit la difficulté d'une partie de jeux par :
    - nb_tentatives
    - temps
    - indice
    - nb_lettres
    """
    def __init__(self,nb_tentatives=6, temps=8, indice=True, nb_lettres=6):
        """
        Args:
            - nb_tentatives (int, optional): le nombres de tentative. Defaults to 6.
            - temps (int, optional): Durée de la partie. Defaults to 8.
            - indice (bool, optional): Le joueur veut un indice ou non. Defaults to True.
            - nb_lettres (int, optional): Le nombre de lettres du mot objectif. Defaults to 6.
        """
        self.nb_tentatives=nb_tentatives
        self.temps=temps
        self.indice=indice
        self.nb_lettres=nb_lettres

    def __str__(self):
        """
        Returns:
            str: nombre de tentatives, nombre de secondes par tentatives, avec ou sans indice, mot de "un nombre" lettres
        EXAMPLE
        -------
        >>> difficultes=Difficultes(None, None ,False,8)
        >>> print(difficultes)
        6 tentatives, 8 secondes par tentatives, sans indice, mot de 8 lettres
        """
        avec_indice = ""
        if self.indice:
            avec_indice="avec indice"
        else:
            avec_indice="sans indice"
        return f"{self.nb_tentatives} tentatives, {self.temps} secondes par tentatives, {avec_indice}, mot de {self.nb_lettres} lettres"
