import sys

from Article import Article
from Stock import Stock

if __name__=='__main__':
    a = Article(nom="art1", code_barre=11111111111, prix_HT=2)
    b = Article("test", 22, 12.2)
    c = Article()
    stock1 = Stock()
    stock1.ajout(a)
    stock1.ajout(b)
    stock1.ajout(c)
    print(stock1)
    sys.exit()