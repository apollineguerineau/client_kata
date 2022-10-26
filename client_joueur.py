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

client=ClientJoueur()
print(client.get_pseudo(1))
client.create_joueur(('essai'))