import sys
from SAE.main import get_OS, get_RAM, get_CPU, get_IP, get_hostname
from PyQt5.QtCore import Qt, QCoreApplication, QFile
from PyQt5.QtWidgets import QApplication, QTextEdit, QFileDialog, QComboBox, QLabel, QMainWindow, QSpinBox, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor
import subprocess
import os


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__txtChoixM = QLabel("Séléctionner la machine :")
        self.__txtCmm = QLabel("Entrer une commande à executer :")
        self.__txtImport = QLabel("Importer un fichier csv :")
        self.__choixM = QComboBox()
        self.__liste = ["localhost", "test", "pour", "le", "choix", "des", "machines"]
        self.__choixM.addItems(self.__liste)
        self.__entreeCmm = QLineEdit("")
        self.__upload = QLabel("endroit pour uploader un fichier csv")
        self.__bOS = QPushButton("OS")
        self.__bRAM = QPushButton("RAM")
        self.__bIP = QPushButton("IP")
        self.__bCPU = QPushButton("CPU")
        self.__bName = QPushButton("Nom")
        self.__bALL = QPushButton("ALL INFO")
        self.__sortieB = QTextEdit("")
        self.__sortieB.setDisabled(True)
        self.__sortieCmm = QLineEdit("")
        self.__sortieCmm.setDisabled(True)
        self.__bKill = QPushButton("KILL")
        self.__bDisc = QPushButton("DISCONNECT")
        self.__bReset = QPushButton("RESET")
        self.__bInfo = QPushButton("?")
        self.__bExec = QPushButton("->")
        self.__colorBack = Color("Grey")






        self.__msgb =QMessageBox()
        self.__msgb.setText("Permet de convertir un nombre de Kelvin en °C ou de °C en Kelvin.")
        self.__msgb.setWindowTitle("Aide")
        self.__msgb.adjustSize()


        grid = QGridLayout()
        widget.setLayout(grid)

        # Ajouter les composants au grid ayout
        #grid.addWidget(self.__colorBack, 0, 0, 17, 13)
        #couleur de fond : (jeu sur l'ordre d'appel pour avoir la bonne superposition)
        grid.addWidget(self.__txtChoixM, 0, 1, 1, 3)
        grid.addWidget(self.__txtCmm, 0, 6, 1, 3)
        grid.addWidget(self.__txtImport, 0, 9, 1, 3)
        grid.addWidget(self.__choixM, 1, 1, 1, 3)
        grid.addWidget(self.__entreeCmm, 1, 6, 1, 3)
        grid.addWidget(self.__upload, 3, 9, 1, 3)
        grid.addWidget(self.__sortieCmm, 3, 6, 1, 3)
        grid.addWidget(self.__bOS, 4, 1, 1, 3)
        grid.addWidget(self.__bRAM, 5, 1, 1, 3)
        grid.addWidget(self.__bCPU, 6, 1, 1, 3)
        grid.addWidget(self.__bIP, 7, 1, 1, 3)
        grid.addWidget(self.__bName, 8, 1, 1, 3)
        grid.addWidget(self.__bALL, 9, 1, 1, 3)
        grid.addWidget(self.__sortieB, 10, 1, 5, 3)
        grid.addWidget(self.__bDisc, 16, 1, 1, 2)
        grid.addWidget(self.__bReset, 16, 6, 1, 2)
        grid.addWidget(self.__bKill, 16, 9, 1, 2)
        grid.addWidget(self.__bInfo, 16, 11)
        grid.addWidget(self.__bExec, 2, 6, 1, 3)



        self.__bCPU.clicked.connect(self.__actionCPU)
        self.__bOS.clicked.connect(self.__actionOS)
        self.__bALL.clicked.connect(self.__actionALL)
        self.__bIP.clicked.connect(self.__actionIP)
        self.__bRAM.clicked.connect(self.__actionRAM)
        self.__bName.clicked.connect(self.__actionName)
        self.__bExec.clicked.connect(self.__actionCMM)
        #self.__choix.currentIndexChanged.connect(self.__testValeur)
        self.setWindowTitle("Monitoring")
        self.resize(800, 500)
        #self.__testValeur()
        #self.__testb.clicked.connect(self.__actionhelp)

    def __actionCPU(self):
        self.__sortieB.setText(f"{get_CPU()}")
    def __actionRAM(self):
        self.__sortieB.setText(f"{get_RAM()}")
    def __actionIP(self):
        self.__sortieB.setText(f"{get_IP()}")
    def __actionOS(self):
        self.__sortieB.setText(f"{get_OS()}")
    def __actionName(self):
        self.__sortieB.setText(f"{get_hostname()}")
    def __actionALL(self):
        self.__sortieB.setText(f"OS : \n{get_OS()}\n"
                                f"RAM : \n{get_RAM()}\n"
                                f"CPU : \n{get_CPU()}\n"
                                f"IP : \n{get_IP()}\n"
                                f"Nom : \n{get_hostname()}\n")

    def __actionCMM(self):
        val = self.__entreeCmm.text()
        n = [True for k in val if k == ":"]
        if n==[True]:
            l = (val.split(":", 1))
            shell = l.pop(0)
            cmm = l.pop(0)
            k=f"{shell};{cmm}"
            process = subprocess.Popen(k, stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0].strip()
            self.__sortieCmm.setText(f"{proc_stdout}")
        else:
            cmm = subprocess.Popen(val, stdout=subprocess.PIPE, shell=True)
            proc_stdout = cmm.communicate()[0].strip()
            self.__sortieCmm.setText(f"{proc_stdout}")

    def __actionhelp(self):
        self.__msgb.open()
        self.__msgb.window()

    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()