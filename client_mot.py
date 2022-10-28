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

    def add_mot_to_liste(self, mot : str, nom_liste : str, id_joueur : int) :
        """Renvoie si le mot a bien été ajouté à la liste. S'il n'a pas été ajouté, cela veut dire 
           que le mot était déjà dans la liste"""

        #On vérifie si le mot est déjà dans la base de données
        from client_mot import ClientMot
        clientmot = ClientMot()

        if clientmot.get_id_by_mot(mot) == None :
            clientmot.create_mot(mot)
        id_mot = clientmot.get_id_by_mot(mot)

        #On vérifie si le mot est déjà dans la liste

        #id_joueur = (Session().joueur.id_joueur)
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        from business_objects.liste import Liste
        listes = clientjoueur.get_listes(id_joueur)
        for liste in listes :
            if liste.nom == nom_liste :
                liste_d_ajout = liste
        if mot in liste_d_ajout :
            print(f"Le mot {mot} est déjà dans la liste")
            return False
        else :
            from client_liste import ClientListe
            clientliste = ClientListe()
            clientliste.ajouter_mot(liste_d_ajout.id_liste, id_mot)
            return True

mot_client=ClientMot()
# print(mot_client.create_mot("FENETRE"))
print(mot_client.get_id_by_mot("FENETRE"))
print(mot_client.add_mot_to_liste("FENETRE", "nouvelle liste", 5))