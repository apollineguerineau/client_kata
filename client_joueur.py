import os
from typing import List, Optional
from utils.singleton import Singleton
import requests
from client_liste import ClientListe
from business_objects.liste import Liste
from business_objects.joueur import Joueur
from business_objects.partie import Partie
from business_objects.difficultes import Difficultes
from business_objects.proposition_verifiee import PropositionVerifiee
from business_objects.proposition import Proposition

END_POINT="/joueur"

class ClientJoueur(metaclass= Singleton):

    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"


    #ça marche
    def get_pseudo(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())

    #ça marche
    def get_id(self, pseudo) :
        req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
        if type(req.json())==int:
            return(req.json()) 
        else: 
            return(None)

    #ça marche
    def consulter_top10(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/score/")
        return(req.json())
    

    #ça marche
    def get_joueur(self, pseudo):
        id=self.get_id(pseudo)
        if id!=None:
            top_10=self.consulter_top10(id)
            return(Joueur(id, pseudo, top_10))
        else: 
            return(None)

    #ça marche
    def create_joueur(self, pseudo):
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")
        return(req)


    #ça marche
    def get_listes(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/liste")
        nom=req.json()[0]
        contenu=req.json()[1]
        id=req.json()[2]
        listes=[]
        for i in range(len(nom)):
            listes.append(Liste(id[i],contenu[i], nom[i]))
        return(listes)

    #ça marche          
    def create_liste(self, id_joueur, name):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/liste/{name}")

    #ça marche
    def get_partie(self, id_joueur):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id_joueur}/partie_en_cours")
        if req.json()[0]!=None :
            id=req.json()[0]
            proposition=req.json()[2]
            score=req.json()[1][0]
            nom=req.json()[1][1]
            id_joueur=req.json()[1][2]
            mot_obj=req.json()[1][3]
            temps_max=req.json()[1][4]
            nb_tentatives_max=req.json()[1][5]
            indice=req.json()[1][6]
            liste_perso=req.json()[1][7]
            id_liste=req.json()[1][8]
            difficultes=Difficultes(nb_tentatives_max,temps_max,indice, len(mot_obj))
            return(Partie(nom, proposition, liste_perso, id_liste, difficultes, mot_obj))
        else: 
            return(None)



    #ça marche
    def create_partie_en_cours(self, id_joueur, partie):
        payload = {
            "nom_partie" :partie.nom
            ,"mot_objectif" : partie.mot_objectif
            , "temps_max" : partie.difficultes.temps
            , "nb_tentatives_max" : partie.difficultes.nb_tentatives
            , "indice" : partie.difficultes.indice
            , "liste_perso" : partie.est_liste_perso
            , "id_liste" : partie.id_liste
        }
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/partie", json=payload)

    #ça marche
    def ajoute_proposition(self, id_joueur, proposition):
            req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/proposition/{proposition}")

    #ça marche
    def supprime_partie_en_cours(self,id_joueur):
        req=requests.delete(f"{self.__HOST}{END_POINT}/{id_joueur}/partie")

    #ça marche
    def ajoute_score(self, id, score):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/score/{score}")

client=ClientJoueur()


# scores=[75.0, 125.0, 68.0, 27.0, 54.0, 46.0]
# for score in scores: 
#     client.ajoute_score(6, score)

# client.ajoute_score(6, 150.0)

# print(client.consulter_top10(6))

difficultes=Difficultes(6,8,True,6)
partie=Partie("test_partie", ["FOULE", "TRAIN", "FRERE", "CREVE"], True, 5, difficultes, "TREVE")
# print(partie)
# client.create_partie_en_cours(2, partie)
# client.ajoute_proposition(2, "TARIE")
# client.supprime_partie_en_cours(2)
# print(client.get_partie(2))
# partie_cree=client.get_partie(6)
# for mot in partie.liste_mots_proposes :
#     mot_propose=Proposition(mot)
#     proposition=partie.verifie_proposition(mot_propose)
#     print(proposition)

#client.create_joueur("Super_joueur")
# print(client.get_joueur("Super_joueur"))

# client.create_liste(6, "Super_liste")
# print(client.get_listes(2))
# for liste in liste_listes:
#     print(liste)

# liste_listes=client.get_listes(1)
# for liste in liste_listes:
#     print(liste)

# print(client.get_joueur("Linh-Da"))
# print(client.get_joueur("Apolline"))

# partie=client.get_partie(5)
# for mot in partie.liste_mots_proposes :
#     mot_propose=Proposition(mot)
#     proposition=partie.verifie_proposition(mot_propose)
#     print(proposition)



