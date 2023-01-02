import socket, sys
import platform
import psutil


class Client():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
        self.message = ""

    def connect(self) -> int:
        """fonction pour gérer la connexion"""
        try:
            self.__sock.connect((self.__host, self.__port))
        except ConnectionRefusedError:
            print("Serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print("Erreur de connexion")
            return -1
        else:
            print("Connexion OK")
            self.commandes:dict = {"os": f"\t{platform.system()} {platform.release()}",
                         "cpu": f"\t{psutil.cpu_percent()}%",
                         "name": f"\t{socket.gethostname()}",
                         "RAM": f"\tUtilisée : {round((psutil.virtual_memory().used) / 10 ** 9, 2)} GB\n" \
                                f"\tRestante : {round(psutil.virtual_memory().free / 10 ** 9, 2)} GB\n" \
                                f"\tTotale : {round(psutil.virtual_memory().total / 10 ** 9, 2)} GB",
                         "ip": f"{socket.gethostbyname(socket.gethostname())}"}
            return 0

    def reception(self):
        """reception des messages"""
        msg_recu = self.__sock.recv(1024)
        msg = msg_recu.decode()
        return msg


    def envoi(self, message:str):
        """envoi de messages"""
        try:
            self.message = message
            envoi = self.message.encode()
            #print("Envoi du message ")
            self.__sock.sendall(envoi)
        except BrokenPipeError:
            print("Erreur : socket fermé")
        return self.message


    """def get_OS(self) -> str:
        platform.system()
        platform.release()
        return f"\t{platform.system()} {platform.release()}"

    def get_CPU(self) -> str:
        return f"\t{psutil.cpu_percent()}%"

    def get_nom(self) -> str:
        return f"\t{platform.node()}"

    def get_RAM(self) -> str:
        return f"\tUtilisée : {round((psutil.virtual_memory().used) / 10**9, 2)} GB\n" \
               f"\tRestante : {round(psutil.virtual_memory().free / 10**9, 2)} GB\n" \
               f"\tTotale : {round(psutil.virtual_memory().total / 10**9, 2)} GB"

    def get_IP(self) -> str:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return f"\t{host_ip}"

    def get_hostname(self) -> str:
        return f"\t{socket.gethostname()}"""""

    def get_status(self):
        """obtention du port et de l'adresse ip utilisés"""
        status = self.__sock.getpeername()
        return f"{status}"


if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1", 15001)
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        client = Client(host, port) #objet client

    client.connect()
