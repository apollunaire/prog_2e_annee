import sys
from exercice1 import divEntier
from exercice2 import ouverture

def main():
    """try:
        x = float(input("x = "))
        y = float(input("y = "))
    except ValueError:
        print("x et y doivent être des entiers")
        return -1
    else:
        try:
            print(divEntier(x, y))
        except ValueError:
            print("Erreur de valeur dans diventier")
            return -2"""
    try:
        file = input("nom du fichier à ouvrir : ")
        print(ouverture(file))
    except (FileNotFoundError):
        print("erreur dans la fonction ouverture")
        return -1
    return 0


if __name__ == '__main__':
    sys.exit(main())
