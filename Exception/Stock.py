from Article import Article
import csv

class Stock():
    def __init__(self, dic:dict = {}):
        self.__dic = dic

    def __str__(self):
        return f"Article : {[[k for k in p] for p in self.__dic]}" # A MODIFIER !!!

    def taille(self) -> int:
        return len(self.__dic.values())

    def ajout(self, article:Article):
        try:
            self.__dic.__setitem__(article.code_bare, (article.nom, article.prix_HT))
            print(f"l'ajout de l'article {article} a bien été fait")
        except:
            for k in self.__dic.keys():
                if article.code_bare==k:
                    raise KeyError('un article possède déjà le même code barre')

    def recherche_cb(self, code_barre:int):
        try:
            print(self.__dic.get(code_barre))
        except KeyError:
            print("l'article n'est pas en stock")
            return -1

    def recherche_nom(self, nom:str):
        try:
            for cle, val in self.__dic.items():
                if val == nom:
                    return self.__dic.get(cle)
        except:
            print("l'article n'est pas en stock")
            return -1

    def supprime_cb(self, code_barre:int):
        try:
            self.__dic.__delattr__(self.__dic.get(code_barre))
        except KeyError:
            print("l'article n'est pas en stock")
            return -1

    def supprime_nom(self, nom:str):
        try:
            for cle, val in self.__dic.items():
                if val == nom:
                    self.__dic.__delattr__(self.__dic.get(cle))
                    return 0
        except:
            print("l'article n'est pas en stock")
            return -1

    def import_csv(self, file:str):
        with open('Example.csv', 'rb', newline='') as csvfile:
            return 0

    def export_csv(self, file:str):
        try:
            with open(file, 'wb', newline='') as csvfile:
                for k in self.__dic.keys():
                    art = self.__dic.get(k)
                    my_writer = csv.writer(csvfile, delimiter=' ')
                    my_writer.writerow(k)
        except FileExistsError:
            print("un fichier au même nom existe déjà")