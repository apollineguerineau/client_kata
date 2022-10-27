import os
from typing import List, Optional
from utils.singleton import Singleton
import requests

END_POINT="/mot"

class ClientMot(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"


    def create_mot(self, mot: str) :
        req = requests.post(f"{self.__HOST}{END_POINT}/contenu/{mot}")

    def get_id_by_mot(self, mot: str):
        req = requests.get(f"{self.__HOST}{END_POINT}/{mot}")
        return(req.json())

mot_client=ClientMot()
# print(mot_client.create_mot("FENETRE"))
print(mot_client.get_id_by_mot("FENETRE"))