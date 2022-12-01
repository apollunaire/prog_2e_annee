import socket

host = "localhost" # "", "127.0.0.1
port = 10000
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