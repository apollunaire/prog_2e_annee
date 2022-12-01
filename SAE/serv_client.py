import socket
import multiprocessing
from time import *
import csv



def socket_serv_client(host:str="localhost", port:int = 10000):
    etat = ""
    while etat != "kill":

        print(f"Ouverture de la socket sur le serveur {host} port {port}")
        client_socket = socket.socket()
        client_socket.connect((host, port))
        print("Serveur est connecté")

        while etat != "kill" and etat != "reset":
            while etat != "kill" and etat != "reset" and etat != "disc":

                etat = input("Message au serveur : ")
                client_socket.send(etat.encode())
                print("Message envoyé")

                etat = client_socket.recv(1024).decode()
                print(f"Message du serveur : {etat}")

        # Fermeture de la socket du client
        client_socket.close()
        print("Socket fermée")


def threading(file:str):
    serveurs = []
    thread = {}
    a=0
    try:
        with open(f"{file}", newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                serveurs.append(row)
                #print(serveurs)
                #print(row)
        for k in serveurs:
            print(k)
            [a] = multiprocessing.Process(target=socket_serv_client(k[0], int(k[1])))
            a.start()
            a+=1

        print(thread)
        return 0
    except (FileExistsError, FileNotFoundError, socket.gaierror) as err:
        print(err)
        return -1
    except socket.gaierror as err:
        print("socket.gaierror" + str(err))



"""p1 = multiprocessing.Process(target=socket_serv_client())
    p2 = multiprocessing.Process(target=socket_serv_client())
    p1.start()
    p2.start()
    end = time.perf_counter()"""



print(threading("test/test.csv"))