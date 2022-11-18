"""
importation des modules et classes nécessaires :
- la classe AbstractGenererMot
- la classe ClientList
- le module Random
"""
from business_objects.abstract_generer_mot import AbstractGenererMot
from client_liste import ClientListe
import random

class GenererMotListePerso(AbstractGenererMot):
    """
Cette classe sert à generer aléatoirement un mot à partir d'une liste personnelle du joueur
    """
    def __init__(self, id_liste):
        """
        Args:
            id_liste (int): identifiant de la liste dont on veut generer un mot
        """
        self.id_liste=id_liste


    def generer(self):
        """
        c'est la méthode qui sert à generer un mot à partir de la liste dont on a déjà fixé 
        son identifiant
        """
        clientliste=ClientListe()
        liste=clientliste.get_mot(self.id_liste)[1]
        print(liste)
        num=random.randint(0,len(liste)-1)
        return(liste[num])


# gerenation=GenererMotListePerso(8)
# print(gerenation.generer())

            