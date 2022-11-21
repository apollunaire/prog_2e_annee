import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
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

        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(1200, 600)

        layout = QGridLayout()

        layout.addWidget(Color('black'), 0, 0, 0, 0)
        layout.addWidget(Color('green'), 1, 0, 1, 0)
        #layout.addWidget(Color('blue'), 1, 1, 0, 0)
        #layout.addWidget(Color('purple'), 2, 1, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

