# -*- coding: utf-8 -*-

import os

import cv2
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
# Form implementation generated from reading ui file 'Select_to_compare.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox
from compare_images import *
from skimage.metrics import structural_similarity

from compare_images import Ui_CompareMe


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\FYP-3\PhotoChampEXE\media\Icons")

    return os.path.join(base_path, relative_path)  #resource_path('icon.png')))



class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def find_Difference(self, file_path1, file_path2):
        # load the two input images
        imageA = cv2.imread(file_path1)
        imageB = cv2.imread(file_path2)
        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        # compute the Structural Similarity Index (SSIM) between the two
        # images, ensuring that the difference image is returned
        (score, diff) = structural_similarity(grayA, grayB, full=True)
        #print(diff)
        similarity = str(score * 100)
        diff = (diff * 255).astype("uint8")

        # threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # loop over the contours
        for c in cnts:
            # compute the bounding box of the contour and then draw the
            # bounding box on both input images to represent where the two
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # show the output images
        #cv2.imshow('', imageA)
        path = os.getcwd()
        #print(path+"\ normal_1.jpg")
        #os.path.join(path, 'normal_1.jpg'), img
        cv2.imwrite(os.path.join(path, 'normal_1.jpg'), imageA)
        #cv2.imshow('', imageB)
        cv2.imwrite(os.path.join(path, "normal_2.jpg"), imageB)
        #cv2.imshow('', diff)
        cv2.imwrite(os.path.join(path, "grey_1.png"), diff)
        #cv2.imshow('', thresh)
        cv2.imwrite(os.path.join(path, "grey_2.png"), thresh)
        #cv2.waitKey(1)
        return similarity, path

