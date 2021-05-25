from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QMainWindow
from back import *

class Ui_Main(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('mainmenu.ui', self)
        #self.setFixedSize(500, 500)
        self.setFixedSize(900, 700)
        self.get_weakness()
        self.pushButton.clicked.connect(self.set_weakness)
        self.pushButton_5.clicked.connect(self.set_fin)
        self.label_153.setPixmap(QtGui.QPixmap("D:/реклама/a.jpg"))



        self.show()
    def set_fin(self):
        try:
            self.set_proceeds()
            self.set_salary()
            self.set_loan()
            self.set_expenses()
        except Exception as e:
            print(e)
    def set_proceeds(self):
        service=self.lineEdit_104.text()
        price=self.spinBox_109.text()
        amount=self.spinBox_110.text()
        set_proceeds_data(service, price, amount)

    def set_salary(self):
        occupation=self.lineEdit_109.text()
        perm_salary=self.spinBox_104.text()
        revenue_percentage=self.spinBox_101.text()
        tax=self.spinBox_102.text()
        insurance=self.spinBox_103.text()
        set_salary_data(occupation, perm_salary, revenue_percentage, tax, insurance)

    def set_loan(self):
        credit_sum=self.spinBox_105.text()
        percentage = self.spinBox_106.text()
        period = self.spinBox_107.text()
        set_loan_data(credit_sum, percentage, period)

    def set_expenses(self):
        name=self.lineEdit_116.text()
        cost = self.spinBox_108.text()
        set_expenses_data(name, cost)



    def set_weakness(self):
        try:
            names=[self.lineEdit_2,self.lineEdit_4,self.lineEdit_6,self.lineEdit_8,self.lineEdit_10]
            actions=[self.lineEdit_3,self.lineEdit_5,self.lineEdit_7,self.lineEdit_9,self.lineEdit_11]
            importance=[self.spinBox,self.spinBox_3,self.spinBox_5,self.spinBox_7,self.spinBox_9]
            probability=[self.spinBox_2,self.spinBox_4,self.spinBox_6,self.spinBox_8,self.spinBox_10]
            power=[self.label_22,self.label_23,self.label_24,self.label_25,self.label_26]
            for i in range(0,5):
                print(i)
                name=names[i].text()
                if(name):
                    action=actions[i].text()
                    imp=importance[i].text()
                    prob=probability[i].text()
                    set_swot_data(i,"weaknesses",name,action,imp,prob)

            self.get_weakness()
        except Exception as e:
            print(e)

    def get_weakness(self):
        names = [self.lineEdit_2, self.lineEdit_4, self.lineEdit_6, self.lineEdit_8, self.lineEdit_10]
        actions = [self.lineEdit_3, self.lineEdit_5, self.lineEdit_7, self.lineEdit_9, self.lineEdit_11]
        importance = [self.spinBox, self.spinBox_3, self.spinBox_5, self.spinBox_7, self.spinBox_9]
        probability = [self.spinBox_2, self.spinBox_4, self.spinBox_6, self.spinBox_8, self.spinBox_10]
        power = [self.label_22, self.label_23, self.label_24, self.label_25, self.label_26]
        res=get_swot_data("weaknesses")
        for r in res:
            i=r["id"]
            names[i].setText(r["name"])
            actions[i].setText(r["action"])
            importance[i].setValue(r["importance"])
            probability[i].setValue(r["probability"])
            power[i].setText(str(r["power"]))

    def closeEvent(self, event):
        sqlite_connection.commit()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Main()
    myapp.show()
    sys.exit(app.exec_())