# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mm.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import os
from multiprocessing import freeze_support

from SourceCode.Get_Browser_history import Ui_Browser_History
from SourceCode.PDF_JS_view import WindowPDF
from SourceCode.getPDF import PDF_window

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from Find_Subtitles_1 import Download_subtitles
from PDF_Viewer import PDF_veiw
from Select_to_compare import TestDifference
from Test_window_Final import Test_window
from car_detection import Test_Car_window
from mediaplayer import MainWindow


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)


class ModelMenu_Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ModelMenu_Window, self).__init__(parent=parent)
        self.title = "PhotoChamp Application"
        self.top = 200
        self.left = 50
        self.width = 560
        self.height = 300
        self.MainWindow1 = QtWidgets.QMainWindow()
        self.brh = Ui_Browser_History()
        self.init_window()
        # self.show()

    def init_window(self):
        self.setWindowTitle("PhotoChamp IFT App")
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))            #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name

        self.setFixedSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pcLabel = QtWidgets.QLabel(self.centralwidget)
        self.pcLabel.setGeometry(QtCore.QRect(50, 210, 161, 41))

        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pcLabel.setFont(font)
        self.pcLabel.setText("PhotoChamp")
        self.pcLabel.setScaledContents(True)
        self.pcLabel.setObjectName("pcLabel")
        self.ift_label = QtWidgets.QLabel(self.centralwidget)
        self.ift_label.setGeometry(QtCore.QRect(20, 240, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ift_label.setFont(font)
        self.ift_label.setText("Image Forensics Tool")
        self.ift_label.setObjectName("ift_label")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 10, 281, 171))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(resource_path('Main_logo.png')))                         #"C:/Users/Laptop/Downloads/Main_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.models = QtWidgets.QComboBox(self.centralwidget)
        self.models.setGeometry(QtCore.QRect(290, 60, 261, 22))
        self.models.setToolTip(" Choose from models menu!")
        self.models.setCurrentText("Error Level Analysis")
        self.models.setObjectName("models")
        self.models.addItem("Error Level Analysis")
        self.models.addItem("VGG16")
        self.models.addItem("VGG19")
        self.models.addItem("Extract MetaData")
        self.models.addItem("Map GPS Coordinates")
        self.models.addItem("Compare and find Differences")
        self.models.addItem("Car Detection")
        self.models.addItem("Download Subtitles for video")
        self.models.addItem("Get Browser History")
        self.models.addItem("PDF Viewer")
        self.models.addItem("Media Viewer")


        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(450, 255, 100, 23))
        self.start_button.setText("Start")
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.on_click)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()
        # + str(self.models.currentText()) == "VGG16" + str(
        # self.models.currentText()) == "VGG19" + str(self.models.currentText()) == "Extract MetaData")

    def on_click(self):
        if str(self.models.currentText()) == "Error Level Analysis":
            self.test_window = Test_window()
            self.test_window.show()
            self.close()
        elif str(self.models.currentText()) == "VGG16":
            self.test_window = Test_window()
            self.test_window.show()
            self.close()
        elif str(self.models.currentText()) == "VGG19":
            self.test_window = Test_window()
            self.test_window.show()
            self.close()
        elif str(self.models.currentText()) == "Extract MetaData":
            self.test_window = Test_window()
            self.test_window.show()
            self.close()
        elif str(self.models.currentText()) == "Map GPS Coordinates":
            self.test_window = Test_window()
            self.test_window.show()
            self.close()
        else:
            if str(self.models.currentText()) == "Compare and find Differences":
                self.test_window = TestDifference()
                self.test_window.show()
                self.close()
            if str(self.models.currentText()) == "Car Detection":
                self.test_window = Test_Car_window()
                self.test_window.show()
                self.close()
            if str(self.models.currentText()) == "Get Browser History":
                self.test_window = self.brh.Get_History(self.MainWindow1)
                self.close()
            if str(self.models.currentText()) == "PDF Viewer":
                self.close()
                self.test_window = PDF_window()
            if str(self.models.currentText()) == "Media Viewer":
                self.test_window = MainWindow()
                self.close()
            if str(self.models.currentText()) == "Download Subtitles for video":
                self.test_window = Download_subtitles()
                self.close()


if __name__ == "__main__":
    import sys

    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    freeze_support()
    window = ModelMenu_Window()
    window.show()
    sys.exit(App.exec())
