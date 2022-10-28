from business_objects.abstract_generer_mot import AbstractGenererMot
from client_liste import ClientListe
import random

class GenererMotListePerso(AbstractGenererMot):
    def __init__(self, id_liste):
        self.id_liste=id_liste


    def generer(self):
        clientliste=ClientListe()
        liste=clientliste.get_mot(self.id_liste)[1]
        print(liste)
        num=random.randint(0,len(liste)-1)
        return(liste[num])


# gerenation=GenererMotListePerso(2)
# print(gerenation.generer())

            