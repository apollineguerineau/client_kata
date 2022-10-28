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



    def get_pseudo(self, id:int) :
        req = requests.get(f"{self.__HOST}{END_POINT}/{id}")
        return(req.json())


    # def get_id(self, pseudo) :
    #     req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
    #     if type(req.json())==int:
    #         return(req.json()) 
    #     else: 
    #         return(None)

    def get_id(self, pseudo) :
        req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
        print(req.json())
        if type(req.json())==int:
            return(req.json()) 
        else: 
            print(None)

    def consulter_top10(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/score/")
        return(req.json())
    
    def get_joueur(self, pseudo):
        id=self.get_id(pseudo)
        top_10=self.consulter_top10(id)
        return(Joueur(id, pseudo, top_10))


    def create_joueur(self, pseudo):
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")
        return(req)

    def get_listes(self, id):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id}/liste")
        # return(req.json())
        nom=req.json()[0]
        contenu=req.json()[1]
        id=req.json()[2]
        listes=[]
        for i in range(len(nom)):
            listes.append(Liste(id[i],contenu[i], nom[i]))
        return(listes)

                
    def create_liste(self, id_joueur, name):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/liste/{name}")


    def get_partie(self, id_joueur):
        req=requests.get(f"{self.__HOST}{END_POINT}/{id_joueur}/partie")
        id=req.json()[0]
        proposition=req.json()[2]
        score=req.json()[1][0]
        nom=req.json()[1][1]
        id_joueur=req.json()[1][2]
        mot_obj=req.json()[1][3]
        temps_max=req.json()[1][4]
        langue=req.json()[1][5]
        nb_tentatives_max=req.json()[1][6]
        indice=req.json()[1][7]
        liste_perso=req.json()[1][8]
        id_liste=req.json()[1][9]
        difficultes=Difficultes(nb_tentatives_max,temps_max,indice, len(mot_obj))
        return(Partie(nom, id, proposition, liste_perso, id_liste, difficultes, mot_obj))


    #celle-ci marche pas
    def ajoute_score(self, id, score):
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/score/{score}")

client=ClientJoueur()
# print(client.get_pseudo(5))
print(client.get_id("Mathis"))
# print(client.get_id("erjk"))
# print(client.create_joueur(('essai2')))
# print(client.get_listes(5))
# for liste in client.get_listes(5):
#     print(liste)
# client.create_liste(5, "super_liste")
# print(client.consulter_top10(5))
# client.ajoute_score(5, 3000.0)
# print(client.consulter_meilleur_score(5))
# print(client.get_joueur("Apolline"))


partie=client.get_partie(1)
for proposition in partie.liste_mots_proposes:
    prop=partie.verifie_proposition(Proposition(proposition))
    print(prop)
    print("")
