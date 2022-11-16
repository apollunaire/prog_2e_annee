
def ouverture(file):
    f = open(file, 'r')
    try:
        with f as txtfile:
            line = txtfile.readline()
            print(line)
        txtfile.close()
    except FileNotFoundError:
        print("le fichier est introuvable")
    except IOError:
        print("IOError")
    else:
        return "oof"

print(ouverture("main.py"))