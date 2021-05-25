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
        # self.setFixedSize(500, 500)
        self.setFixedSize(900, 700)
        self.get_weakness()
        self.pushButton.clicked.connect(self.set_weakness)
        self.pushButton_5.clicked.connect(self.set_fin)
        self.label_153.setPixmap(QtGui.QPixmap("D:/реклама/a.jpg"))
        self.questionThemeComboBox.addItems(view_all_projects())
        self.questionThemeComboBox.currentIndexChanged.connect(self.choose_project)
        self.themeTestButton.clicked.connect(self.view_project)
        self.genetalTestButton.clicked.connect(self.create_project)


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
            names = [self.lineEdit_2, self.lineEdit_4, self.lineEdit_6, self.lineEdit_8, self.lineEdit_10]
            actions = [self.lineEdit_3, self.lineEdit_5, self.lineEdit_7, self.lineEdit_9, self.lineEdit_11]
            importance = [self.spinBox, self.spinBox_3, self.spinBox_5, self.spinBox_7, self.spinBox_9]
            probability = [self.spinBox_2, self.spinBox_4, self.spinBox_6, self.spinBox_8, self.spinBox_10]
            power = [self.label_22, self.label_23, self.label_24, self.label_25, self.label_26]
            for i in range(0, 5):
                print(i)
                name = names[i].text()
                if (name):
                    action = actions[i].text()
                    imp = importance[i].text()
                    prob = probability[i].text()
                    set_swot_data(i, "weaknesses", name, action, imp, prob)

            self.get_weakness()
        except Exception as e:
            print(e)

    def get_weakness(self):
        names = [self.lineEdit_2, self.lineEdit_4, self.lineEdit_6, self.lineEdit_8, self.lineEdit_10]
        actions = [self.lineEdit_3, self.lineEdit_5, self.lineEdit_7, self.lineEdit_9, self.lineEdit_11]
        importance = [self.spinBox, self.spinBox_3, self.spinBox_5, self.spinBox_7, self.spinBox_9]
        probability = [self.spinBox_2, self.spinBox_4, self.spinBox_6, self.spinBox_8, self.spinBox_10]
        power = [self.label_22, self.label_23, self.label_24, self.label_25, self.label_26]
        res = get_swot_data("weaknesses")
        for r in res:
            i = r["id"]
            names[i].setText(r["name"])
            actions[i].setText(r["action"])
            importance[i].setValue(r["importance"])
            probability[i].setValue(r["probability"])
            power[i].setText(str(r["power"]))
    
    def set_strengths(self):
        try:
            names=[self.lineEdit_19,self.lineEdit_20,self.lineEdit_15,self.lineEdit_13,self.lineEdit_18]
            actions=[self.lineEdit_17,self.lineEdit_12,self.lineEdit_16,self.lineEdit_14,self.lineEdit_21]
            importance=[self.spinBox_13,self.spinBox_17,self.spinBox_18,self.spinBox_19,self.spinBox_20]
            probability=[self.spinBox_16,self.spinBox_15,self.spinBox_11,self.spinBox_14,self.spinBox_12]
            power=[self.label_28,self.label_34,self.label_33,self.label_35,self.label_31]
            for i in range(0,5):
                print(i)
                name=names[i].text()
                if(name):
                    action=actions[i].text()
                    imp=importance[i].text()
                    prob=probability[i].text()
                    set_swot_data(i,"strengths",name,action,imp,prob)

            self.get_strengths()
        except Exception as e:
            print(e)

    def get_strengths(self):
        names=[self.lineEdit_19,self.lineEdit_20,self.lineEdit_15,self.lineEdit_13,self.lineEdit_18]
        actions=[self.lineEdit_17,self.lineEdit_12,self.lineEdit_16,self.lineEdit_14,self.lineEdit_21]
        importance=[self.spinBox_13,self.spinBox_17,self.spinBox_18,self.spinBox_19,self.spinBox_20]
        probability=[self.spinBox_16,self.spinBox_15,self.spinBox_11,self.spinBox_14,self.spinBox_12]
        power=[self.label_28,self.label_34,self.label_33,self.label_35,self.label_31]
        res=get_swot_data("strengths")
        for r in res:
            i=r["id"]
            names[i].setText(r["name"])
            actions[i].setText(r["action"])
            importance[i].setValue(r["importance"])
            probability[i].setValue(r["probability"])
            power[i].setText(str(r["power"]))
    
    def set_opportunities(self):
        try:
            names=[self.lineEdit_29,self.lineEdit_30,self.lineEdit_25,self.lineEdit_23,self.lineEdit_28]
            actions=[self.lineEdit_27,self.lineEdit_22,self.lineEdit_26,self.lineEdit_24,self.lineEdit_31]
            importance=[self.spinBox_23,self.spinBox_27,self.spinBox_28,self.spinBox_29,self.spinBox_30]
            probability=[self.spinBox_26,self.spinBox_25,self.spinBox_21,self.spinBox_24,self.spinBox_22]
            power=[self.label_38,self.label_44,self.label_43,self.label_45,self.label_41]
            for i in range(0,5):
                print(i)
                name=names[i].text()
                if(name):
                    action=actions[i].text()
                    imp=importance[i].text()
                    prob=probability[i].text()
                    set_swot_data(i,"opportunities",name,action,imp,prob)

            self.get_opportunities()
        except Exception as e:
            print(e)

    def get_opportunities(self):
        names=[self.lineEdit_29,self.lineEdit_30,self.lineEdit_25,self.lineEdit_23,self.lineEdit_28]
        actions=[self.lineEdit_27,self.lineEdit_22,self.lineEdit_26,self.lineEdit_24,self.lineEdit_31]
        importance=[self.spinBox_23,self.spinBox_27,self.spinBox_28,self.spinBox_29,self.spinBox_30]
        probability=[self.spinBox_26,self.spinBox_25,self.spinBox_21,self.spinBox_24,self.spinBox_22]
        power=[self.label_38,self.label_44,self.label_43,self.label_45,self.label_41]
        res=get_swot_data("opportunities")
        for r in res:
            i=r["id"]
            names[i].setText(r["name"])
            actions[i].setText(r["action"])
            importance[i].setValue(r["importance"])
            probability[i].setValue(r["probability"])
            power[i].setText(str(r["power"]))
    
    def set_threats(self):
        try:
            names=[self.lineEdit_101,self.lineEdit_95,self.lineEdit_102,self.lineEdit_96,self.lineEdit_99]
            actions=[self.lineEdit_103,self.lineEdit_94,self.lineEdit_97,self.lineEdit_98,self.lineEdit_100]
            importance=[self.spinBox_93,self.spinBox_100,self.spinBox_91,self.spinBox_94,self.spinBox_99]
            probability=[self.spinBox_96,self.spinBox_92,self.spinBox_95,self.spinBox_97,self.spinBox_98]
            power=[self.label_144,self.label_148,self.label_147,self.label_142,self.label_143]
            for i in range(0,5):
                print(i)
                name=names[i].text()
                if(name):
                    action=actions[i].text()
                    imp=importance[i].text()
                    prob=probability[i].text()
                    set_swot_data(i,"threats",name,action,imp,prob)

            self.get_threats()
        except Exception as e:
            print(e)

    def get_threats(self):
        names=[self.lineEdit_101,self.lineEdit_95,self.lineEdit_102,self.lineEdit_96,self.lineEdit_99]
        actions=[self.lineEdit_103,self.lineEdit_94,self.lineEdit_97,self.lineEdit_98,self.lineEdit_100]
        importance=[self.spinBox_93,self.spinBox_100,self.spinBox_91,self.spinBox_94,self.spinBox_99]
        probability=[self.spinBox_96,self.spinBox_92,self.spinBox_95,self.spinBox_97,self.spinBox_98]
        power=[self.label_144,self.label_148,self.label_147,self.label_142,self.label_143]
        res=get_swot_data("threats")
        for r in res:
            i=r["id"]
            names[i].setText(r["name"])
            actions[i].setText(r["action"])
            importance[i].setValue(r["importance"])
            probability[i].setValue(r["probability"])
            power[i].setText(str(r["power"]))


    def closeEvent(self, event):
        self.questionThemeComboBox.clear()
        sqlite_connection.commit()

    def choose_project(self):
        print("choose_the_project")
        print(view_all_projects())
        try:
            self.tabWidget.setCurrentIndex(6)
        except Exception as e:
            self.errorTestLabel.setText(str(e))

    def create_project(self):
        print("create_the_project")
        name_project = self.lineEdit.text()
        print(name_project)
        try:
            create_new_project(name_project)
            print(view_all_projects())
        except Exception as e:
            self.errorTestLabel.setText(str(e))

    def view_project(self):
        print("change_project")
        try:
            self.questionThemeComboBox.clear()
            self.questionThemeComboBox.addItems(view_all_projects())
        except Exception as e:
            self.errorTestLabel.setText(str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Main()
    myapp.show()
    sys.exit(app.exec_())
