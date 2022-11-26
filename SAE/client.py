# -*-coding: utf8-*

from threading import Thread
import platform as p
import socket
import time
import sys
import re
import os


def client():
    os.system("color 0f")

    id_co_individuel = 0
    msg_a_envoyer = ""
    ligne_a_ajouter = ""
    msg_a_encoder = ""


    def async_recv(client_socket):
        while 1:
            msg_recu = client_socket.recv(1024)
            if msg_recu == b"":
                client_socket.close()
                print("Le serveur est arrêté.\n")
                break
            if msg_recu != msg_a_encoder:
                msg_recu = msg_recu.decode()
                if re.search(r'^id_', msg_recu) is None:
                    print("\n>>>{0}".format(msg_recu))
                else:
                    id_co_individuel = int(re.sub(r'(id_)', r'', msg_recu))
            elif msg_a_encoder == msg_recu:
                msg_recu = msg_recu.decode()
                print("\n>>>Envoyé : {0}".format(msg_recu))


    def envoie(msg_a_envoyer):
        msg_a_encoder = str(msg_a_envoyer)
        msg_a_encoder = msg_a_envoyer.encode()
        print("Envoie du message  . . . \1")
        connexion_avec_serveur.send(msg_a_encoder)
        msg_a_encoder = ""
        msg_a_envoyer = ""
        # on envoie le message
        print("Attente de la réponse . . .")


    print(" " * 20 + "****** Client Elranet, bienvenue. ******\n\n\n" + " " * 20)
    #hote = input(" " * 21 + "Entrez le nom de l'hôte > ")
    #port = int(input(" " * 21 + "Entrez le port (50000 par défault) > "))
    print("\n")
    print("_" * 80 + "|/-\\" * (81 // 4) + "|   " * (81 // 4))

    afficher = lambda cle, valeur: print("{k} :: {v}".format(k=cle, v=valeur))
    systeme = p.system()
    python = p.python_version()
    jeu, formatFichier = p.architecture()
    distribution = p.version()
    afficher("Système      Opérant    ", systeme)
    afficher("Architecture Processeur ", jeu)
    afficher("Version      Système    ", distribution)
    afficher("Version      Python     ", python)
    hote = "localhost"
    port = 50004

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))

    envoie(systeme)
    envoie(jeu)
    envoie(distribution)
    envoie(python)

    # faire la réception du socket dans un autre thread
    thread = Thread(target=async_recv, args=(connexion_avec_serveur,))
    thread.start()

    print("Connexion établie avec le serveur sur le port {}.".format(port))

    while msg_a_envoyer.lower() != "fin":
        try:
            # partie du code où on va écrire un message pour le client
            while 1:
                ligne_a_ajouter = input("> ")
                if ligne_a_ajouter == "send":  # la commande 'fin' demande l'arrêt du serveur
                    break
                elif ligne_a_ajouter.lower() == "fin":
                    # on arrete tout :
                    break
                elif ligne_a_ajouter == "ren":
                    msg_a_envoyer += "\n"
                    msg_a_envoyer += ligne_a_ajouter
                    envoie(msg_a_envoyer)
                elif ligne_a_ajouter == "id":
                    msg_a_envoyer += "\n"
                    msg_a_envoyer += ligne_a_ajouter
                    envoie(msg_a_envoyer)
                else:
                    msg_a_envoyer += "\n"
                    msg_a_envoyer += ligne_a_ajouter

            if msg_a_envoyer != "" and ligne_a_ajouter.lower() != "fin" and ligne_a_ajouter != "ren":
                # on envoie
                envoie(msg_a_envoyer)
            # --------------------------------------------------------
            elif ligne_a_ajouter.lower() == "fin":
                msg_a_envoyer = "fin"
                msg_a_encoder = msg_a_envoyer.encode()
                connexion_avec_serveur.send(msg_a_encoder)
                break
            # --------------------------------------------------------
        except NameError as nom_erreur:
            print(nom_erreur)

        except TypeError as type_err:
            print(type_err)

        except EnvironmentError as env_err:
            print(env_err)

    thread.stop()
    print("Fermeture de la connexion. Appuyer sur une touche pour continuer . . .")
    wait = input()
    connexion_avec_serveur.close()

client()