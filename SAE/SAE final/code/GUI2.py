import sys, csv, socket, re
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QCompleter,QInputDialog, QApplication, QGraphicsWidget, QTextEdit, QFileDialog, QComboBox, \
    QLabel, QMainWindow, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QCloseEvent
from client import Client



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__createMenuBar() #barre de menu
        widget = QWidget() #widget
        self.setCentralWidget(widget) #place
        self.client = None #connexion

        self.commandes = ["powershell:get-process", "python --version", "ping 192.157.65.78",
                          "dos:mkdir toto", "linux:ls -la", "dos:dir"] #liste de commandes pour auto-completion
        self.__txtChoixM = QLabel("Séléctionner la machine :") #label choix machine
        self.__txtCmm = QLabel("Commande à executer :") #label commande
        self.__txtImport = QLabel("Importer un fichier csv :") #label fichier csv
        self.__choixM = QComboBox() #combobox pour choix machine
        self.__liste = [] #liste de machines
        self.__choixM.addItems(self.__liste) #ajout de cette liste à la combobox
        self.__entreeCmm = QLineEdit("") #lineedit pour commande
        self.__bOS = QPushButton("OS") #label os
        self.__bRAM = QPushButton("RAM") #label ram
        self.__bIP = QPushButton("IP") #label ip
        self.__bCPU = QPushButton("CPU") #label cpu
        self.__bName = QPushButton("Nom") #label name
        self.__bALL = QPushButton("ALL INFO") #label all info
        self.__sortieB = QTextEdit("") #textedit pour sortie des commandes simples
        self.__sortieB.setDisabled(True) #impossible à modifier pour l'utilisateur.ice
        self.__sortieCmm = QTextEdit("") #textedit pour sortie des commandes de l'utilisateur.ice
        self.__sortieCmm.setDisabled(True) #impossible à modifier
        self.__bKill = QPushButton("KILL") #bouton kill
        self.__bDisc = QPushButton("DISCONNECT") #bouton disconnect
        self.__bReset = QPushButton("RESET") #bouton reset
        self.__bInfo = QPushButton("?") #bouton informations
        self.__bfile = QPushButton("CSV file") #bouton import fichier csv
        self.__filename = QFileDialog() #explorateur de fichier
        self.__filename.setFileMode(QFileDialog.AnyFile) #tous les fichiers
        self.__filename.setNameFilter("*.csv") #avec un filtre sur le type (csv)
        self.__file = QLineEdit("") #lineedit pour afficher le nom du fichier csv utilisé
        self.__file.setDisabled(True) #impossible à modifier pour l'utilisateur.ice
        #self.__bOK = QPushButton("OK") #bouton OK
        self.__bConnect = QPushButton("Connect") #bouton connect pour établir la connexion avec le serveur
        self.__completer = QCompleter(self.commandes) #auto-completion pour les commandes utilisateur.ice
        self.__entreeCmm.setCompleter(self.__completer) #lien entre le qlineedit et l'auto completeur

        self.__msgb = QMessageBox() #messagebox pour l'état de la connexion
        self.__msgb.setWindowTitle("Connexion")
        self.__msgb.setText(" "*31 + "Aucune connexion en cours." + " "*31)
        self.__msgb.adjustSize()

        grid = QGridLayout()
        widget.setLayout(grid)

        #composants layout
        grid.addWidget(self.__txtChoixM, 2, 1, 1, 3)
        grid.addWidget(self.__txtCmm, 2, 6, 1, 3)
        grid.addWidget(self.__choixM, 3, 1, 1, 2)
        grid.addWidget(self.__bConnect, 3, 3, 1, 1)
        grid.addWidget(self.__entreeCmm, 3, 6, 1, 4)
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
        grid.addWidget(self.__bfile, 3, 10, 1, 2)
        grid.addWidget(self.__file, 4, 6, 1, 6)


        #gestion des actions pour les boutons
        self.__bConnect.clicked.connect(self.__crea_thread)
        self.__bCPU.clicked.connect(self.__actionCPU)
        self.__bOS.clicked.connect(self.__actionOS)
        self.__bALL.clicked.connect(self.__actionALL)
        self.__bIP.clicked.connect(self.__actionIP)
        self.__bRAM.clicked.connect(self.__actionRAM)
        self.__bName.clicked.connect(self.__actionName)
        self.__entreeCmm.returnPressed.connect(self.__actionCMM)
        self.__bInfo.clicked.connect(self.__actionhelp)
        self.__bReset.clicked.connect(self.__actionReset)
        self.__bDisc.clicked.connect(self.__actionDis)
        self.__bKill.clicked.connect(self.__actionKill)
        self.__bfile.clicked.connect(self.__actionFile)

        #reglages fenêtre
        self.setWindowTitle("Monitoring")
        self.resize(800, 500)



    def __createMenuBar(self):
        """barre de menu"""
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File")
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

    def is_valid_ip(self, ip:str) -> bool:
        """test adresse ip"""
        ipex = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        if re.search(ipex, ip):
            return True
        else:
            return False

    def __actionCPU(self):
        """affichage de la cpu si client connecté"""
        if self.client!=None:
            self.__sortieB.setText(f"{(self.client).commandes['cpu']}")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")

    def __actionRAM(self):
        """affichage de la ram si client connecté"""
        if self.client != None:
            self.__sortieB.setText(f"{(self.client).commandes['RAM']}")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")
    def __actionIP(self):
        """affichage de l'@ip si client connecté"""
        if self.client != None:
            self.__sortieB.setText(f"{(self.client).commandes['ip']}")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")
    def __actionOS(self):
        """affichage du systeme d'exploitation si client connecté"""
        if self.client != None:
            self.__sortieB.setText(f"{(self.client).commandes['os']}")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")
    def __actionName(self):
        """affichage du nom de la machine si client connecté"""
        if self.client != None:
            self.__sortieB.setText(f"{(self.client).commandes['name']}")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")
    def __actionALL(self):
        """affichage de toutes les informations précédentes si client connecté"""
        if self.client != None:
            self.__sortieB.setText(f"OS : \n{(self.client).commandes['os']}\n"
                                f"RAM : \n{(self.client).commandes['RAM']}\n"
                                f"CPU : \n{(self.client).commandes['cpu']}\n"
                                f"IP : \n{(self.client).commandes['ip']}\n"
                                f"Nom : \n{(self.client).commandes['name']}\n")
        else:
            self.__sortieB.setText(f"vous n'êtes pas connecté‧e")

    def __actionDis(self):
        """deconnexion du client"""
        if self.client!=None:
            self.client.envoi("disconnect")
            self.client=None

    def __actionKill(self):
        """fermeture du cliet et du serveur"""
        if self.client!=None:
            self.client.envoi("kill")
            self.client=None

    def __actionReset(self):
        """deconnexion du client et fermeture puis ouverture du serveur"""
        if self.client!=None:
            self.client.envoi("reset")
            self.client=None

    def __actionCMM(self):
        os_txt = self.client.commandes['os'] #recuperation de l'os
        try :
            val = self.__entreeCmm.text()
            n = [True for k in val if k == ":"] #si : dans la commande alors commande specifique
            if n == [True]: #si valeur avec :
                l = (val.split(":", 1)) #séparation
                shell = l[0] #recup shell
                tmp = str(l[1:])
                cmm = tmp[2:-2] #recup commande
                print(cmm)
                k = f"{shell};{cmm}"
                print(os_txt.lower())
                if (("darwin" in os_txt.lower()) and ("linux" or "powershell" in shell.lower())) \
                    or ("window" in os_txt.lower() and ("powershell" in shell.lower())) \
                        or ("linux" in os_txt.lower() and (("powershell" in shell.lower() or "dos" in shell.lower()))):
                    #test si os est en accord avec le shell souhaité
                    self.client.envoi(f"{k}") #envoi de la commande au client
                    j = self.client.reception() #lectre de la sortie
                    #print(j)
                    self.__sortieCmm.setText(f"{j}") #affichage sur GUI
                else: #si shell pas en accord avec l'os
                    self.__sortieCmm.setText("la commande est soit erronnée soit impossible à executer sur ce système") #affichage d'un message d'erreur
                    return -1
            else: #si commande sans shell precise
                self.client.envoi(val) #envoi
                j = self.client.reception() #reception sortie
                self.__sortieCmm.setText(f"{j}") #affichage

            if not val in self.commandes: #si la commande n'a pas déjà été lancée
                #print(f"ajout de : {val}")
                self.commandes.append(val) #ajout de celle-ci à la liste des commandes
                #print(self.commandes)
                self.__completer = QCompleter(self.commandes) #mise à jour de l'auto-completeur
                self.__entreeCmm.setCompleter(self.__completer) #et du lien entre le lineedit
        except OSError as err:
            self.__sortieCmm.setText(f"ERR - {err}") #si os pas ok, message d'erreur
            return -1

    def __actionhelp(self):
        """infos de connexion"""
        if self.client!=None: #si connexion
            val = self.client.get_status() #recuperation des infos
            print(val[1:-1])
            k = val[1:-1].split(",")
            print(val)
            self.__msgb.setText(f"adresse IP : {k[0][1:-1]}\n"
                                f"port : {k[1]}")
        else:
            self.__msgb.setText("Aucune connexion en cours")
        self.__msgb.open()
        self.__msgb.window()

    def __actionFile(self):
        """selection du fichier csv"""
        file = self.__filename.getOpenFileName(filter="*csv")
        #print(file)
        self.file = file[0]
        self.__lectureCSV()
        self.__file.setText(self.file)


    def __actionQuitter(self):
        QCoreApplication.exit(0)

    def __lectureCSV(self):
        """lecture du fichier csv et mise à jour du combobox"""
        f = self.file #fichier selectionne
        self.__machines = [] #liste de machines
        try:
            if f != "[]": #si deja fichier
                self.__liste.clear() #effacement des donnees precedentes
                with open(f"{self.file}", newline='\n') as csvfile: #ouverture du fichier csv
                    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|') #lecture du fichier
                    for row in spamreader: #pour chaque ligne
                        self.__liste.append(row[0]) #ajouter le premier element à la liste
                        self.__machines.append(row) #ajouter la ligne aux machines
                        #print(self.__machines)
                        #print(row)
                self.__choixM.clear() #remise à 0
                self.__liste.append("Autre") #ajout du choix autre (pour ajouter machine dans le csv)
                self.__choixM.addItems(self.__liste) #ajouter les éléments de la liste à la combobox
                return 0
            else:
                raise FileNotFoundError ("ERR - il n'y a pas de fichier sélectionné")
        except (FileNotFoundError, FileExistsError):
            self.__file.setText("ERR - le fichier n'a pas été trouvé")
            return -1

    def __crea_thread(self):
        """creation d'un thread pour connexion"""
        try :
            val = self.__choixM.currentText()
            if self.client != None: #si déja une connexion
                self.client.envoi("reset") #reset
            if val == "Autre": #si selction de autre
                    value, ok = QInputDialog.getText(QMessageBox(), 'Ajout machine',
                                                     'Entrez l\'adresse IP de la machine puis relancez la connexion : ') #messagebox pour entrer une @ip
                    if ok and self.is_valid_ip(value)==True: #si valeur est bien une @ip
                        #print(value)
                        with open(f"{self.__file.text()}", 'a') as csvfile: #ajout au fichier csv (pas de test si déjà existant)
                            writer = csv.writer(csvfile)
                            writer.writerow([f"{value}"])
                        self.__lectureCSV() #revision de la liste des machines
            else: #sinon
                if self.is_valid_ip(val)==True:
                    self.client = Client(val, 15001) #creation objet client avec @ip specifiee
                    self.client.connect() #lancement de la connexion
                    #print("thread ok")
                else:
                    err = QMessageBox()
                    err.setText("veuillez selectionner une machine")
                    err.open()
                    err.window()

        except socket.gaierror:
            self.__sockerr = QMessageBox()
            self.__sockerr.setWindowTitle("Erreur")
            self.__sockerr.setText("impossible de lancer la connexion")
            self.__sockerr.adjustSize()

        except FileNotFoundError:
            self.__filenotfound = QMessageBox()
            self.__filenotfound.setWindowTitle("Erreur")
            self.__filenotfound.setText("le fichier spécifié n'a pas été trouvé")
            self.__filenotfound.adjustSize()
        return 0


    def closeEvent(self, _e: QCloseEvent):
        """message d'avertissement avant fermeture de GUI"""
        box = QMessageBox()
        box.setWindowTitle("Quitter")
        box.setText("Voulez vous quitter ?\nCela mettra fin aux connexions en cours.")
        box.addButton(QMessageBox.Yes) #choix yes
        box.addButton(QMessageBox.No) #choix np

        rep = box.exec()

        if rep == QMessageBox.Yes: #si oui
            QCoreApplication.exit(0) #fermeture
            if self.client!=None: #si deja connexion
                self.client.envoi("kill") #kill
        else:
            _e.ignore() #sinon abstraction

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()