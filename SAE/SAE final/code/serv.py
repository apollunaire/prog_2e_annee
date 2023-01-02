import socket
import os

def serveur():
    message = ""
    conn = None
    server_socket = None
    while message != "kill":
        message = ""
        server_socket = socket.socket()
        server_socket.bind(("0.0.0.0", 15001))
        #0.0.0.0 permet d'écouter toutes les @IP de la machine
        server_socket.listen(1)
        print('En attente de connexion')
        while message != "kill" and message != "reset":
            message = ""
            try :
                conn, addr = server_socket.accept() #établissement de la connexion
                print (addr)
            except ConnectionError:
                print ("Erreur de connexion")
                break
            else :
                while message != "kill" and message != "reset" and message != "disconnect":
                    message = conn.recv(1024).decode()
                    if message != "kill" and message != "reset" and message != "disconnect":                         # print ("Received from client: ", message)
                        rep = os.popen(message) #envoi de la commande sur le client connecté
                        output = rep.read() #reception de la sortie de celle-ci
                        message = output
                    conn.sendall(message.encode())
                conn.close() #fermeture de la connexion
        print ("Connection closed")
        server_socket.close() #fermeture du serveur
        print ("Server closed")


if __name__ == '__main__':
    serveur()