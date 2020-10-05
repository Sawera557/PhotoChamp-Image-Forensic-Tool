# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

#from car_detection import Test_Car_window


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)


class Result_Car(QtWidgets.QMainWindow):
    def __init__(self, image_path, output, result):
        super().__init__()
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 590
        self.height = 345
        #self.Main_window = QtWidgets.QMainWindow()
        self.init_window(image_path, output, result)


    def init_window(self, image_path, output, result):
        self.setFixedSize(540, 430)

        self.setWindowTitle("PhotoChamp: Find Differences And Compare")
        self.setWindowIcon(QtGui.QIcon(
           "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.show_car = QtWidgets.QLabel(self.centralwidget)
        self.show_car.setEnabled(True)
        self.show_car.setGeometry(QtCore.QRect(10, 80, 520, 295))
        self.show_car.setMinimumSize(QtCore.QSize(520, 295))
        self.show_car.setMaximumSize(QtCore.QSize(520, 295))
        self.show_car.setToolTip("")
        self.show_car.setStatusTip("")
        self.show_car.setWhatsThis("")
        self.show_car.setAccessibleName("")
        self.show_car.setAccessibleDescription("")
        self.show_car.setText("")
        self.show_car.setPixmap(QtGui.QPixmap(image_path))
        self.show_car.setScaledContents(True)
        self.show_car.setObjectName("show_car")
        self.result_car = QtWidgets.QLineEdit(self.centralwidget)
        self.result_car.setGeometry(QtCore.QRect(120, 0, 410, 33))
        self.result_car.setMinimumSize(QtCore.QSize(410, 30))
        self.result_car.setMaximumSize(QtCore.QSize(450, 33))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.result_car.setFont(font)
        self.result_car.setMouseTracking(False)
        self.result_car.setAcceptDrops(False)
        self.result_car.setToolTip("")
        self.result_car.setStatusTip("")
        self.result_car.setWhatsThis("")
        self.result_car.setAccessibleName("")
        self.result_car.setAccessibleDescription("")
        self.result_car.setInputMask(result)
        self.result_car.setText(result)
        self.result_car.setReadOnly(True)
        self.result_car.setObjectName("result_car")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(10, 0, 110, 40))
        self.result_label.setMinimumSize(QtCore.QSize(110, 40))
        self.result_label.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.result_label.setFont(font)
        self.result_label.setToolTip("")
        self.result_label.setStatusTip("")
        self.result_label.setWhatsThis("")
        self.result_label.setAccessibleName("")
        self.result_label.setAccessibleDescription("")
        self.result_label.setText("Result")
        self.result_label.setObjectName("result_label")
        self.result_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.result_label_2.setGeometry(QtCore.QRect(10, 40, 110, 40))
        self.result_label_2.setMinimumSize(QtCore.QSize(110, 40))
        self.result_label_2.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.result_label_2.setFont(font)
        self.result_label_2.setToolTip("")
        self.result_label_2.setStatusTip("")
        self.result_label_2.setWhatsThis("")
        self.result_label_2.setAccessibleName("")
        self.result_label_2.setAccessibleDescription("")
        self.result_label_2.setText("Resemblence %")
        self.result_label_2.setObjectName("result_label_2")
        self.result_class = QtWidgets.QLineEdit(self.centralwidget)
        self.result_class.setGeometry(QtCore.QRect(120, 40, 411, 33))
        self.result_class.setMinimumSize(QtCore.QSize(410, 33))
        self.result_class.setMaximumSize(QtCore.QSize(450, 33))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.result_class.setFont(font)
        self.result_class.setToolTip("")
        self.result_class.setStatusTip("")
        self.result_class.setWhatsThis("")
        self.result_class.setAccessibleName("")
        self.result_class.setAccessibleDescription("")
        self.result_class.setInputMask(output)
        self.result_class.setText(output)
        self.result_class.setObjectName("result_class")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(270, 380, 75, 23))
        self.Back.setToolTip("")
        self.Back.setStatusTip("")
        self.Back.setWhatsThis("")
        self.Back.setAccessibleName("")
        self.Back.setAccessibleDescription("")
        self.Back.setText("Back")
        self.Back.setObjectName("Back")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setToolTip("<h5>Close the program!<h5>")  # Notice using h2 tags From Html
        self.Quit.setIcon(QtGui.QIcon(
            "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\cancel-symbol-transparent-9.png"))  # icon Pic File name
        self.Quit.setGeometry(QtCore.QRect(360, 380, 75, 23))
        self.Quit.setText("Quit")
        self.Quit.setObjectName("Quit")
        self.Back.clicked.connect(self.back_to_Main)
        self.Quit.clicked.connect(self.close_main_window)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.show()
        #MainWindow.setStatusBar(self.statusbar)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)


    @pyqtSlot()
    def back_to_Main(self):
        from car_detection import Test_Car_window
        self.Test_Again_window = Test_Car_window()
        self.Test_Again_window.show()
        self.close()


    @pyqtSlot()
    def closex(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)
        if reply == QMessageBox.Yes:
            self.close()


    @pyqtSlot()
    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit?",
                QMessageBox.Close | QMessageBox.Cancel)

            if reply == QMessageBox.Close:
                self.close()

    @pyqtSlot()
    def close_main_window(self):
        """
           Generate 'question' dialog on clicking 'X' button in title bar.
           Reimplement the closeEvent() event handler to include a 'Question'
           dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            self.close()
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''