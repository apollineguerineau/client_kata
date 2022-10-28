import os
from typing import List, Optional
from utils.singleton import Singleton
import requests
from business_objects.liste import Liste


END_POINT="/liste"

class ClientListe(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"


    def get_mot(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())


    def ajouter_mot(self, id_liste, id_mot) :
        req = requests.post(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")


    def supprimer_mot(self, id_liste, id_mot):
        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")
        print(req.status_code)

    
    def supprimer_liste(self, id_liste):
        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}")

client_liste=ClientListe()
print(client_liste.get_mot(1))
# print(client_liste.supprimer_mot(5,2))
# print(client_liste.get_mot(5))
# client_liste.supprimer_liste(7)
