import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QWidget, QPushButton
import os
from multiprocessing import freeze_support
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from Training_window_Final import Training_window

from Model_menu import ModelMenu_Window


def resource_path(relative_path):
   try:
       base_path = sys._MEIPASS
   except Exception:
       base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

   return os.path.join(base_path, relative_path)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        """constructor to create a new window with charactersitis after create object from class window"""
        super().__init__()
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 570
        self.height = 280
        self.file_path = ""
        self.init_window()

    def init_window(self):
        """initialize Main IFD window"""

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))                             #"D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//icon.png"))  # icon Pic File name
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        font = QtGui.QFont()
        font.setUnderline(True)
        font.setFamily("Sanserif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        label = QLabel(self)
        label.move(277, 85)
        label.setText('PhotoChamp')
        label.setFont(font)

        label = QLabel(self)
        label.move(277, 125)
        label.setText('Image Forensics Tool')
        label.setFont(QtGui.QFont("Sanserif", 16))
        '''
        label = QLabel(self)
        label.move(277, 140)
        label.setText('Forensics Tool')
        label.setFont(QtGui.QFont("Sanserif", 20))
        '''

        label = QLabel(self)
        label.move(20, 200)
        label.setText('Click training or testing to start the process:')
        label.setFont(QtGui.QFont("Sanserif", 8))

        pixmap = QPixmap((resource_path('icons8-cbs-512.png')))                   #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.png")
        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setGeometry(QtCore.QRect(0, 10, 281, 171))
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))
        self.label.show()

        self.combo = QComboBox(self)
        self.combo.addItem("Training")
        self.combo.addItem("Testing")
        self.combo.setGeometry(QRect(234, 198, 300, 20))

        self.button = QPushButton("Start", self)
        self.button.setGeometry(QRect(445, 230, 90, 20))
        self.button.setIcon(QtGui.QIcon(resource_path('start.png')))                                               #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\start.png"))  # icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.setToolTip("<h5>Launch Your choice either Training or Testing<h5>")
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        if str(self.combo.currentText()) == "Training":
            self.training_window = Training_window()
            self.training_window.show()
            self.close()

        elif str(self.combo.currentText()) == "Testing":
            self.test_window = ModelMenu_Window()
            self.test_window.show()
            self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    freeze_support()
    window = MainWindow()
    sys.exit(App.exec())
