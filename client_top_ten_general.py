"""couche service : gère le endpoint pour consulter le top10 général
"""


import requests
from utils.singleton import Singleton

END_POINT="/top10"

#pylint: disable=invalid-name
#justification: le __HOST pourrait reservir pour un déploiement
#pylint: disable=too-few-public-methods
#justification: pas besoin de méthode supplémentaire

class ClientTopTen(metaclass= Singleton):
    """gère le endpoint pour consulter le top10 général
    """
    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def consulter_top_ten_general(self):
        '''Retourne le top 10 général
        '''
        req = requests.get(f"{self.__HOST}{END_POINT}")
        return req.json() #suppression parenthèses testé
