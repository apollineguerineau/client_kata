"""permet de générer les mot à partir de l'API herokuapp.com
"""
import requests
from business_objects.abstract_generer_mot import AbstractGenererMot

class GenererMotApi(AbstractGenererMot):
    # pylint: disable=too-few-public-methods
    """ C'est la classe abstraite GenererMotApi qui sert à generer aléatoirement
    un mot en fixant le nombre de lettres de ce mot
    """
    def __init__(self, nb_lettres):

        """
        Args:
            nb_lettres (int): le nombre de lettres du mot qu'on cherche à generer
        """
        #pylint: disable=super-init-not-called
        self.nb_lettres=nb_lettres

    def generer(self):
        """la méthode <generer> sert à generer aléatoirement un mot à partir de <Random Word API>
        et qui a comme longueur le nombre de lettres déjà choisi
        """
        req=requests.get(f"https://random-word-api.herokuapp.com/word?length={self.nb_lettres}")
        if req.status_code==200:
            res=req.json()[0]
            mot=''
            for lettre in res:
                mot+=lettre.upper()
        return mot
