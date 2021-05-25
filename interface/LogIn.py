from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow

from back import *
#from MainMenu import *

from interface.MainMenu import Ui_Main


class Ui_LogIn(QMainWindow):
    def __init__(self):
        print("logIn")
        super(QMainWindow, self).__init__()
        init_conn()
        uic.loadUi('logIn.ui', self)
        self.setFixedSize(500, 500)
        # log in button
        self.logInButton.clicked.connect(self.logInUI)
        # registration button
        self.unregisteredButton.clicked.connect(self.registrationUI)
        # self.show()

    def logInUI(self):
        print("logInUI")
        login = self.loginLine.text()
        password = self.passwordLine.text()
        print(login, password)
        try:
            results = sign_in(login, password)
            print(results)
            if results:
                self.errorLabel.setText(str("success"))
                print("success")
                self.close()
                print("self.close()")
                self.Open = Ui_Main()
                self.Open.show()
            # self.close()
            #self.Open.show()
        except Exception as e:
            print(e)
            self.errorLabel.setText(str(e))


        # self.close()
        # self.Open = SecretQuestionWin(user)
        # self.Open.show()

    def registrationUI(self):
        print("registrationUI")
        login = self.loginLine.text()
        password = self.passwordLine.text()
        print(login, password)
        try:
            results = sign_up(login, password)
            print(results)
            if results:
                self.errorLabel.setText(str("success"))
                print("success")
                self.close()
                print("self.close()")
                self.Open = Ui_Main()
                self.Open.show()
            # self.close()
            #self.Open.show()
        except Exception as e:
            self.errorLabel.setText(str(e))


    def closeEvent(self, event):
        sqlite_connection.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_LogIn()
    myapp.show()
    #sqlite_connection.close()
    sys.exit(app.exec_())
    sqlite_connection.close()
