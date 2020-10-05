# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)


class Ui_metaExtract_window(QtWidgets.QMainWindow):
    def Extract_metadata(self, metaExtract_window, tags, lat, lon, date, dataPil):
        metaExtract_window.setWindowTitle("PhotoChamp IFT App")
        metaExtract_window.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))              #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name
        metaExtract_window.setObjectName("metaExtract_window")
        metaExtract_window.setFixedSize(674, 441)

        #metaExtract_window.setMinimumSize(QtCore.QSize(674, 441))
        #metaExtract_window.setMaximumSize(QtCore.QSize(674, 441))
        self.label = QtWidgets.QLabel(metaExtract_window)
        self.label.setGeometry(QtCore.QRect(180, 0, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("MetaData Extraction WIndow")
        self.label.setObjectName("label")
        self.metadata1 = QtWidgets.QScrollArea(metaExtract_window)
        self.metadata1.setGeometry(QtCore.QRect(10, 60, 321, 341))
        self.metadata1.setAccessibleName("")
        self.metadata1.setAccessibleDescription("")
        self.metadata1.setWidgetResizable(True)
        self.metadata1.setObjectName("metadata1")
        self.exif1 = QtWidgets.QWidget()
        self.exif1.setGeometry(QtCore.QRect(0, 0, 319, 339))
        self.exif1.setObjectName("exif1")
        self.data1 = QtWidgets.QPlainTextEdit(self.exif1)
        self.data1.setGeometry(QtCore.QRect(0, 0, 321, 341))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data1.setFont(font)
        self.data1.setReadOnly(True)
        self.data1.setDocumentTitle("")
        self.data1.setPlainText(str(
            "Latitude in Degrees : " + str(lat) + '\n' + "Longitude in Degrees : " + str(
                lon) + '\n' + "Date and Time : " + str(date)))
        try:
            self.data1.appendPlainText(str('\n'.join(dataPil)))
        except:
            self.data1.appendPlainText(str(dataPil))
        #finally:
            #self.data1.appendPlainText("Could not be extracted")
        self.data1.setObjectName("data1")
        self.metadata1.setWidget(self.exif1)
        self.metadata2 = QtWidgets.QScrollArea(metaExtract_window)
        self.metadata2.setGeometry(QtCore.QRect(340, 60, 321, 341))
        self.metadata2.setWidgetResizable(True)
        self.metadata2.setObjectName("metadata2")
        self.exif2 = QtWidgets.QWidget()
        self.exif2.setGeometry(QtCore.QRect(0, 0, 319, 339))
        self.exif2.setObjectName("exif2")
        self.data2 = QtWidgets.QPlainTextEdit(self.exif2)
        self.data2.setGeometry(QtCore.QRect(0, 0, 321, 341))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.data2.setFont(font)
        self.data2.setDocumentTitle("")
        self.data2.setReadOnly(True)
        self.data2.setPlainText(str('\n'.join(tags)))
        self.data2.setObjectName("data2")
        self.metadata2.setWidget(self.exif2)
        self.Back = QtWidgets.QPushButton(metaExtract_window)
        self.Back.setGeometry(QtCore.QRect(234, 410, 101, 23))
        self.Back.setText("Back")
        self.Back.setShortcut("")
        self.Back.setObjectName("Back")
        self.Back.clicked.connect(self.back_to_Main)
        self.Back.clicked.connect(lambda: metaExtract_window.close())
        self.Quit = QtWidgets.QPushButton(metaExtract_window)
        self.Quit.setGeometry(QtCore.QRect(340, 410, 101, 23))
        self.Quit.setText("Quit")
        self.Quit.setShortcut("")
        self.Quit.setObjectName("Quit")
        self.Quit.clicked.connect(self.close_main_window)
        self.Quit.clicked.connect(lambda: metaExtract_window.close())
        #self.show()
        QtCore.QMetaObject.connectSlotsByName(metaExtract_window)


    def back_to_Main(self, metaExtract_window):
        from Test_window_Final import Test_window
        self.Back_TO_Test = Test_window()
        self.Back_TO_Test.show()
        self.close()


    def close_main_window(self):
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            self.close()