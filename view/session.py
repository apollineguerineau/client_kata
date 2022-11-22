from utils.singleton import Singleton

from business_objects.joueur import Joueur
from business_objects.liste import Liste

#pylint: disable=import-outside-toplevel
#justification: permet d'éviter les imports circulaires (TP du prof et crash test)
class Session(metaclass=Singleton):
    """permet de

    Parameters
    ----------
    metaclass : Singleton
        permet de s'assurer qu'il n'existe qu'une seule instance de Session
    """
    def __init__(self, joueur: Joueur,
                 partie = None, liste:Liste = None):
        """
        Définition des variables que l'on stocke en session

        Attributes
        ----------

        joueur : Joueur
            Joueur connecté

        partie : Partie
            Partie en cours du joueur connecté
            Si le joueur n'a pas de partie en cours, partie vaut None

        liste : str
        Nom de la liste en cours d'utilisation
        """
        self.joueur = joueur
        self.liste = liste
        self.partie = partie