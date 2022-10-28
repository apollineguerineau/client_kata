from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self, pseudo, partie = None, liste = None):
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