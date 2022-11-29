import socket


def socket_serveur_asynchrone():
    try:
        message = ""
        while message.lower() != "exit":
            #udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en UDP
            #tcpSvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creation socket en TCP
            server_socket = socket.socket()  #creation de la socket
            host = "localhost"
            #port = socket.gethostname() #adresse IP ?
            port = 10001
            server_socket.bind((host, port))  #association du host et du port
            server_socket.listen(1)  #attente de la connexion / ici pas de connexions simultanees
            #print(server_socket.listen(1))
            conn, address = server_socket.accept()  #connexion
            print(f"SERVEUR")
            message = conn.recv(1024).decode()  #reception data
            message.lower()
            print(message)  #affichage de data
            #reply = input("message à envoyer : ")  # entree de la reponse
            while (message != "bye") and (message != "exit"):
                reply = input("message à envoyer : ")  # entree de la reponse
                conn.send(reply.encode())  # envoi de la reponse

                data = conn.recv(1024).decode()  # reception data
                data.lower()
                print(data)  # affichage de data

            """if message == "exit":
                conn.connect_ex((host, port))"""
            """if message == "exit":
                break"""
        conn.close() #fermeture connexion
    except (TimeoutError, ConnectionRefusedError, socket.gaierror, ConnectionResetError, BrokenPipeError) as err:
        print(f"ERREUR - {err}")
        return -1
        #server_socket.connect_ex("") #à tester ? // fermeture connexion hote specifie ?
        #conn.connect_ex(address) #à tester ? // fermeture de la connexion avec l'hote specifie ?



(socket_serveur_asynchrone())