# Author : Sr@1
"""
Using pyqt5 for the gui og the application

"""

import sys
from pyqt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Sample')
    w.show()

    sys.exit(app.exec_())
