import sys
#from exercice1 import divEntier

"""def main():
    try:
        x = int(input("x = "))
        y = int(input("y = "))
    except ValueError:
        return "x et y doivent être des entiers"
    else:
        print(divEntier(x, y))
    return 0"""

def divEntier(x: int, y: int) -> int:
    """if y < 0 or x < 0:
        raise ValueError("nombre")
    if y == 0:
        raise ValueError("nul")"""
    try:
        if x < y:
            return 0
        else:
            x = x - y
    except (ValueError, RecursionError):
        if y < 0 or x < 0:
            print("nombre négatif")
        if y == 0:
            print("y ne peut pas être nul")
    else:
        return divEntier(x, y) + 1

if __name__ == '__main__':
    try:
        x = int(input("x = "))
        y = int(input("y = "))
    except ValueError:
        print("x et y doivent être des entiers")
    else:
        print(divEntier(x, y))
    sys.exit()
