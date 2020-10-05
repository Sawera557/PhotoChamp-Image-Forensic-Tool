# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subtitlesui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from datetime import timedelta

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QFileDialog
from multiprocessing import freeze_support
from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)




class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def download_Subtitle_func(self, video_path):
        # configure the cache
        region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
        # scan for videos newer than 2 weeks and their existing subtitles in a folder
        videos = scan_videos(video_path, age=timedelta())
        # download best subtitles
        subtitles = download_best_subtitles(videos, {Language('eng')})
        # save them to disk, next to the video
        for v in videos:
            save_subtitles(v, subtitles[v])


class Download_subtitles(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 590
        self.height = 345
        self.file_path = ""
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))            #"D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.path_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_edit.setGeometry(QtCore.QRect(100, 20, 381, 31))
        self.path_edit.setText("")
        self.path_edit.setPlaceholderText("C:\\Users\\Laptop\\Videos\\Money Heist")
        self.path_edit.setObjectName("path_edit")

        self.browse_b1 = QtWidgets.QPushButton(self.centralwidget)
        self.browse_b1.setGeometry(QtCore.QRect(484, 20, 91, 31))
        self.browse_b1.setText("Browse")
        self.browse_b1.setObjectName("browse_b1")
        self.browse_b1.clicked.connect(self.getfiles)

        self.video_labl = QtWidgets.QLabel(self.centralwidget)
        self.video_labl.setGeometry(QtCore.QRect(10, 20, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.video_labl.setFont(font)
        self.video_labl.setText("Videos Folder ")
        self.video_labl.setObjectName("video_labl")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setGeometry(QtCore.QRect(10, 40, 41, 20))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.video_label.setFont(font)
        self.video_label.setText("Path")
        self.video_label.setObjectName("video_label")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 270, 571, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 310, 91, 23))
        self.back.setText("Back")
        self.back.setObjectName("back")
        self.back.clicked.connect(self.back_to_Main)

        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(350, 310, 91, 23))
        self.quit.setText("Quit")
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.close_main_window)

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(100, 80, 451, 181))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.result_label.setFont(font)
        # self.result_label.setText("Subtitles found successfully...")
        self.result_label.setObjectName("result_label")

        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(260, 310, 91, 23))
        self.find.setText("Find")
        self.find.setObjectName("find")
        self.find.clicked.connect(self.download)
        self.find.clicked.connect(self.on_click)

        '''
        Find_Subtitles_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Find_Subtitles_window)
        self.statusbar.setObjectName("statusbar")
        Find_Subtitles_window.setStatusBar(self.statusbar)
        #QtCore.QMetaObject.connectSlotsByName(Find_Subtitles_window)
        '''
        self.show()

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progressBar.setValue(self.completed)

    @pyqtSlot()
    def back_to_Main(self):
        from Model_menu import ModelMenu_Window
        self.Model_menu = ModelMenu_Window()
        self.Model_menu.show()
        self.close()

    @pyqtSlot()
    def getfiles(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Single Dir', 'D:\Movies\Money heist\Season 01')
        # getOpenFileName(self, 'Single File', 'C:\'' "*.png *.xpm *.jpg *.tiff *.jpg *.bmp")
        self.file_path = fileName
        if self.file_path != "":
            # head, tail = os.path.split(fileName)
            self.path_edit.setText(fileName)
            self.result_label.hide()

            self.result_label.setText("Click Find And Please wait...")
            self.result_label.show()
        else:
            pass

    @pyqtSlot()
    def on_click(self):
        if self.file_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose image from your computer !")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))                #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
            msg.exec_()
        else:
            self.myThread = Thread()
            self.myThread.download_Subtitle_func(self.file_path)
            self.myThread.start()
            self.result_label.setText("Subtitles found successfully...")
            self.result_label.show()

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


if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    freeze_support()
    window = Download_subtitles()
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())
