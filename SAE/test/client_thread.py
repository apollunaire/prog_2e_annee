import socket, threading, sys
import psutil
import platform

"""classe Client héritant de Thread
doit implémenter la méthode run qui est immplictement appelé lorsque l'on démarre le thread à l'aide de start()"""

class Serveur(threading.Thread):

    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()

    def __connect(self) -> int:
        """méthode connexion"""
        try:
            self.__sock.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("monitoring non lancé ou mauvaise information ??")
            return -1
        except ConnectionError:
            print("erreur de connexion")
            return -1
        else:
            print("connexion OK")
            return 0

    def __dialogue(self):
        """methode dialogue synchrone"""
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = input("serveur: ")
            self.__sock.send(msg.encode())
            msg = self.__sock.recv(1024).decode()
            print(msg)
        self.__sock.close()

    def run(self):
        if (self.__connect()==0):
            self.__dialogue()

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

    def disconnect(self, m: str) -> str:
        k = f"disconnect {m}"
        print(k)
        return (f"envoi commande : {k}")

    def kill(self, m: str) -> str:
        k = f"kill {m}"
        print(k)
        return (f"envoi commande : {k}")

    def reset(self, m: str) -> str:
        k = f"reset {m}"
        print(k)
        return (f"envoi commande : {k}")

"""if __name__=="__main__":
    if len(sys.argv) < 3:
        client = Client("127.0.0.1", 15001)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        # création de l'objet client qui est aussi un thread
        client = Client(host, port)
    #démarrage de la thread client
    client.start()
    client.join()"""


test = Serveur("localhost", 10000)
print(test.get_hostname())
test.start()
test.join()



# cd "C:/Users/tipha/Documents/IUT COLMAR/R309/prog_2e_annee/SAE/test/"
# python client_thread.py

