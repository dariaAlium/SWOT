from PyQt5 import uic
from PyQt5 import QtWidgets
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
        try:
            self.pushButton.clicked.connect(self.set_weakness)
            self.questionThemeComboBox.addItems(view_all_projects())
            self.questionThemeComboBox.currentIndexChanged.connect(self.choose_project)
            self.themeTestButton.clicked.connect(self.view_project)
            self.genetalTestButton.clicked.connect(self.create_project)
        except Exception as e:
            print(e)

        self.show()

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
