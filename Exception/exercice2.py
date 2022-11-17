
def ouverture(file):
    try:
        f = open(file, 'r')
        with f as txtfile:
            line = txtfile.readline()
            print(line)
        txtfile.close()
    except FileNotFoundError:
        print("le fichier est introuvable")
    except IOError:
        print("IOError")
    else:
        return 0

