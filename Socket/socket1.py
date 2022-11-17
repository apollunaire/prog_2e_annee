import socket

def socket_client():
    client_socket = socket.socket() #creation de la socket
    host = socket.gethostname() #recuperation du hostname
    print(host) #affichage hostname
    client_socket.connect(("", 1000)) #connexion host par le port (si localhost, host="")
    message = input("message a envoyer : ") #entree du message a envoyer
    client_socket.send(message.encode()) #envoi du message
    data = client_socket.recv(1024).decode() #reception de donnees
    print(data) #affichage des donnees recues
    client_socket.close() #fermeture de la connexion / du port


def socket_serveur():
    #udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creation socket en UDP
    #tcpSvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creation socket en TCP
    server_socket = socket.socket()  #creation de la socket
    server_socket.bind(("", 1001))  #association du host et du port
    server_socket.listen(1)  #attente de la connexion / ici pas de connexions simultanees
    conn, address = server_socket.accept()  #connexion
    data = conn.recv(1024).decode()  #reception data
    print(data)  #affichage de data
    if data == 'bye':
        conn.close() #fermeture de la connexion
    if data == 'arret':
        conn.close() #fermeture connexion
    else :
        reply = input("message à envoyer : ")  #entree de la reponse
        conn.send(reply.encode())  #envoi de la reponse
    #server_socket.connect_ex("") #à tester ? // fermeture connexion hote specifie ?
    #conn.connect_ex(address) #à tester ? // fermeture de la connexion avec l'hote specifie ?
