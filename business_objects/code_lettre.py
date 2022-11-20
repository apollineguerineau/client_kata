"""module pour gérer la couleur des lettres affichées
pendant le jeu.
"""
#TODO demander confirmation pour garder les deux lignes suivantes
from colorama import init
init()
class CodeLettre :
    # pylint: disable=too-few-public-methods
    """permet de gérer l'affichage des lettres au cours du jeu
    """
    def __init__(self,lettre, code_couleur):
        """_summary_

        Parameters
        ----------
        lettre : str
            une lettre
        code_couleur : Boolean ou str
            soit True, soit False, soit 'Mal placee'
        """
        self.lettre=lettre
        self.code_couleur=code_couleur
        self.affichage=self.afficher()

    def afficher(self):
        """permet de gérer les couleurs des lettres

        Returns
        -------
        str
            une string qui met la lettre en couleur dans la console
        """
        if self.code_couleur:
            couleur='\x1b[1;37;42m'
        if not self.code_couleur:
            couleur='\x1b[1;37;40m'
        if self.code_couleur=='Mal placee':
            couleur='\x1b[1;30;43m'
        return couleur + ' ' + self.lettre + ' ' +'\x1b[0m'
