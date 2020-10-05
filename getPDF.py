import os
import sys

import PyPDF2
#from PIL import Image, ImageChops, ImageEnhance
from PDF_JS_view import WindowPDF
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QComboBox, QLineEdit, QLabel, QPushButton, QWidget, \
    QMessageBox
from multiprocessing import freeze_support




def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\FYP-3\PhotoChampEXE\media\Icons")

    return os.path.join(base_path, relative_path)


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size1(file_path):
    """
    this function will return the file size
    """
    pass
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


class PDF_window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 345
        self.file_path = ""
        self.init_window()

    def init_window(self):
        """initialize window"""
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))         # "D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//icon.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)

        # quit = QAction("Quit", self)
        # quit.triggered.connect(self.closex)

        # Label
        label = QLabel(self)
        label.move(10, 44)
        label.setText('Image Name ')
        label.setFont(QtGui.QFont("verdana", 7))

        # text Box
        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(True)
        self.line_edit.setFont(QtGui.QFont("verdana", 8))
        self.line_edit.setGeometry(QRect(80, 40, 365, 20))
        self.line_edit.setPlaceholderText("image Name here!")

        # Button
        self.button = QPushButton("Browse", self)
        self.button.setGeometry(QRect(450, 40, 90, 20))
        self.button.setToolTip(
            "<h5>Browse image from your computer to start test!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('698831-icon-105-folder-add-512.png')))         #"D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//698831-icon-105-folder-add-512.png"))icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.getfiles)

        # Button
        self.button = QPushButton("Test", self)
        self.button.setGeometry(QRect(270, 310, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('698827-icon-101-folder-search-512.png')))     #"D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//698827-icon-101-folder-search-512.png"))  # icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.on_click)

        # Button
        self.button = QPushButton("Back", self)
        self.button.setGeometry(QRect(180, 310, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('repeat-pngrepo-com.png')))   #"repeat-pngrepo-com.png"))   icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.back_to_Main)

        # Button
        self.button = QPushButton(" Quit", self)
        self.button.setGeometry(QRect(360, 310, 90, 20))
        self.button.setToolTip("<h5>Close the program!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('cancel-symbol-transparent-9.png')))    #"D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//cancel-symbol-transparent-9.png"))  # icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.close_main_window)

        # Button
        # self.button = QPushButton("Help", self)
        # self.button.setGeometry(QRect(450, 310, 90, 20))
        # self.button.setToolTip("<h5>Help!<h5>")  # Notice using h2 tags From Html
        # self.button.setIcon(QtGui.QIcon("icons8-faq-100 (1).png")) #icon Pic File name
        # self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        # self.button.clicked.connect(self.on_click_help)

        label = QLabel(self)
        label.setText('Model ')
        label.setFont(QtGui.QFont("verdana", 8))
        label.move(10, 20)

        self.combo = QComboBox(self)
        self.combo.addItem("View PDF")

        self.combo.setGeometry(QRect(80, 15, 460, 20))

        label = QLabel(self)
        label.setText('File Informations')
        label.setFont(QtGui.QFont("verdana", 10))
        label.move(50, 75)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topleft.setGeometry(QRect(10, 90, 175, 200))

        label = QLabel(self)
        label.setText('PDF')
        label.setFont(QtGui.QFont("verdana", 10))
        label.move(290, 75)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topleft.setGeometry(QRect(200, 90, 200, 200))

        self.show()

    @pyqtSlot()
    def back_to_Main(self):
        from Model_menu import ModelMenu_Window
        self.Model_menu = ModelMenu_Window()
        self.Model_menu.show()
        self.close()


    @pyqtSlot()
    def getfiles(self):
        fileName, extention = QFileDialog.getOpenFileName(self, 'Single File', 'C:\\', "*.pdf ")
        self.file_path = fileName
        if self.file_path != "":
            head, tail = os.path.split(fileName)
            self.line_edit.setText(tail)
            self.label.hide()
            self.label2.hide()
            self.label3.hide()
            self.label4.hide()
            self.label_1.hide()
            self.label_2.hide()

            self.label_1.move(410, 125)
            self.label_1.setText('and please wait...')
            self.label_1.setFont(QtGui.QFont("verdana", 11))

            self.label_2.move(410, 100)
            self.label_2.setText('Click View PDF')
            self.label_2.setFont(QtGui.QFont("verdana", 11))

            pixmap = QPixmap('D:\\FYP-3\\Material\\pdf.png')
            self.label.setPixmap(pixmap)
            self.label.resize(190, 190)
            self.label.move(205, 95)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))

            name = "FileName: " + str(tail)
            self.label2.setText(name)
            self.label2.setFont(QtGui.QFont("verdana", 8))
            self.label2.move(15, 100)

            # PDF information
            pdfFileObj = open(self.file_path, 'rb')
            # creating a pdf reader object
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # printing number of pages in pdf file
            pages = pdfReader.numPages
            page2 = "PDF ToTal pages: " + str(pages)
            self.label3.setText(page2)
            self.label3.setFont(QtGui.QFont("verdana", 8))
            self.label3.move(15, 112)

            size = file_size1(self.file_path)
            file_size = "PDF Size: " + str(size)
            self.label4.setText(file_size)
            self.label4.setFont(QtGui.QFont("verdana", 8))
            self.label4.move(15, 124)

            self.label_1.show()
            self.label_2.show()
            self.label2.show()
            self.label3.show()
            self.label4.show()
            self.label.show()
        else:
            pass

    @pyqtSlot()
    def on_click(self):
        if self.file_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose image from your computer !")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon(resource_path('icons8-cbs-512.ico')))         #   "D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//icons8-cbs-512.ico"))
            msg.exec_()
        else:
            if str(self.combo.currentText()) == "View PDF":
                self.result_window = WindowPDF(self.file_path)
                self.result_window.show()

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
    window = PDF_window()
    sys.exit(App.exec())
