import sys

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QMenuBar, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__test = QLabel("")
        self.__texte = QLineEdit("")
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir votre nom")
        #text = QLineEdit("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        #test = QLabel("")

        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.__texte, 1, 0)
        grid.addWidget(ok, 2, 0)
        grid.addWidget(self.__test, 3, 0)
        grid.addWidget(quit, 4, 0)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Une première fenêtre")
        self.resize(350, 100)

    def __actionOk(self):
        texte_a_copier = self.__texte.text()
        self.__test.setText(f"Bonjour {texte_a_copier}")
        pass
    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()