class TestDifference(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(TestDifference, self).__init__(parent=parent)
        #self.ui = Compare_Window()
        #self.MainWindow = QtWidgets.QMainWindow()
        #self.ui.setupUi(self.MainWindow)  # self.MainWindow, self.file_path, output, result)
        self.file_path1 = ""
        self.file_path2 = ""
        self.imageA, self.imageB, self.diff, self.thresh = "", "", "", ""
        self.similarity = ""
        self.path = os.getcwd()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_CompareMe(self.similarity, self.path)
        #self.ui.setupUi(self, self.similarity, self.path)

        self.init_window(self.MainWindow)
        #self.show()

    def init_window(self, MainWindow):
        self.setWindowTitle("PhotoChamp: Find Differences And Compare")
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))            #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name
        self.resize(585, 378)
        self.setFixedSize(585, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.m_label = QLabel(self.centralwidget)
        self.m_label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.m_label.setText("Model")
        self.m_label.setObjectName("m_label")

        self.img1_label = QtWidgets.QLabel(self.centralwidget)
        self.img1_label.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.img1_label.setText("Image Name 1")
        self.img1_label.setObjectName("img1_label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 10, 481, 22))
        self.comboBox.setToolTip("Selected model!")
        self.comboBox.setCurrentText("Compare and find Differences")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "Compare and find Differences")

        self.img2_label = QtWidgets.QLabel(self.centralwidget)
        self.img2_label.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.img2_label.setText("Image Name 2")
        self.img2_label.setObjectName("img2_label")

        self.Browse1 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse1.setGeometry(QtCore.QRect(490, 40, 81, 23))
        self.Browse1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Browse1.setToolTip("Browse image path in any order!")
        self.Browse1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Browse1.setText("Browse")
        self.Browse1.setShortcut("")
        self.Browse1.setObjectName("Browse1")

        self.Browse2 = QtWidgets.QPushButton(self.centralwidget)
        self.Browse2.setGeometry(QtCore.QRect(490, 70, 81, 23))
        font = QtGui.QFont()
        font.setKerning(False)
        self.Browse2.setFont(font)
        self.Browse2.setMouseTracking(False)
        self.Browse2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Browse2.setToolTip("Browse image path in any order!")
        self.Browse2.setText("Browse")
        self.Browse2.setShortcut("")
        self.Browse2.setObjectName("Browse2")

        self.frame_Img1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_Img1.setGeometry(QtCore.QRect(10, 120, 271, 191))
        self.frame_Img1.setToolTip("")
        self.frame_Img1.setStatusTip("First image to test difference with other image!")
        self.frame_Img1.setWhatsThis("")
        self.frame_Img1.setAccessibleName("")
        self.frame_Img1.setAccessibleDescription("")
        self.frame_Img1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Img1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Img1.setObjectName("frame_Img1")

        self.displaypic1 = QtWidgets.QLabel(self.frame_Img1)
        self.displaypic1.setGeometry(QtCore.QRect(6, 2, 261, 191))
        self.displaypic1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.displaypic1.setPixmap(QtGui.QPixmap(""))
        self.displaypic1.setScaledContents(True)
        self.displaypic1.setObjectName("displaypic1")

        self.frame_Img2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_Img2.setGeometry(QtCore.QRect(290, 120, 281, 191))
        self.frame_Img2.setToolTip("")
        self.frame_Img2.setStatusTip("Second image to test difference with other image!")
        self.frame_Img2.setWhatsThis("")
        self.frame_Img2.setAccessibleName("")
        self.frame_Img2.setAccessibleDescription("")
        self.frame_Img2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Img2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Img2.setObjectName("frame_Img2")

        self.displaypic2 = QtWidgets.QLabel(self.frame_Img2)
        self.displaypic2.setGeometry(QtCore.QRect(6, 2, 271, 191))
        self.displaypic2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.displaypic2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.displaypic2.setToolTip("")
        self.displaypic2.setStatusTip("")
        self.displaypic2.setWhatsThis("")
        self.displaypic2.setAccessibleName("")
        self.displaypic2.setAccessibleDescription("")
        self.displaypic2.setText("")
        self.displaypic2.setPixmap(QtGui.QPixmap(""))
        self.displaypic2.setScaledContents(True)
        self.displaypic2.setObjectName("displaypic2")

        self.pic1_label = QtWidgets.QLabel(self.centralwidget)
        self.pic1_label.setGeometry(QtCore.QRect(90, 100, 71, 21))
        self.pic1_label.setToolTip("")
        self.pic1_label.setStatusTip("")
        self.pic1_label.setWhatsThis("")
        self.pic1_label.setAccessibleName("")
        self.pic1_label.setAccessibleDescription("")
        self.pic1_label.setText("Image Name 1")
        self.pic1_label.setObjectName("pic1_label")

        self.pic2_label = QtWidgets.QLabel(self.centralwidget)
        self.pic2_label.setGeometry(QtCore.QRect(380, 100, 71, 21))
        self.pic2_label.setToolTip("")
        self.pic2_label.setStatusTip("")
        self.pic2_label.setWhatsThis("")
        self.pic2_label.setAccessibleName("")
        self.pic2_label.setAccessibleDescription("")
        self.pic2_label.setText("Image Name 2")
        self.pic2_label.setObjectName("pic2_label")

        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(250, 320, 91, 23))
        self.back.setToolTip("Go back to main menu!")
        self.back.setStatusTip("")
        self.back.setWhatsThis("")
        self.back.setAccessibleName("")
        self.back.setAccessibleDescription("")
        self.back.setText("Back")
        self.back.setShortcut("")
        self.back.setObjectName("back")
        self.back.clicked.connect(self.back_to_Main)

        self.path_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.path_1.setGeometry(QtCore.QRect(90, 40, 391, 20))
        self.path_1.setReadOnly(True)
        self.path_1.setPlaceholderText("Image path here!")
        self.path_1.setObjectName("path_1")

        self.path_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.path_2.setGeometry(QtCore.QRect(90, 70, 391, 20))
        self.path_2.setReadOnly(True)
        self.path_2.setPlaceholderText("Image path here!")
        self.path_2.setObjectName("path_2")

        self.test = QtWidgets.QPushButton(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(340, 320, 91, 23))
        self.test.setToolTip("Click to start testing! ")
        self.test.setText("Test")
        self.test.setObjectName("test")

        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(430, 320, 81, 23))
        self.Quit.setToolTip("Click to Exit Program!")
        self.Quit.setText("Quit")
        self.Quit.setObjectName("Quit")
        self.Quit.clicked.connect(self.close_main_window)

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actiongetfiles = QtWidgets.QAction(self)

        #self.retranslateUi(MainWindow)
        self.Browse1.clicked.connect(self.getfiles)
        self.Browse2.clicked.connect(self.getfiles2)
        self.test.clicked.connect(self.on_click)
        self.Quit.clicked.connect(self.close_main_window)
        self.path_1.textEdited['QString'].connect(self.test.click)
        self.path_2.textEdited['QString'].connect(self.test.click)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()


    @pyqtSlot()
    def back_to_Main(self):
        from Model_menu import ModelMenu_Window
        self.Model_menu = ModelMenu_Window()
        self.Model_menu.show()
        self.close()

    @pyqtSlot()
    def getfiles(self):
        fileName1, extention = QFileDialog.getOpenFileName(self, 'Single File', 'C:\'',
                                                          "*.png *.xpm *.jpg *.tiff *.jpg *.bmp")
        self.file_path1 = fileName1
        if self.file_path1 != "":
            head, tail = os.path.split(fileName1)
            self.path_1.setText(tail)
            pixmap1 = QPixmap(self.file_path1)
            self.displaypic1.setPixmap(pixmap1)
            self.displaypic1.setPixmap(pixmap1.scaled(self.displaypic1.size(), Qt.IgnoreAspectRatio))

        else:
            pass

    @pyqtSlot()
    def getfiles2(self):
        fileName2, extention = QFileDialog.getOpenFileName(self, 'Single File', 'C:\'',
                                                          "*.png *.xpm *.jpg *.tiff *.jpg *.bmp")
        self.file_path2 = fileName2
        if self.file_path2 != "":
            head, tail = os.path.split(fileName2)
            self.path_2.setText(tail)
            pixmap2 = QPixmap(self.file_path2)
            self.displaypic2.setPixmap(pixmap2)
            self.displaypic2.setPixmap(pixmap2.scaled(self.displaypic2.size(), Qt.IgnoreAspectRatio))

        else:
            pass

    @pyqtSlot()
    def on_click(self):
        if (self.file_path1 == "" + self.file_path2 == "" ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Choose image from your computer !")
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))               #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
            msg.exec_()
        else:
            if str(self.comboBox.currentText()) == "Compare and find Differences":
                self.myThread = Thread()
                similarity1, path1  = self.myThread.find_Difference(self.file_path1, self.file_path2)
                self.myThread.start()
                self.close()
                self.result_window = Ui_CompareMe(similarity1, path1)
                self.result_window.show()
                #self.ui.setupUi(self.MainWindow, similarity, path)
                #self.MainWindow.show()

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


    #def retranslateUi(self, MainWindow):
        #pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TestDifference()
    ui.show()
    sys.exit(app.exec_())
    