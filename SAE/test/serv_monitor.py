import socket, multiprocessing
from client_thread import Serveur
import csv
import socket


def socket_serv_monitoring(host:str="localhost", port:int=10000):
    etat = ""
    while etat !="kill":

        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)

        while etat != "kill" and etat != "reset":

            print('En attente du client')
            conn, address = server_socket.accept()
            print(f'Client connecté {address}')

            while etat != "kill" and etat != "reset" and etat != "disc":

                # Réception du message du client
                etat = conn.recv(1024) # message en by
                message = etat.decode()
                print(f"Message du client : {message}")

                # J'envoie un message
                etat = input("Saisir un message : ")
                conn.send(etat.encode())
                print(f"Message {etat} envoyé")

            # Fermeture
            conn.close()
            print("Fermeture de la socket client")
        server_socket.close()
        print("Fermeture de la socket serveur")

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
            [a] = Serveur("localhost", 10000)
            a.start()
            a.join()
            a+=1
        print(thread)
        return 0
    except (FileExistsError, FileNotFoundError, socket.gaierror) as err:
        print(err)
        return -1
    except socket.gaierror as err:
        print("socket.gaierror" + str(err))



#socket_serv_monitoring()