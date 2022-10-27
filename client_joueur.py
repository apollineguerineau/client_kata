import os
from typing import List, Optional
from utils.singleton import Singleton
import requests

END_POINT="/joueur"

class ClientJoueur(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def get_pseudo(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json()['pseudo'])

    def create_joueur(self, pseudo):
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")

    def get_nom_listes(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/liste")
        if req.status_code==200:
            row=req.json()
        return(row)
                

client=ClientJoueur()
print(client.get_pseudo(5))
# client.create_joueur(('essai'))
print(client.get_nom_listes(5))