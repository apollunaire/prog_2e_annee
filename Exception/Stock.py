
class Stock():
    def __init__(self, dic:dict = dict):
        self.__dic = dic

    def taille(self) -> int:
        return self.__dic.__len__()

