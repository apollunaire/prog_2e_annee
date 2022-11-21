

class Article():
    TVA = 20
    def __init__(self, nom: str = 'sans nom', code_barre: int = 11111111, prix_HT: float = 0.0):
        self.__nom = nom
        self.__code_bare = code_barre
        self.__prix_HT = prix_HT

    def __str__(self):
        return f"{self.nom}, {self.code_bare}, {self.prix_HT}€ (HT)"

    @property
    def nom(self):
        return self.__nom

    @property
    def code_bare(self):
        return self.__code_bare

    @property
    def prix_HT(self):
        return self.__prix_HT

    """@nom.setter
    def nom(self, nom: str):
        self.nom = nom"""

    """@code_bare.setter
    def code_bare(self, cb:int(8)):
        self.code_bare = cb"""

    @prix_HT.setter
    def prix_HT(self, prix: float):
        self.prix_HT = prix

    def prixTTC(self):
        if self.prix_HT<=0:
            raise (ZeroDivisionError)
        else:
            return self.prix_HT*(Article.TVA/100)


