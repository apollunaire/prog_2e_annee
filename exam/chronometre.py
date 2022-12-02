import time

from PyQt5.QtCore import Qt, QCoreApplication, QFile
from PyQt5.QtWidgets import QCheckBox, QFileIconProvider, QApplication, QVBoxLayout, QGraphicsWidget, QTextEdit, QFileDialog, QComboBox, QLabel, QMainWindow, QSpinBox, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor
import sys
import threading
import socket

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        self.etat = False
        self.arret_thread = False

        self.__txtcpt = QLabel("Compteur:")
        self.__cmpt = QLineEdit("0")
        self.__cmpt.setDisabled(True)
        self.__bStart = QPushButton("Start")
        self.__bReset = QPushButton("Reset")
        self.__bStop = QPushButton("Stop")
        self.__bConnect = QPushButton("Connect")
        self.__bQuit = QPushButton("Quitter")

        self.client_socket = socket.socket()

        grid = QGridLayout()
        widget.setLayout(grid)


        grid.addWidget(self.__txtcpt, 0, 0, 1, 2)
        grid.addWidget(self.__cmpt, 1, 0, 1, 2)
        grid.addWidget(self.__bStart, 2, 0, 1, 2)
        grid.addWidget(self.__bReset, 3, 0, 1, 1)
        grid.addWidget(self.__bStop, 3, 1, 1, 1)
        grid.addWidget(self.__bConnect, 4, 0, 1, 1)
        grid.addWidget(self.__bQuit, 4, 1, 1, 1)

        self.setWindowTitle("Chronnomètre")
        #self.resize(200, 300)

        self.__bStart.clicked.connect(self.start)
        self.__bQuit.clicked.connect(self.quitter)
        self.__bReset.clicked.connect(self.reset)
        self.__bStop.clicked.connect(self.stop)
        self.__bConnect.clicked.connect(self.connect)

    def start(self):
        #print("début thread")
        start = time.perf_counter()
        #print("début counter")
        self.cmpt = threading.Thread(target=self.__start)  # création de la thread
        #print("thread créée")
        self.cmpt.start()  # je démarre la thread
        #print("thread démarée")
        fin = time.perf_counter()

    def __start(self):
        if self.etat == True:
            message = "Start"
            self.client_socket.send(message.encode())
        val = int(self.__cmpt.text())
        #print(val)
        #print(self.arret_thread)
        while self.arret_thread == False:
            val+= 1
            #print(val)
            self.__cmpt.setText(str(val))
            #print("OK")
            time.sleep(1)


    def stop(self):
        if self.etat == True:
            message = "Stop"
            self.client_socket.send(message.encode())
        self.arret_thread = True
        self.cmpt.join()

    def reset(self):
        if self.etat == True:
            message = "Reset"
            self.client_socket.send(message.encode())
        self.__cmpt.setText("0")

    def quitter(self):
        if self.etat == True:
            message = "Quit"
            self.client_socket.send(message.encode())
            message = "bye"
            self.client_socket.send(message.encode())
            self.etat = False
        self.stop()
        QCoreApplication.exit(0)

    def connect(self):
        try:
            self.client_socket = socket.socket()
            self.client_socket.connect(("localhost", 10000))
            self.etat = True
        except ConnectionRefusedError:
            print("serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print("erreur de connection")
            return -1
        else:
            print("connexion réalisée")
            return 0

        """self.client_socket = socket.socket()
        self.client_socket.connect(("localhost", 10000))
        self.etat = True
        print("connexion réalisée")
        return 0"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()