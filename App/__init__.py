# Author : Sr@1
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt

#User file imports
from initUI import UI
from initMenubar import Menubar

#Main class inheriting from the QMainWindow
class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.filename = ""

        self.initUI()

    initMenubar = Menubar
    initUI = UI


def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
