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

    def get_id(self, pseudo) :
        req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
        return(req.json()['id_joueur'])    

    def create_joueur(self, pseudo):
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")
        return(req)

    def get_nom_listes(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/liste")
        return(req.json())
                
    def create_liste(self, id, name):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/liste/{name}")


client=ClientJoueur()
print(client.get_pseudo(5))
print(client.get_id("Apolline"))
# print(client.create_joueur(('essai2')))
print(client.get_nom_listes(5))
client.create_liste(5, "super_liste")
