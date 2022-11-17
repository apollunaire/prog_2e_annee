#! C:\Users\tipha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10
from validation1 import *
import sys

if __name__ == '__main__':
    if len(sys.argv)!=3:
        print(usage())
    if sys.argv[1]=="--nb":
        try:
            nb = int(sys.argv[2])
        except ValueError:
            print(usage())
        except IndexError:
            print("pb d'index")
        else:
            print(f"les programmes vont etre executes {nb} fois")
            print("...")
            print(test(nb))
    sys.exit()