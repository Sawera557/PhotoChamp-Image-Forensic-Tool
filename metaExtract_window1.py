# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class Ui_metaExtract_window(QtWidgets.QMainWindow):
    def __init__(self, metaExtract_window, tags, lat, lon, date, dataPil):
        super().__init__()
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 590
        self.height = 345

        self.init_window(metaExtract_window, tags, lat, lon, date, dataPil)
        #self.metaExtract_window = QtWidgets.QMainWindow()
        #self.metaExtract_window.init_window(self)
        self.show()
        #self.metaExtract_window.Quit.clicked.connect(self.close_main_window)

    def init_window(self, metaExtract_window, tags, lat, lon, date, dataPil):
        metaExtract_window.setWindowTitle("PhotoChamp IFT App")
        metaExtract_window.setWindowIcon(QtGui.QIcon(
            "D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name
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
        #self.Back.clicked.connect(self.back_to_Main)

        self.Quit = QtWidgets.QPushButton(metaExtract_window)
        self.Quit.setGeometry(QtCore.QRect(340, 410, 101, 23))
        self.Quit.setText("Quit")
        self.Quit.setShortcut("")
        self.Quit.setObjectName("Quit")
        #self.Quit.clicked.connect(self.close_main_window)
        QtCore.QMetaObject.connectSlotsByName(metaExtract_window)

    @pyqtSlot()
    def back_to_Main(metaExtract_window):
        from Test_window_Final import Test_window
        metaExtract_window.Back_TO_Test = Test_window()
        metaExtract_window.Back_TO_Test.show()
        metaExtract_window.close()

    @pyqtSlot()
    def close_main_window(metaExtract_window):
        reply = QMessageBox.question(metaExtract_window, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            metaExtract_window.close()

