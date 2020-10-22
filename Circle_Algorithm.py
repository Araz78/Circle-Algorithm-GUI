from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import os

plt.style.use('seaborn-whitegrid')
#=========================================== Create directory 
def create_folder():
    try:
        directory = "Charts"
        parent_dir = ""
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
    except:
        pass
#=========================================== GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(972, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.value_of_r = QtWidgets.QLineEdit(self.centralwidget)
        self.value_of_r.setGeometry(QtCore.QRect(672, 131, 141, 41))
        self.value_of_r.setObjectName("value_of_r")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(830, 140, 131, 31))
        self.label.setObjectName("label")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(830, 200, 131, 34))
        self.btn_run.setObjectName("btn_run")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(11, 0, 641, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.pic_eighth_quarter = QtWidgets.QLabel(self.tab_8)
        self.pic_eighth_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_eighth_quarter.setStyleSheet("")
        self.pic_eighth_quarter.setText("")
        self.pic_eighth_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_eighth_quarter.setObjectName("pic_eighth_quarter")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pic_seventh_quarter = QtWidgets.QLabel(self.tab_7)
        self.pic_seventh_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_seventh_quarter.setStyleSheet("")
        self.pic_seventh_quarter.setText("")
        self.pic_seventh_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_seventh_quarter.setObjectName("pic_seventh_quarter")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pic_sixth_quarter = QtWidgets.QLabel(self.tab_6)
        self.pic_sixth_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_sixth_quarter.setStyleSheet("")
        self.pic_sixth_quarter.setText("")
        self.pic_sixth_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_sixth_quarter.setObjectName("pic_sixth_quarter")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pic_fifth_quarter = QtWidgets.QLabel(self.tab_5)
        self.pic_fifth_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_fifth_quarter.setStyleSheet("")
        self.pic_fifth_quarter.setText("")
        self.pic_fifth_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_fifth_quarter.setObjectName("pic_fifth_quarter")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pic_fourth_quarter = QtWidgets.QLabel(self.tab_4)
        self.pic_fourth_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_fourth_quarter.setStyleSheet("")
        self.pic_fourth_quarter.setText("")
        self.pic_fourth_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_fourth_quarter.setObjectName("pic_fourth_quarter")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pic_third_quarter = QtWidgets.QLabel(self.tab_3)
        self.pic_third_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_third_quarter.setStyleSheet("")
        self.pic_third_quarter.setText("")
        self.pic_third_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_third_quarter.setObjectName("pic_third_quarter")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pic_second_quarter = QtWidgets.QLabel(self.tab_2)
        self.pic_second_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_second_quarter.setStyleSheet("")
        self.pic_second_quarter.setText("")
        self.pic_second_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_second_quarter.setObjectName("pic_second_quarter")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.pic_first_quarter = QtWidgets.QLabel(self.tab_1)
        self.pic_first_quarter.setGeometry(QtCore.QRect(0, 0, 641, 371))
        self.pic_first_quarter.setStyleSheet("")
        self.pic_first_quarter.setText("")
        self.pic_first_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_first_quarter.setObjectName("pic_first_quarter")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pic_all_quarter = QtWidgets.QLabel(self.tab)
        self.pic_all_quarter.setGeometry(QtCore.QRect(0, 0, 641, 361))
        self.pic_all_quarter.setStyleSheet("")
        self.pic_all_quarter.setText("")
        self.pic_all_quarter.setPixmap(QtGui.QPixmap("white.png"))
        self.pic_all_quarter.setObjectName("pic_all_quarter")
        self.tabWidget.addTab(self.tab, "")
        self.txt_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_log.setGeometry(QtCore.QRect(0, 420, 971, 101))
        self.txt_log.setObjectName("txt_log")
        self.txt_log.append("لطفا مقدار وتر را وارد کنید.")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(670, 200, 131, 34))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(8)
        self.btn_run.clicked.connect(self.get_value_of_r)
        self.btn_clear.clicked.connect(self.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        create_folder()

    def clear(self):
        self.value_of_r.clear()
        self.txt_log.clear()
        self.txt_log.append("لطفا مقدار وتر را وارد کنید.")
        self.pic_all_quarter.clear()
        self.pic_first_quarter.clear()
        self.pic_second_quarter.clear()
        self.pic_third_quarter.clear()
        self.pic_fourth_quarter.clear()
        self.pic_fifth_quarter.clear()
        self.pic_sixth_quarter.clear()
        self.pic_seventh_quarter.clear()
        self.pic_eighth_quarter.clear()
        
        import shutil
        path = "Charts"
        shutil.rmtree(path)
        create_folder()


    def get_value_of_r(self):
        #=========================================== Geting value from gui
        r = int(self.value_of_r.text())
        #=========================================== Calculate the value of P0
        P0 = 1 - r
        #=========================================== Insert the values ​​of X_k, Y_k, P_k
        X_k = []
        X_k.append(0)
        
        Y_k = []
        Y_k.append(r)

        P_k = []
        P_k.append(P0)

        i = 0
        while X_k[i] <= Y_k[i]:
            if P_k[i] < 0:
                new_pk = (P_k[i] + ((2 * (X_k[i] + 1)) + 1))
                P_k.append(new_pk)
                X_k.append(1 + X_k[i])
                Y_k.append(Y_k[i])
                i+=1

            else:
                new_pk = ((P_k[i] + ((2 * (X_k[i] + 1)) + 1)) - (2 * (Y_k[i] - 1)))
                P_k.append(new_pk)
                X_k.append(1 + X_k[i])
                Y_k.append(Y_k[i] - 1)
                i+=1
        #=========================================== Clear extra numbers and negative X_k and Y_k
        xk = X_k[i]
        yk = Y_k[i]
        pk = P_k[i]
        X_k.remove(xk)
        Y_k.remove(yk)
        P_k.remove(pk)

        X_k_negative = [ -x for x in X_k]
        Y_k_negative = [ -y for y in Y_k]
        #=========================================== Draw First Quarter
        plt.plot(X_k, Y_k, 'o', color='red')
        plt.savefig('Charts/01-First Quarter.png')
        #=========================================== Draw Second Quarter
        plt.plot(Y_k, X_k, 'o', color='red')
        plt.savefig('Charts/02-Second Quarter.png')
        #=========================================== Draw Third Quarter
        plt.plot(Y_k_negative, X_k, 'o', color='red')
        plt.savefig('Charts/03-Third Quarter.png')
        #=========================================== Draw Fourth Quarter
        plt.plot(X_k_negative, Y_k, 'o', color='red')
        plt.savefig('Charts/04-Fourth Quarter.png')
        #=========================================== Draw Fifth Quarter
        plt.plot(X_k_negative, Y_k_negative, 'o', color='red')
        plt.savefig('Charts/05-Fifth Quarter.png')
        #=========================================== Draw Sixth Quarter
        plt.plot(Y_k_negative, X_k_negative, 'o', color='red')
        plt.savefig('Charts/06-Sixth Quarter.png')
        #=========================================== Draw Seventh Quarter
        plt.plot(Y_k, X_k_negative, 'o', color='red')
        plt.savefig('Charts/07-Seventh Quarter.png')
        #=========================================== Draw Eighth Quarter
        plt.plot(X_k, Y_k_negative, 'o', color='red')
        plt.savefig('Charts/08-Eighth Quarter.png')
        #=========================================== Draw All Quarter
        plt.plot(X_k, Y_k,Y_k,X_k,Y_k_negative,X_k,X_k_negative,Y_k,X_k_negative,Y_k_negative,Y_k_negative,X_k_negative,Y_k,X_k_negative,X_k,Y_k_negative, 'o', color='red')
        plt.savefig('Charts/00-All Quarter.png')
        self.txt_log.clear()
        self.txt_log.append("مختصصات شما رسم گردید.")

        #=========================================== Show pic's in Tab's
        self.pic_all_quarter.setPixmap(QtGui.QPixmap("Charts/00-All Quarter.png"))
        self.pic_first_quarter.setPixmap(QtGui.QPixmap("Charts/01-First Quarter.png"))
        self.pic_second_quarter.setPixmap(QtGui.QPixmap("Charts/02-Second Quarter.png"))
        self.pic_third_quarter.setPixmap(QtGui.QPixmap("Charts/03-Third Quarter.png"))
        self.pic_fourth_quarter.setPixmap(QtGui.QPixmap("Charts/04-Fourth Quarter.png"))
        self.pic_fifth_quarter.setPixmap(QtGui.QPixmap("Charts/05-Fifth Quarter.png"))
        self.pic_sixth_quarter.setPixmap(QtGui.QPixmap("Charts/06-Sixth Quarter.png"))
        self.pic_seventh_quarter.setPixmap(QtGui.QPixmap("Charts/07-Seventh Quarter.png"))
        self.pic_eighth_quarter.setPixmap(QtGui.QPixmap("Charts/08-Eighth Quarter.png"))
        
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "مقدار وتر (r) را وارد کنید :"))
        self.btn_run.setText(_translate("MainWindow", "محاسبه کن"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "ربع هشتم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "ربع هفتم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "ربع ششم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "ربع پنجم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ربع چهارم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ربع سوم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ربع دوم"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "ربع اول"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "تمام ربع ها"))
        self.btn_clear.setText(_translate("MainWindow", "پاک کن"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
