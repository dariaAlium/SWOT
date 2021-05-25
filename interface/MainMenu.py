from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
from back import *

class Ui_Main(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('mainmenu.ui', self)
        #self.setFixedSize(500, 500)
        self.setFixedSize(900, 700)
        self.pushButton.clicked.connect(self.set_weakness)
        self.show()
    def set_weakness(self):
        names=[self.lineEdit_2,self.lineEdit_4,self.lineEdit_6,self.lineEdit_8,self.lineEdit_10]
        actions=[self.lineEdit_3,self.lineEdit_5,self.lineEdit_7,self.lineEdit_9,self.lineEdit_11]
        importance=[self.spinBox,self.spinBox_3,self.spinBox_5,self.spinBox_7,self.spinBox_9]
        probability=[self.spinBox_2,self.spinBox_4,self.spinBox_6,self.spinBox_8,self.spinBox_10]
        power=[self.label_22,self.label_23,self.label_24,self.label_25,self.label_26]
        for i in range(0,6):
            name=names[i].text()
            if(name):
                action=actions[i].text()
                imp=importance[i].text()
                prob=probability[i].text()
                set_swot_data(i,"weaknesses",action,imp,prob)
        #вызвать функцию гет

    def get_weakness(self):
        names = [self.lineEdit_2, self.lineEdit_4, self.lineEdit_6, self.lineEdit_8, self.lineEdit_10]
        actions = [self.lineEdit_3, self.lineEdit_5, self.lineEdit_7, self.lineEdit_9, self.lineEdit_11]
        importance = [self.spinBox, self.spinBox_3, self.spinBox_5, self.spinBox_7, self.spinBox_9]
        probability = [self.spinBox_2, self.spinBox_4, self.spinBox_6, self.spinBox_8, self.spinBox_10]
        power = [self.label_22, self.label_23, self.label_24, self.label_25, self.label_26]
        res=get_swot_data()
        for r in res:
            names[r["id"]].setText()

            name = names[i].text()
            if (name):
                action = actions[i].text()
                imp = importance[i].text()
                prob = probability[i].text()
                get_swot_data("weaknesses")




    def logInUI(self):
        login = self.loginLine.text()
        password = self.passwordLine.text()
        results = sign_in(login, password)
        self.errorLabel.setText(str("error"))

        self.close()
        # self.Open = SecretQuestionWin(user)
        # self.Open.show()
        print("hi")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Main()
    myapp.show()
    sys.exit(app.exec_())