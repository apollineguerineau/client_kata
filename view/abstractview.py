"""classe abstraite pour les vues
"""

from abc import ABC, abstractmethod
import re
from InquirerPy import inquirer
class AbstractView(ABC):
    """classe abstraite pour les vues en console
    """
    #pylint: disable=unnecessary-pass
    @abstractmethod
    def display_info(self):
        """méthode abstraite pour afficher uniquement de l'information en console
        """
        pass

    @abstractmethod
    def make_choice(self):
        """méthode abstraite pour afficher un choix à faire par l'utilisateur en console
        """
        pass
