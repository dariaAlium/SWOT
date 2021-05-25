class Ui_LogIn(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('logIn.ui', self)
        self.setFixedSize(500, 500)
        self.logInButton.clicked.connect(self.logInUI)
        # self.show()

    def logInUI(self):
        login = self.loginLine.text()
        password = self.passwordLine.text()
        results = sign_in(login, password)
        self.errorLabel.setText(str("error"))

        self.close()
        # self.Open = SecretQuestionWin(user)
        # self.Open.show()
        print("hi")