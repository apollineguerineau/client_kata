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
        '''Retourne un mot selon son identifiant

        Parameters: l'identifiant du mot : int

        Returns:
            str : le mot'''
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())


    def ajouter_mot(self, id_liste, id_mot) :
        '''Ajoute un mot à une liste dans la base de données

        Parameters: l'identifiant de la liste : int, l'identifiant du mot : int'''
        req = requests.post(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")


    def supprimer_mot(self, id_liste, id_mot):
        '''Supprime un mot dans la liste

        Parameters: l'identifiant de la liste : int, l'identifiant du mot : int'''
        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}/mot/{id_mot}")


    def supprimer_liste(self, id_liste):
        '''Supprime une liste dans la bdd

        Parameters: l'identifiant de la liste : int'''

        req = requests.delete(f"{self.__HOST}{END_POINT}/{id_liste}")

