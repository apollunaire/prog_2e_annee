import sys
from socket1 import *

if __name__=='__main__':
    try:
        print(socket_serveur())
        #print(socket_client())
    except (TimeoutError, ConnectionRefusedError, socket.gaierror, ConnectionResetError, BrokenPipeError) as err:
        print(f"ERREUR - {err}")
    except OSError as err:
        print(f"ERREUR - {err}")
    sys.exit()