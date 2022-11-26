import sys
from SAE.main import get_OS, get_RAM, get_CPU, get_IP, get_hostname
from PyQt5.QtCore import Qt, QCoreApplication, QFile
from PyQt5.QtWidgets import QApplication, QTextEdit, QFileDialog, QComboBox, QLabel, QMainWindow, QSpinBox, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor


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
        self.__colorBack = Color("Grey")






        self.__msgb =QMessageBox()
        self.__msgb.setText("Permet de convertir un nombre de Kelvin en °C ou de °C en Kelvin.")
        self.__msgb.setWindowTitle("Aide")
        self.__msgb.adjustSize()


        grid = QGridLayout()
        widget.setLayout(grid)

        # Ajouter les composants au grid ayout
        #grid.addWidget(self.__colorBack, 0, 0, 17, 13)


        grid.addWidget(self.__txtChoixM, 0, 1, 1, 3)
        grid.addWidget(self.__txtCmm, 0, 6, 1, 3)
        grid.addWidget(self.__txtImport, 0, 9, 1, 3)
        grid.addWidget(self.__choixM, 1, 1, 1, 3)
        grid.addWidget(self.__entreeCmm, 1, 6, 1, 3)
        grid.addWidget(self.__upload, 3, 9, 1, 3)
        grid.addWidget(self.__sortieCmm, 3, 6, 1, 3)
        grid.addWidget(self.__bOS, 5, 1, 1, 3)
        grid.addWidget(self.__bRAM, 6, 1, 1, 3)
        grid.addWidget(self.__bCPU, 7, 1, 1, 3)
        grid.addWidget(self.__bIP, 8, 1, 1, 3)
        grid.addWidget(self.__bName, 9, 1, 1, 3)
        grid.addWidget(self.__bALL, 10, 1, 1, 3)
        grid.addWidget(self.__sortieB, 12, 1, 3, 3)
        grid.addWidget(self.__bDisc, 16, 1, 1, 2)
        grid.addWidget(self.__bReset, 16, 6, 1, 2)
        grid.addWidget(self.__bKill, 16, 9, 1, 2)
        grid.addWidget(self.__bInfo, 16, 11)



        self.__bCPU.clicked.connect(self.__actionCMD)
        self.__bOS.clicked.connect(self.__actionCMD)
        self.__bALL.clicked.connect(self.__actionCMD)
        self.__bIP.clicked.connect(self.__actionCMD)
        self.__bRAM.clicked.connect(self.__actionCMD)
        self.__bName.clicked.connect(self.__actionCMD)
        #self.__choix.currentIndexChanged.connect(self.__testValeur)
        self.setWindowTitle("Une première fenêtre")
        self.resize(800, 450)
        #self.__testValeur()
        #self.__testb.clicked.connect(self.__actionhelp)

    def __actionCMD(self):
        val = self.__choixM.currentIndex()
        if self.__bCPU.click:
            self.__sortieB.setText(f"{get_CPU()}")
        if self.__bRAM.click:
            self.__sortieB.setText(f"{get_RAM()}")
        if self.__bIP.click:
            self.__sortieB.setText(f"{get_IP()}")
        if self.__bOS.click:
            self.__sortieB.setText(f"{get_OS()}")
        if self.__bALL.click:
            self.__sortieB.setText(f"OS : {get_OS()}\n"
                                   f"RAM : {get_RAM()}\n"
                                   f"CPU : {get_CPU()}\n"
                                   f"IP : {get_IP()}\n"
                                   f"Nom : {get_hostname()}\n")


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