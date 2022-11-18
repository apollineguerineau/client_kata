import os
from typing import List, Optional
from utils.singleton import Singleton
import requests
from business_objects.liste import Liste


END_POINT="/liste"

class ClientListe(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    #ça marche
    def get_mot(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())

    #ça marche
    def ajouter_mot(self, id_liste, id_mot) :
        """Ajouter le mot ayant l'identifiant <id_mot> dans la liste ayant l'identifiant <id_liste>

        Args:
            id_liste : identifiant de la liste
            id_mot : identifiant du mot
        """
        req = requests.post(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")

    #ça marche
    def supprimer_mot(self, id_liste, id_mot):
        """Supprimer le mot ayant l'identifiant <id_mot> de la liste ayant l'identifiant <id_liste>

        Args:
            id_liste : identifiant de la liste
            id_mot : identifiant du mot
        """
        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")
        print(req.status_code)

    #ça marche
    def supprimer_liste(self, id_liste):
        """Supprimer la liste ayant l'identifiant <id_liste>

        Args:
            id_liste : identifiant de la liste
        """
        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}")

# client_liste=ClientListe()
# id=[4,5,8,12,16,29,30]
# for mot in id: 
#     client_liste.ajouter_mot(9, mot)
# print(client_liste.get_mot(9))
# client_liste.supprimer_mot(8,4)
# print(client_liste.get_mot(8))
# client_liste.supprimer_liste(8)
