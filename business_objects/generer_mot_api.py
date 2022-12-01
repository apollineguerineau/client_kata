"""permet de générer les mot à partir de l'API herokuapp.com
"""
import requests
from business_objects.abstract_generer_mot import AbstractGenererMot
from business_objects.proposition import Proposition


class GenererMotApi(AbstractGenererMot):
    # pylint: disable=too-few-public-methods
    """ C'est la classe abstraite GenererMotApi qui sert à generer aléatoirement
    un mot en fixant le nombre de lettres de ce mot
    """
    def __init__(self, nb_lettres):

        """
        Args:
            nb_lettres (int): le nombre de lettres du mot qu'on cherche à generer
        """
        #pylint: disable=super-init-not-called
        self.nb_lettres=nb_lettres

    def generer(self):
        """la méthode <generer> sert à generer aléatoirement un mot à partir de <Random Word API>
        et qui a comme longueur le nombre de lettres déjà choisi
        """
        #req=requests.get("https://api.api-ninjas.com/v1/randomword", headers={'X-Api-Key': 'qMQWg2l0mek+z1MW2iI5GA==u4SLxJOSyy1GP5Ht'})
        req=requests.get("https://random-words-api.vercel.app/word")
        if req.status_code==200:
            res=req.json()[0]['word']
            mot=Proposition(res).mot
            return(mot)
        else :
            return (None)


#    def generer(self):
#        res=self.trouve_mot()
#        if res==None:
#            return("problème")
#        while(len(res))!=self.nb_lettres:
#            res=self.trouve_mot()
#        return(res)




