import socket

def socket_client():
    try :
        client_socket = socket.socket() #creation de la socket
        hostname = socket.gethostname() #recuperation du hostname
        print(hostname) #affichage hostname
        host="localhost"
        port = 10001
        client_socket.connect((host, port)) #connexion host par le port (si localhost, host="")
        print("CLIENT")
        message = input("message a envoyer : ")  # entree du message a envoyer
        message.lower()
        while (message!="bye") and (message!="exit"):
            client_socket.send(message.encode())  # envoi du message
            data = client_socket.recv(1024).decode()  # reception de donnees
            print(data)  # affichage des donnees recues
            message = input("message2 a envoyer : ")  # entree du message a envoyer

        client_socket.send(message.encode()) #envoi du message
        client_socket.close() #fermeture de la connexion / du port
    except (TimeoutError, ConnectionRefusedError, socket.gaierror, ConnectionResetError, BrokenPipeError) as err:
        print(f"ERREUR - {err}")
        return -1


(socket_client())