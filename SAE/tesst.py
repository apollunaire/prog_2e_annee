import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QMenu
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        QtWidgets.QMainWindow.__init__(self)


        self.setWindowTitle("Serveur menu")
        self.resize(1200, 600)

        layout = QGridLayout()
        #layout.addWidget([composant], [emplacement])
        layout.addWidget(Color('black'), 0, 0, 0, 0)
        layout.addWidget(Color('green'), 1, 1, 1, 1)
        layout.addWidget(Color('blue'), 0, 0, 1, 1)
        layout.addWidget(Color('purple'), 1, 0, 1, 1)
        layout.addWidget(Color('yellow'), 0, 1, 1, 1)


        buttonA = QtWidgets.QPushButton('Click!', self)
        self.buttonA.clicked.connect(self.clickCallback)
        self.buttonA.move(100, 50)

        self.labelA = QtWidgets.QLabel(self)
        self.labelA.move(110, 100)



        widget = QWidget()
        #widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.__createMenuBar()
        self.clickCallback()

    def clickCallback(self):
        self.labelA.setText("Button is clicked")

    def __createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File")
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

