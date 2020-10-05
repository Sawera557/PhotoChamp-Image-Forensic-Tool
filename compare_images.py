# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare_images.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
# from Select_to_compare import imageA, imageB, diff, thresh
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)



class Ui_CompareMe(QtWidgets.QMainWindow):
    def __init__(self, similarity , path):
        super().__init__()
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 590
        self.height = 345

        self.init_window(similarity, path)

    def init_window(self, similarity, path):
        self.setFixedSize(540, 430)

        self.setWindowTitle("PhotoChamp: Find Differences And Compare")
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))            #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.sim_label = QtWidgets.QLabel(self.centralwidget)
        self.sim_label.setGeometry(QtCore.QRect(10, 0, 110, 40))
        self.sim_label.setMinimumSize(QtCore.QSize(110, 40))
        self.sim_label.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.sim_label.setFont(font)
        self.sim_label.setText("Similarity %")
        self.sim_label.setObjectName("sim_label")
        self.scoreMe = QtWidgets.QLineEdit(self.centralwidget)
        self.scoreMe.setGeometry(QtCore.QRect(120, 10, 411, 33))
        self.scoreMe.setMinimumSize(QtCore.QSize(410, 33))
        self.scoreMe.setMaximumSize(QtCore.QSize(450, 33))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.scoreMe.setFont(font)

        self.scoreMe.setText(similarity+"%")
        self.scoreMe.setPlaceholderText("")
        self.scoreMe.setObjectName("scoreMe")
        self.normal_1 = QtWidgets.QLabel(self.centralwidget)
        self.normal_1.setEnabled(True)
        self.normal_1.setGeometry(QtCore.QRect(10, 60, 258, 148))
        self.normal_1.setMinimumSize(QtCore.QSize(258, 147))
        self.normal_1.setMaximumSize(QtCore.QSize(258, 148))

        self.normal_1.setPixmap(QtGui.QPixmap(os.path.join(path, "normal_1.jpg")))
        self.normal_1.setScaledContents(True)
        self.normal_1.setObjectName("normal_1")
        self.normal_2 = QtWidgets.QLabel(self.centralwidget)
        self.normal_2.setEnabled(True)
        self.normal_2.setGeometry(QtCore.QRect(10, 221, 258, 147))
        self.normal_2.setMinimumSize(QtCore.QSize(258, 147))
        self.normal_2.setMaximumSize(QtCore.QSize(258, 148))

        self.normal_2.setPixmap(QtGui.QPixmap(os.path.join(path, "normal_2.jpg")))
        self.normal_2.setScaledContents(True)
        self.normal_2.setObjectName("normal_2")
        self.grey1 = QtWidgets.QLabel(self.centralwidget)
        self.grey1.setEnabled(True)
        self.grey1.setGeometry(QtCore.QRect(270, 60, 258, 148))
        self.grey1.setMinimumSize(QtCore.QSize(258, 147))
        self.grey1.setMaximumSize(QtCore.QSize(258, 148))

        self.grey1.setPixmap(QtGui.QPixmap(os.path.join(path, "grey_1.png")))
        self.grey1.setScaledContents(True)
        self.grey1.setObjectName("grey1")
        self.grey2 = QtWidgets.QLabel(self.centralwidget)
        self.grey2.setEnabled(True)
        self.grey2.setGeometry(QtCore.QRect(270, 221, 258, 147))
        self.grey2.setMinimumSize(QtCore.QSize(258, 147))
        self.grey2.setMaximumSize(QtCore.QSize(258, 148))
        
        self.grey2.setPixmap(QtGui.QPixmap(os.path.join(path, "grey_2.png")))
        self.grey2.setScaledContents(True)
        self.grey2.setObjectName("grey2")

        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(350, 380, 75, 23))
        self.Quit.setToolTip("Click to Exit Program!")
        self.Quit.setText("Quit")
        self.Quit.setObjectName("Quit")
        self.Quit.clicked.connect(self.close_main_window)


        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(270, 380, 75, 23))
        self.back.setToolTip("")
        self.back.setText("Back")
        self.back.setObjectName("back")
        self.back.clicked.connect(self.back_to_Main)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)



    @pyqtSlot()
    def back_to_Main(self):
        from Select_to_compare import TestDifference
        self.TestAgain = TestDifference()
        self.TestAgain.show()
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
    CompareMe = QtWidgets.QMainWindow()
    ui = Ui_CompareMe(similarity, path)
    #ui.setupUi(CompareMe, similarity, path)
    #CompareMe.show()
    sys.exit(app.exec_())
'''