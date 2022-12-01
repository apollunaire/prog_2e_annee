import socket

host = "localhost" # "", "127.0.0.1
port = 10000
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