# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BR.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import csv
from collections import KeysView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5.QtWidgets import QMessageBox


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def retrive_history_all(self):
        keys = {}.keys()
        isinstance(keys, KeysView)
        issubclass(type(keys), KeysView)
        type(keys) is KeysView
        type(keys).__mro__

        import browserhistory as bh

        dict_obj = bh.get_browserhistory()
        dict_obj.keys()
        #dict_keys(['safari', 'chrome', 'firefox'])
        #dict_obj['chrome'][1]
        bh.write_browserhistory_csv()

    def write_chromehistory_csv(self) -> None:
        """It writes csv files that contain the browser history in
        the current working directory. It will writes csv files base on
        the name of browsers the program detects."""
        import browserhistory as bh
        browserhistory = bh.get_browserhistory()
        for chrome, history in browserhistory.items():
            with open('chrome' + '_history.csv', mode='w', encoding='utf-8', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',',
                                        quoting=csv.QUOTE_ALL)
                for data in history:
                    csv_writer.writerow(data)

    def write_firefoxhistory_csv(self) -> None:
        """It writes csv files that contain the browser history in
        the current working directory. It will writes csv files base on
        the name of browsers the program detects."""
        import browserhistory as bh
        browserhistory = bh.get_browserhistory()
        for firefox, history in browserhistory.items():
            with open('firefox' + '_history.csv', mode='w', encoding='utf-8', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',',
                                        quoting=csv.QUOTE_ALL)
                for data in history:
                    csv_writer.writerow(data)



class Ui_Browser_History(QtWidgets.QMainWindow):
    def Get_History(self, MainWindow):
        #MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(548, 367)
        MainWindow.setWindowTitle("PhotoChamp IFT App")
        MainWindow.setWindowIcon(QtGui.QIcon(
            "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 461, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("All Browsers")
        self.comboBox.addItem("Google Chrome")
        self.comboBox.addItem("Mozilla Firefox")
        self.label_browser = QtWidgets.QLabel(self.centralwidget)
        self.label_browser.setGeometry(QtCore.QRect(10, 30, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.label_browser.setFont(font)
        self.label_browser.setText("Browser")
        self.label_browser.setObjectName("label_browser")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 290, 521, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")
        self.pic_br = QtWidgets.QLabel(self.centralwidget)
        self.pic_br.setGeometry(QtCore.QRect(300, 70, 191, 191))
        self.pic_br.setPixmap(QtGui.QPixmap(""))
        self.pic_br.setScaledContents(True)
        self.pic_br.setObjectName("pic_br")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.Back.setText("Back")
        self.Back.setObjectName("Back")
        self.Back.clicked.connect(self.back_to_Main)
        self.Back.clicked.connect(lambda: MainWindow.close())

        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.Quit.setText("Quit")
        self.Quit.setObjectName("Quit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 461, 16))
        font = QtGui.QFont()
        font.setPointSize(9)

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(10, 30, 451, 120))
        self.result_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.result_label_1.setGeometry(QtCore.QRect(10, 30, 451, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(30)
        self.result_label.setFont(font)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.result_label_1.setFont(font)
        self.result_label_1.setFont(font)
        self.result_label_1.setObjectName("result_label_1")
        self.result_label.hide()
        self.result_label_1.hide()
        self.label_4.setText("Choose browser to load and write broswer history in csv file")
        self.label_4.setObjectName("label_4")
        self.get = QtWidgets.QPushButton(self.centralwidget)
        self.get.setGeometry(QtCore.QRect(240, 320, 75, 23))
        self.get.setText("Get History")
        self.get.setObjectName("get")
        self.get.clicked.connect(self.download)
        self.get.clicked.connect(self.on_click)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)


    def on_click(self):
        if str(self.comboBox.currentText()) == "All Browsers":
            self.pic_br.setPixmap(QtGui.QPixmap("D:\\FYP-3\\Material\\img.png"))
            self.pic_br.setGeometry(QtCore.QRect(230, 70, 300, 191))
            self.myThread = Thread()
            self.myThread.retrive_history_all()
            self.myThread.start()
            self.result_label.setText("Browser history")
            self.result_label_1.setText("retrieved for All...")
            self.result_label.show()
            self.result_label_1.show()
        elif str(self.comboBox.currentText()) == "Google Chrome":
            self.pic_br.setPixmap(QtGui.QPixmap("D:/High Accyracy Models Final/chrom.png"))
            self.myThread = Thread()
            self.myThread.write_chromehistory_csv()
            self.myThread.start()
            self.result_label.setText("Browser history")
            self.result_label_1.setText("retrieved for chrome...")
            self.result_label.show()
            self.result_label_1.show()
        elif str(self.comboBox.currentText()) == "Mozilla Firefox":
            self.pic_br.setPixmap(QtGui.QPixmap("D:\FYP-3\Material\Firefox_Logo,_2017.png"))
            self.myThread = Thread()
            self.myThread.write_firefoxhistory_csv()
            self.myThread.start()
            self.result_label.setText("Browser history")
            self.result_label_1.setText("retrieved for firefox...")
            self.result_label.show()
            self.result_label_1.show()

    def back_to_Main(self, metaExtract_window):
        from Model_menu import ModelMenu_Window
        self.Model_menu = ModelMenu_Window()
        self.Model_menu.show()
        self.close()


    def close_main_window(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Browser_History()
    ui.Get_History(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
