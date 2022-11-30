import sys
import platform
import psutil
import socket

def get_OS(m:str) ->str:
    return f"\t{platform.uname().system} {platform.uname().release}"


def get_CPU(m:str) -> str:
    return f"\t{psutil.cpu_percent()}%"


def get_nom(m:str) -> str:
    return f"\t{platform.node()}"

def get_RAM(m:str) -> str:
    return f"\tUtilisée : {round((psutil.virtual_memory().used)/1000000000, 2)} GB\n" \
           f"\tRestante : {round(psutil.virtual_memory().free/1000000000, 2)} GB\n" \
           f"\tTotale : {round(psutil.virtual_memory().total/1000000000, 2)} GB"

def get_IP(m:str) -> str:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return f"\t{host_ip}"

def get_hostname(m:str) -> str:
    return f"\t{socket.gethostname()}"

def disconnect(m:str) -> str:
    k = f"disconnect {m}"
    print(k)
    return (f"envoi commande : {k}")

def kill(m:str) -> str:
    k = f"kill {m}"
    print(k)
    return (f"envoi commande : {k}")

def reset(m:str) -> str:
    k = f"reset {m}"
    print(k)
    return (f"envoi commande : {k}")






if __name__=='__main__':
    print(f"OS : {get_OS()}")
    print(f"CPU : {get_CPU()}")
    print(f"RAM : {get_RAM()}")

    sys.exit()