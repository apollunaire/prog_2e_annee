import sys

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow, QSpinBox, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__textTemp = QLabel("Température")
        self.__textConv = QLabel("Conversion")
        self.__bConv = QPushButton("Convertir")
        self.__textC = QLabel("°C")
        self.__textK = QLabel("K")
        self.__liste = ["°C vers K", "K vers °C"]
        self.__choix = QComboBox()
        self.__choix.addItems(self.__liste)
        self.__result = QLineEdit("", )
        self.__result.setDisabled(True)
        self.__entree = QLineEdit("")

        self.__testb = QPushButton("?")

        self.__msgb =QMessageBox()
        self.__msgb.setText("Permet de convertir un nombre de Kelvin en °C ou de °C en Kelvin.")
        self.__msgb.setWindowTitle("Aide")
        self.__msgb.adjustSize()


        grid = QGridLayout()
        widget.setLayout(grid)

        # Ajouter les composants au grid ayout
        grid.addWidget(self.__textTemp, 0, 0)
        grid.addWidget(self.__entree, 0, 1)
        grid.addWidget(self.__textC, 0, 2)
        grid.addWidget(self.__bConv, 1, 1)
        grid.addWidget(self.__choix, 3, 4)
        grid.addWidget(self.__textConv, 3, 0)
        grid.addWidget(self.__result, 3, 1)
        grid.addWidget(self.__textK, 3, 2)
        grid.addWidget(self.__testb, 5, 5)




        self.__bConv.clicked.connect(self.__actionConv)
        self.__choix.currentIndexChanged.connect(self.__testValeur)
        self.setWindowTitle("Une première fenêtre")
        self.resize(350, 100)
        self.__testValeur()
        self.__testb.clicked.connect(self.__actionhelp)


    def __actionConv(self):
        val = self.__entree.text()
        try:
            print(self.__entree.text())
            self.__choix.currentIndexChanged.connect(self.__testValeur)
            if self.__choix.currentText() == "°C vers K":
                val = float(val)
                if val < -273.15:
                    raise ValueError(self.__result.setText("impossible d'atteindre une valeur inférieure au zéro absolu"))
                self.__result.setText(f"{val+273.15}")

            else:
                if val < 0:
                    raise ValueError(self.__result.setText("impossible d'atteindre une valeur inférieure au zéro absolu"))
                val = float(val)
                self.__result.setText(f"{val-273.15}")
            pass
        except ValueError as err:
            self.__result.setText(f"{err}")
            self.__msgb.setText(f"{err}")
            print(err)

    def __actionhelp(self):
        self.__msgb.open()
        self.__msgb.window()





    def __testValeur(self):
        val = self.__choix.currentText()
        if val == self.__liste[1]:
            self.__textC.setText("K")
            self.__textK.setText("°C")
        elif val == self.__liste[0]:
            self.__textC.setText("°C")
            self.__textK.setText("K")


    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()