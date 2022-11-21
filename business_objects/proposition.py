"""gère les propositions
"""
import requests
class Proposition :
    '''Classe implémentant une proposition de mot (faite par le joueur)

    attributes
    ---------
    mot : str
    Examples
    --------
    >>> proposition=Proposition("éèâàçîïôùê")
    >>> print(proposition)
    EEAACIIOUE
    '''
    def __init__(self, mot):
        self.mot=mot
        self.transforme_proposition()

    def est_autorise(self):
        '''Vérifie si la proposition existe dans le dictionnaire
        par l'intermédiaire de l'API dictionaryapi
        return : bool
        True si le mot existe
        False sinon

        Examples
        --------
        >>> import requests
        >>> proposition=Proposition("horse")
        >>> proposition.est_autorise()
        True
        >>> proposition=Proposition("zhtwxr")
        >>> proposition.est_autorise()
        False
        '''
        req=requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.mot}')
        res=req.json()
        if isinstance(res, dict):
            return False
        return True


    def majuscule(self):
        '''Remplace les minuscules en majuscules d'une chaîne de caractères

        parameters : str

        return : str
        La chaîne en majuscule
        '''
        chaine=''
        if self.mot is None:
            return None
        for caractere in self.mot:
            chaine +=caractere.upper()
        return chaine


    def supprime_accent(self):
        '''Supprime les accents d'une chaîne de caracteres

        parameters : str

        return : str
        La chaîne sans les accents

        Examples
        --------

        '''
        chaine=""
        # traitement du cas NULL
        if self.mot is None:
            return None
        #création d'une copie du mot
        copie=''
        # mise en minuscules
        for caractere in self.mot:
            copie+=caractere.lower()
        # dictionnaire qui référence les accents
        dictionnaire_accents = {
                    "é": "e",
                    "è": "e",
                    "à": "a",
                    "ù": "u",
                    "î": "i",
                    "ï": "i",
                    "ç": "c",
                    "â": "a",
                    "ô": "o",
                    "ê": "e",
                }
        # remplacement des accents
        for caractere in copie:
            # pylint: disable=consider-iterating-dictionary
            if caractere in dictionnaire_accents.keys():
                chaine += dictionnaire_accents.get(caractere)
            else:
                chaine +=caractere
        return chaine

    def transforme_proposition(self):
        '''Met en majuscule et enlève les accents de la proposition
        '''
        self.mot=self.supprime_accent()
        self.mot=self.majuscule()

    def __str__(self):
        '''affiche la proposition
        '''
        return self.mot

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
