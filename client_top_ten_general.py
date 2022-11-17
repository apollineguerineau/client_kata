import os
from typing import List, Optional
from utils.singleton import Singleton
import requests

END_POINT="/top10"

class ClientTopTen(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def consulter_top_ten_general(self):
        req = requests.get(f"{self.__HOST}{END_POINT}")
        return(req.json())



# client_top10=ClientTopTen()
# print(client_top10.consulter_top_ten_general())

