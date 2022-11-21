import sys
import threading
from socket1 import *
from socket2 import *

if __name__=='main':
    t1=threading.Thread(target=socket_client(), args=[1])
    t2=threading.Thread(target=socket_client(), args=[2])

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    sys.exit()