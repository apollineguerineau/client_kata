import os
from typing import List, Optional
from utils.singleton import Singleton
import requests
import re #import regex

END_POINT="/mot"

class ClientMot(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"

    def create_mot(self, mot: str) :
        '''Ajouter un mot dans la bdd

        Parameters
        mot : str
        '''
        req = requests.post(f"{self.__HOST}{END_POINT}/contenu/{mot}")


    def add_mot_to_liste(self, mot : str, nom_liste : str, id_joueur : int) :
        """Ajoute un mot à une liste personelle d'un joueur

        Parameters : 
        mot : str
        nom_liste : str
        id_joueur : int
        
        Returns
        Renvoie True si le mot a bien été ajouté à la liste. S'il n'a pas été ajouté, cela veut dire 
        que le mot était déjà dans la liste où qu'il ne respectait pas les conditions"""

        #On vérifie si le mot est déjà dans la base de données
        regex = "^[A-zÀ-ú]+$"
        resultat = re.match(regex, mot)
        if resultat==None:
            print(f"Le mot {mot} ne respecte pas les conditions: uniquement des lettres avec ou sans accents, pas de chiffres, pas de caractères spéciaux ")
            return(False)
        if len(mot)>50:
            print(f"Le mot {mot} est trop long ")
            return(False)
        from client_mot import ClientMot
        clientmot = ClientMot()

        if clientmot.get_id(mot) == None :
            clientmot.create_mot(mot)
        id_mot = clientmot.get_id(mot)

        #On vérifie si le mot est déjà dans la liste

        #id_joueur = (Session().joueur.id_joueur)
        from client_joueur import ClientJoueur
        clientjoueur = ClientJoueur()
        from business_objects.liste import Liste
        listes = clientjoueur.get_listes(id_joueur)
        for liste in listes :
            if liste.nom == nom_liste :
                liste_d_ajout = liste

        if mot in liste_d_ajout.liste :
            print(f"Le mot {mot} est déjà dans la liste")
            return False
        else :
            from client_liste import ClientListe
            clientliste = ClientListe()
            clientliste.ajouter_mot(liste_d_ajout.id_liste, id_mot)
            return True



    def get_id(self, mot) :
        '''Retourne l'id du mot (s'il existe dans la bdd)

        Parameters : 
        mot : str

        Returns : 
        L'id du mot ou None
        '''
        req = requests.get(f"{self.__HOST}{END_POINT}/mot/{mot}")
        if type(req.json())==int :
            return(req.json())
        else : 
            return(None) 
        
