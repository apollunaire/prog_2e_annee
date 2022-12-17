import socket, threading, sys
import platform
import psutil

class Client():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
        self.__thread = None

    # fonction de connection.
    def connect(self) -> int:
        try:
            self.__sock.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print("erreur de connection")
            return -1
        else:
            print("connexion réalisée")
            return 0

    """ 
        fonction qui gére le dialogue
        -> lance une thread pour la partie reception 
        -> lance une boucle pour la partie emission. arréte si kill, reset ou disconnect
    """

    def dialogue(self, msg:str=""):
        #msg = ""
        self.__thread = threading.Thread(target=self.__reception, args=[self.__sock, ])
        self.__thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.__envoi()
        self.__thread.join()
        self.__sock.close()

    # méthode d'envoi d'un message au travers la socket. Le résultat de cette methode est le message envoyé.
    def __envoi(self):
        msg = input("client: ")
        try:
            self.__sock.send(msg.encode())
        except BrokenPipeError:
            print("erreur, socket fermée")
        return msg

    """
      thread recepction, la connection étant passée en argument
    """

    def __reception(self, conn):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)

    def get_OS(self) -> str:
        platform.system()
        platform.release()
        return f"\t{platform.system()} {platform.release()}"

    def get_CPU(self) -> str:
        return f"\t{psutil.cpu_percent()}%"

    def get_nom(self) -> str:
        return f"\t{platform.node()}"

    def get_RAM(self) -> str:
        return f"\tUtilisée : {round((psutil.virtual_memory().used) / 1000000000, 2)} GB\n" \
               f"\tRestante : {round(psutil.virtual_memory().free / 1000000000, 2)} GB\n" \
               f"\tTotale : {round(psutil.virtual_memory().total / 1000000000, 2)} GB"

    def get_IP(self) -> str:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return f"\t{host_ip}"

    def get_hostname(self) -> str:
        return f"\t{socket.gethostname()}"


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1",15001)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        # création de l'objet client qui est aussi un thread
        client = Client(host, port)
        
    # en dehors du if
    client.connect()
    client.dialogue()