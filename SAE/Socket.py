import socket


class Socket:
    def __init__(self, port:int = 10001, host:str = "localhost"):
        self.__port = port
        self.__host = host

    def connexion_client(self, port:int = 10001, host:str = "localhost"):
        client_socket = socket.socket()
        client_socket.connect((host, port))
        return 0

    def connexion_serveur(self, port:int = 10001, host:str = "localhost"):
        server_socket = socket.socket()
        server_socket.bind((host, port))  # association du host et du port
        server_socket.listen()
        #conn, address = server_socket.accept()  #connexion
        return 0

    def reception_serveur(self, server_socket):
        conn, address = server_socket.accept()  # connexion
        data = conn.recv(1024).decode()  # reception data
        print(data)

    def reception_client(self):

        return 0

    def envoi_serveur(self, conn):
        reply = input("message à envoyer : ")  # entree de la reponse
        conn.send(reply.encode())  # envoi de la reponse
        return 0

    def envoi_client(self):
        return 0