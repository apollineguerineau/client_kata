import os
from typing import List, Optional
from utils.singleton import Singleton
import requests
from client_liste import ClientListe



END_POINT="/joueur"

class ClientJoueur(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def get_pseudo(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())

    def get_id(self, pseudo) :
        req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
        if req.json()==None:
            return(None)
        else:
            return(req.json()['id_joueur']) 
  

    def create_joueur(self, pseudo):
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")
        return(req)

    # def get_nom_listes(self, id):
    #     req=requests.get(f"{self.__HOST}{END_POINT}/{id}/liste")
    #     nom=req.json()[0]
    #     contenu=req.json()[1]
    #     listes=[]
    #     for i in range(len(nom)):
    #         listes.append(Liste)

                
    def create_liste(self, id, name):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/liste/{name}")

    def consulter_top10(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/score/")
        return(req.json())

    #celle-ci marche pas
    def ajoute_score(self, id, score):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/score/{score}")

client=ClientJoueur()
# print(client.get_pseudo(5))
print(client.get_id("ejkbfe"))
print(client.get_id("Apolline"))
# print(client.create_joueur(('essai2')))
# print(client.get_nom_listes(1))
# client.create_liste(5, "super_liste")
# print(client.consulter_top10(5))
# client.ajoute_score(5, 3000.0)
# print(client.consulter_meilleur_score(5))
