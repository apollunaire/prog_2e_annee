import sys
from SAE.main import get_OS, get_RAM, get_CPU, get_IP, get_hostname, disconnect, kill, reset
from PyQt5.QtCore import Qt, QCoreApplication, QFile
from PyQt5.QtWidgets import QCheckBox, QFileIconProvider, QApplication, QVBoxLayout, QGraphicsWidget, QTextEdit, QFileDialog, QComboBox, QLabel, QMainWindow, QSpinBox, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor
import subprocess
import csv
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
        self.__createMenuBar()
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
        self.__sortieCmm = QTextEdit("")
        self.__sortieCmm.setDisabled(True)
        self.__bKill = QPushButton("KILL")
        self.__bDisc = QPushButton("DISCONNECT")
        self.__bReset = QPushButton("RESET")
        self.__bInfo = QPushButton("?")
        self.__bExec = QPushButton("->")
        self.__colorBack = Color("Grey")
        self.__bfile = QPushButton("Choisir un fichier")
        self.__filename = QFileDialog()
        self.__filename.setFileMode(QFileDialog.AnyFile)
        self.__filename.setNameFilter("*.csv")
        self.__file = QLineEdit("")
        self.__file.setDisabled(True)
        self.__bOK = QPushButton("OK")


        #self.__filename.getOpenFileName() #ouvre le menu pour choisir le fichier
        #self.__filename.selectedFiles()


        self.__msgb =QMessageBox()
        self.__msgb.setWindowTitle("Aide")
        self.__msgb.setText(" "*31 + "Monitoring de serveurs" + " "*31)
        self.__msgb.adjustSize()

        """grid2 = QGridLayout()
        self.__test = QMessageBox()
        self.__test.setWindowTitle("Choix fichier CSV")
        self.__test.setLayout(grid2)"""


        #self.setLayout(layout)


        grid = QGridLayout()
        widget.setLayout(grid)

        #composants layout
            #grid.addWidget(self.__colorBack, 0, 0, 17, 13)
            #couleur de fond : (jeu sur l'ordre d'appel pour avoir la bonne superposition)
        grid.addWidget(self.__txtChoixM, 2, 1, 1, 3)
        grid.addWidget(self.__txtCmm, 2, 6, 1, 3)
        #grid.addWidget(self.__txtImport, 2, 9, 1, 3)
        grid.addWidget(self.__choixM, 3, 1, 1, 3)
        grid.addWidget(self.__entreeCmm, 3, 6, 1, 3)
        #grid.addWidget(self.__upload, 5, 9, 1, 3)
        grid.addWidget(self.__sortieCmm, 6, 6, 11, 6)
        grid.addWidget(self.__bOS, 6, 1, 1, 3)
        grid.addWidget(self.__bRAM, 7, 1, 1, 3)
        grid.addWidget(self.__bCPU, 8, 1, 1, 3)
        grid.addWidget(self.__bIP, 9, 1, 1, 3)
        grid.addWidget(self.__bName, 10, 1, 1, 3)
        grid.addWidget(self.__bALL, 11, 1, 1, 3)
        grid.addWidget(self.__sortieB, 12, 1, 5, 3)
        grid.addWidget(self.__bDisc, 18, 1, 1, 2)
        grid.addWidget(self.__bReset, 18, 6, 1, 2)
        grid.addWidget(self.__bKill, 18, 9, 1, 2)
        grid.addWidget(self.__bInfo, 18, 11)
        grid.addWidget(self.__bExec, 4, 6, 1, 3)
        grid.addWidget(self.__bfile, 3, 9, 1, 2)
        grid.addWidget(self.__bOK, 3, 11, 1, 1)
        grid.addWidget(self.__file, 4, 9, 1, 3)
        #k = grid.addWidget(Color("Grey"), 0, 0,20, 20)
        #grid.addWidget(self.__filename,  0, 0, 20, 20)


        #gestion des actions pour les boutons
        self.__bCPU.clicked.connect(self.__actionCPU)
        self.__bOS.clicked.connect(self.__actionOS)
        self.__bALL.clicked.connect(self.__actionALL)
        self.__bIP.clicked.connect(self.__actionIP)
        self.__bRAM.clicked.connect(self.__actionRAM)
        self.__bName.clicked.connect(self.__actionName)
        self.__bExec.clicked.connect(self.__actionCMM)
        self.__bInfo.clicked.connect(self.__actionhelp)

        self.__bReset.clicked.connect(self.__actionReset)
        self.__bDisc.clicked.connect(self.__actionDis)
        self.__bKill.clicked.connect(self.__actionKill)
        self.__bfile.clicked.connect(self.__actionFile)
        self.__bOK.clicked.connect(self.__actionOK)
        #self.__choix.currentIndexChanged.connect(self.__testValeur)


        #reglages fenêtre
        self.setWindowTitle("Monitoring")
        self.resize(800, 500)
        #self.__testValeur()


    def __createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File")
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")


    def __actionCPU(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"{get_CPU(m)}")
    def __actionRAM(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"{get_RAM(m)}")
    def __actionIP(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"{get_IP(m)}")
    def __actionOS(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"{get_OS(m)}")
    def __actionName(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"{get_hostname(m)}")
    def __actionALL(self):
        m = self.__choixM.currentText()
        self.__sortieB.setText(f"OS : \n{get_OS(m)}\n"
                                f"RAM : \n{get_RAM(m)}\n"
                                f"CPU : \n{get_CPU(m)}\n"
                                f"IP : \n{get_IP(m)}\n"
                                f"Nom : \n{get_hostname(m)}\n")

    def __actionDis(self):
        m = self.__choixM.currentText()
        disconnect(m)

    def __actionKill(self):
        m = self.__choixM.currentText()
        kill(m)

    def __actionReset(self):
        m = self.__choixM.currentText()
        reset(m)


    def __actionCMM(self):
        os_txt = get_OS(self.__choixM.currentText())
        try :
            val = self.__entreeCmm.text()
            n = [True for k in val if k == ":"]
            if n == [True]:
                l = (val.split(":", 1))
                shell = l[0]
                tmp = str(l[1:])
                cmm = tmp[2:-2]
                print(cmm)
                k = f"{shell};{cmm}"
                print(os_txt.lower())
                if (("darwin" in os_txt.lower()) and ("linux" or "powershell" in shell.lower())) \
                    or ("window" in os_txt.lower() and ("powershell" in shell.lower())) \
                        or ("linux" in os_txt.lower() and (("powershell" in shell.lower() or "dos" in shell.lower()))):
                    print(True)
                    rep = os.popen(cmd=k)
                    k = (rep.read())
                    self.__sortieCmm.setText(f"{k}")
                else:
                    self.__sortieCmm.setText("la commande est soit erronnée soit impossible à executer sur ce système")
                    return -1

            else:
                rep = os.popen(cmd=val)
                k = str(rep.read())
                self.__sortieCmm.setText(f"{k}")
        except OSError as err:
            self.__sortieCmm.setText(f"ERR - {err}")
            return -1


    def __OLDactionCMM(self):
        val = self.__entreeCmm.text()
        n = [True for k in val if k == ":"]
        if n == [True]:
            l = (val.split(":", 1))
            shell = l[0]
            tmp = str(l[1:])
            cmm = tmp[2:-2]
            print(cmm)
            k=f"{shell};{cmm}"
            process = subprocess.Popen(k, stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0] #[0].strip()
            tmp = str(proc_stdout)
            #print(tmp)
            final = tmp[4:-1]
            #print(f" TEST - {final}")
            k = final.splitlines(True)
            self.__sortieCmm.setText(f"{k}") #probblème d'affichage
        else:
            cmm = subprocess.Popen(val, stdout=subprocess.PIPE, shell=True)
            proc_stdout = cmm.communicate()[0] #[0].strip()
            # [0]: resultat renvoyé sous forme de liste donc on prend le premier element
            self.__sortieCmm.setText(f"{proc_stdout}")

    def __actionhelp(self):
        self.__msgb.open()
        self.__msgb.window()

    def __actionFile(self):
        self.__filename.open()
        self.__filename.window()

    def __actionOK(self):
        f = str(self.__filename.selectedFiles())
        file = f[2:-2]
        #print(file)
        self.__file.setText(f"{str(file)}")
        self.__lectureCSV()

    def __actionQuitter(self):
        QCoreApplication.exit(0)

    def __lectureCSV(self):
        f = str(self.__filename.selectedFiles())
        file = f[2:-2]
        self.__machines = []
        try:
            if f != "[]":
                self.__liste.clear()
                with open(f"{file}", newline='\n') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                    for row in spamreader:
                        self.__liste.append(row[0])
                        self.__machines.append(row)
                        print(self.__machines)
                        print(row)
                self.__choixM.clear()
                self.__choixM.addItems(self.__liste)
                return 0
            else:
                raise FileNotFoundError ("ERR - il n'y a pas de fichier sélectionné")
        except (FileNotFoundError, FileExistsError):
            self.__file.setText("ERR - le fichier n'a pas été trouvé")
            return -1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()