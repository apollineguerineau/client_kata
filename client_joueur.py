"""couche service: gère les requetes des objets Joueurs vers l'API
"""
import requests

from utils.singleton import Singleton

from client_liste import ClientListe

from business_objects.liste import Liste
from business_objects.joueur import Joueur
from business_objects.partie import Partie
from business_objects.difficultes import Difficultes
from business_objects.proposition_verifiee import PropositionVerifiee
from business_objects.proposition import Proposition

END_POINT="/joueur"

#pylint: disable=invalid-name
#justification: le __HOST pourrait reservir pour un déploiement
#pylint: disable=unused-variable
#justification: le "req =" est nécessaire pour lancer une requete
class ClientJoueur(metaclass= Singleton):
    """gère
    """
    def __init__(self) -> None:
        self.__HOST ="http://127.0.0.1:80"



    def get_pseudo(self, identifiant_joueur:int) :
        '''Retourne le pseudo du joueur selon son identifiant

        Parameters:
        identifiant_joueur: int
            l'identifiant du joueur

        Returns:
            str: le pseudo du joueur'''
        req = requests.get(f"{self.__HOST}{END_POINT}/{identifiant_joueur}")
        return req.json()


    def get_id(self, pseudo) :
        '''Retourne l'identifiant du joueur selon son pseudo

        Parameters: le pseudo du joueur : str

        Returns:
            int : l'identifiant du joueur
            None si le pseudo n'est pas dans la base de données'''
        req = requests.get(f"{self.__HOST}{END_POINT}/pseudo/{pseudo}")
        if isinstance(req.json(), int):
            return req.json()
        return None


    def consulter_top10(self, identifiant_joueur):
        '''Retourne le top 10 du joueur

        Parameters: l'identifiant du joueur : int

        Returns:
            list : le top 10 du joueur'''
        req=requests.get(f"{self.__HOST}{END_POINT}/{identifiant_joueur}/score/")
        return(req.json())


    def get_joueur(self, pseudo):
        '''Retourne un joueur

        Parameters: le pseudo du joueur : str

        Returns:
            Joueur : le joueur'''
        identifiant_joueur = self.get_id(pseudo)
        if identifiant_joueur is not None:
            top_10=self.consulter_top10(identifiant_joueur)
            return(Joueur(identifiant_joueur, pseudo, top_10))
        return None


    def create_joueur(self, pseudo):
        '''Crée un joueur dans la base de données
        '''
        req=requests.post(f"{self.__HOST}{END_POINT}/{pseudo}")
        return(req)


    def get_listes(self, id_joueur):
        '''Retourne les listes personnelles du joueur (si il en a)

        Parameters:
        id_joueur : int
            l'identifiant du joueur

        Returns:
            list(Liste) : la liste des listes personnelles
            None si le joueur n'a pas de liste'''
        req=requests.get(f"{self.__HOST}{END_POINT}/{id_joueur}/liste")
        nom=req.json()[0]
        contenu=req.json()[1]
        id_liste=req.json()[2]
        listes=[]
        #pylint: disable=consider-using-enumerate
        #justification: enumerate ne renvoie pas le même type
        for i in range(len(nom)):
            listes.append(Liste(id_liste[i],contenu[i], nom[i]))

        if not listes: #listes==[]
            return None
        return(listes)



    def create_liste(self, id_joueur, name):
        '''Crée une liste personnelles dans la base de données

        Parameters : l'identifiant du joueur : int et le nom de la liste crée : str
        '''
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/liste/{name}")


    def get_partie(self, id_joueur):
        '''Retourne la partie en cours du joueur (si elle existe)

        Parameters: l'identifiant du joueur : int

        Returns:
            Partie : la partie en cours
            None si le joueur n'a pas de partie en cours'''
        req=requests.get(f"{self.__HOST}{END_POINT}/{id_joueur}/partie_en_cours")
        if req.json()[0]!=None :
            id=req.json()[0]
            proposition=req.json()[2]
            id_joueur=req.json()[1][0]
            mot_obj=req.json()[1][1]
            nb_tentatives_max=req.json()[1][2]
            indice=req.json()[1][3]
            liste_perso=req.json()[1][4]
            temps_max=req.json()[1][5]
            difficultes=Difficultes(nb_tentatives_max,temps_max,indice, len(mot_obj))
            return(Partie( proposition, liste_perso, difficultes, mot_obj,0))
        else:
            return None



    def create_partie_en_cours(self, id_joueur, partie):
        '''Crée une partie en cours du joueur

        Parameters : l'identifiant du joueur et la partie : Partie
        '''
        payload = {
            "mot_objectif" : partie.mot_objectif
            , "nb_tentatives_max" : partie.difficultes.nb_tentatives
            , "indice" : partie.difficultes.indice
            , "liste_perso" : partie.est_liste_perso
            , "temps_max" : partie.difficultes.temps
        }
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/partie", json=payload)


    def ajoute_proposition(self, id_joueur, proposition):
        '''Ajoute une proposition à une partie

        Parameters: l'identifiant du joueur : int, proposition : str'''
        req=requests.post(f"{self.__HOST}{END_POINT}/{id_joueur}/proposition/{proposition}")


    def supprime_partie_en_cours(self,id_joueur):
        '''Supprime la partie en cours du joueur

        Parameters: l'identifiant du joueur : int'''
        req=requests.delete(f"{self.__HOST}{END_POINT}/{id_joueur}/partie")


    def ajoute_score(self, id, score):
        '''Ajoute un score au joueur

        Parameters: l'identifiant du joueur : int, score : float'''
        req=requests.post(f"{self.__HOST}{END_POINT}/{id}/score/{score}")
