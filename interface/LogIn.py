from PyQt5 import uic
from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QMainWindow


class Ui_LogIn(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('logIn.ui', self)
        self.setFixedSize(500, 500)
        self.logInButton.clicked.connect(self.logInUI)
        #self.show()

    def logInUI(self):
        print("hi")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_LogIn()
    myapp.show()
    sys.exit(app.exec_())
