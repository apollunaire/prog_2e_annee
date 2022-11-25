# -*-coding: utf8-*

import platform as p
import socket
import select
import re
import os

def serveur():

    os.system("color 0f")
    print(" " * 21 + "***** Serveur Elranet, bienvenue. *****\n\n\n" + " " * 21)
    try:
        hote = socket.gethostbyname(socket.gethostname())
    except NameError as nom_err:
        print(nom_err)
    except TypeError as type_err:
        print(type_err)

    port = int(input(" " * 21 + "Entrez le port (50000 par défault) > "))
    print("\n")
    print("_" * 80 + "|/-\\" * (81 // 4) + "|   " * (81 // 4))

    if port != 50000 and port is None:
        port = 50000

    port = int(port)
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    # keepalive : option pour savoir qui est en ligne
    print("Le serveur écoute à présent sur le port {0} depuis {1}.\n".format(port, hote))
    afficher = lambda cle, valeur: print("{k} :: {v}".format(k=cle, v=valeur))
    systeme = p.system()
    python = p.python_version()
    jeu, formatFichier = p.architecture()
    distribution = p.version()
    afficher("Système      Opérant    ", systeme)
    afficher("Architecture Processeur ", jeu)
    afficher("Version      Système    ", distribution)
    afficher("Version      Python     ", python)

    print("")

    serveur_lance = True
    clients_connectes = []
    ok_a_encoder = ""

    try:
        id_co, id_co_int, recherche_id = 0, 0, 0
        id_clients = {}
    except NameError as nom_err:
        print(nom_err)
        input()
    except TypeError as type_err:
        print(type_err)
        input()

    while serveur_lance:
        # On va vérifier que de nouveaux clients ne demandent pas à se connecter
        # Pour cela, on écoute la connexion_principale en lecture
        # On attend maximum 50ms
        connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)

        for connexion in connexions_demandees:
            connexion_avec_client, infos_connexion = connexion.accept()
            try:
                id_co += 1
                id_co_int = int(id_co)
                connexion_avec_client.send("id_{0}".format(id_co).encode())

                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)
                id_clients[id_co_int] = connexion_avec_client

                client_en_cours = id_clients[id_co_int]

                os_client = client_en_cours.recv(1024).decode()
                architecture_client = client_en_cours.recv(1024).decode()
                v_client = client_en_cours.recv(1024).decode()
                python_client = client_en_cours.recv(1024).decode()
                print("{0} sous {1} {2} v{3} avec {4}, id:{5} est maintenant connecté à Elranet."
                      .format(infos_connexion, os_client, architecture_client, v_client, python_client, id_co))
            except NameError as nom_err:
                print(nom_err)
                input()
            except TypeError as type_err:
                print(type_err)
                input()

        # Maintenant, on écoute la liste des clients connectés
        # Les clients renvoyés par select sont ceux devant être lus (recv)
        # On attend là encore 50ms maximum
        # On enferme l'appel à select.select dans un bloc try
        # En effet, si la liste de clients connectés est vide, une exception
        # Peut être levée
        clients_a_lire = []
        try:
            clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
        except select.error:
            pass

        finally:
            # On parcourt la liste des clients à lire
            for client in clients_a_lire:
                # Client est de type socket
                msg_recu = client.recv(1024)
                # Peut planter si le message contient des caractères spéciaux
                msg_recu = msg_recu.decode()
                msg_recu = "{0} a envoyé : {1}".format(infos_connexion, msg_recu)
                print("\n{0}".format(msg_recu))
                ok = "5 / 5"
                ok_a_encoder = ok.encode()
                client.send(ok_a_encoder)
                if re.search(r'ren$', msg_recu) is None:
                    for client in clients_connectes:
                        client.send(msg_recu.encode())
                    ok_a_encoder = ""
                elif re.search(r'ren$', msg_recu) is not None:
                    last_name = re.sub(r'(\nren)', r'', msg_recu)
                    while recherche_id != id_co_int:
                        recherche_id += 1
                    if recherche_id == id_co_int:
                        envoie_id = id_clients[recherche_id]
                    print("{0} a demandé à être renommé en {1}."
                          .format(envoie_id, last_name))
                    for client in clients_connectes:
                        client.send("{0} a demandé à être renommé en {1}."
                                    .format(envoie_id, last_name).encode())
                    ok_a_encoder = ""
                    id_co = str(id_co)
                    id_co = last_name
                    id_client[recherche_id] = last_name
                elif re.search(r'id', msg_recu) is not None:
                    while recherche_id != id_co_int:
                        recherche_id += 1
                    if recherche_id == id_co_int:
                        envoie_id = id_clients[recherche_id]
                        envoie_id.send("Identifiant utilisateur : {0}, {1}."
                                       .format(id_co_int, infos_connexion).encode())
                if msg_recu == "fin":
                    serveur_lance = False

    print("Fermeture des connexions. Appuyer sur une touche pour continuer . . .")
    wait = input()
    for client in clients_connectes:
        client.close()
    connexion_principale.close()

serveur()