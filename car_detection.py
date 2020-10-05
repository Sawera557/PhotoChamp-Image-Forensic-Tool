# from car_result import ui_MainWindow
from optparse import OptionParser

from PIL import Image
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QComboBox, QLineEdit, QLabel, QMessageBox, QWidget, \
    QPushButton
from keras.models import load_model
from multiprocessing import freeze_support
from pylab import *
from result_car import *

from result_car import Result_Car

row, column = 100, 100


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)



def resource_model_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\sys_models")

    return os.path.join(base_path, relative_path)


def normalize(picture):
    width, height = picture.size
    normalized_array = []
    for j in range(0, height):
        for i in range(0, width):
            pixel = picture.getpixel((i, j))
            normalized_array.append(pixel[0] / 255.0)
    return np.array(normalized_array)


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def test_with_CNN(self, image_path, model_path):
        """
            CNN
            :param model_path:
            :param  image_path
            :return output[classes] , result[text output a car]
        """
        model = load_model(model_path)
        parser = OptionParser()
        parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")

        img = Image.open(image_path)
        img = img.resize((row, column), Image.ANTIALIAS)

        X_test = normalize(img)
        X_test = X_test.reshape(1, row, column, 1)  # (1, row, column) 3D input for CNN
        classes = model.predict(X_test)
        output = str(classes)

        maxVal = classes[0].max()
        indexVal = np.where(classes[0] == maxVal)  # result is an array

        if indexVal[0] == 0:
            result = "......... It is a CAR ........."
        else:
            result = "......... It is not a CAR ........."

        return output, result

    def test_with_DNN(self, image_path, model_path):
        """
                DNN
                :param model_path:
                :param  image_path
                :return output[classes] , result[text output a car]
        """
        model = load_model(model_path)
        parser = OptionParser()
        parser.add_option("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")

        img = Image.open(image_path)
        img = img.resize((row, column), Image.ANTIALIAS)

        X_test = normalize(img)

        X_test = X_test.reshape(1, row * column)  # [row*column] - 1D input for DNN
        classes = model.predict(X_test)
        output = str(classes)

        maxVal = classes[0].max()
        indexVal = np.where(classes[0] == maxVal)  # result is an array

        if indexVal[0] == 0:
            result = "......... It is a CAR ........."
        else:
            result = "......... It's not a CAR ........."

        return output, result


class Test_Car_window(QWidget):
    def __init__(self, parent=None, model_path="C:\\Users\\Laptop\\PycharmProjects\\ELA_Model.h5", output="", result=""):
        super().__init__()
        self.title = "IFD Application"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 345
        self.file_path = ""
        self.model_path = model_path
        output = output
        result = result
        self.MainWindow = QtWidgets.QMainWindow()
        #self.Result_Car = Result_Car(self.file_path, output, result)
        #self.ui.setupUi(self.MainWindow, self.file_path, output, result)
        #self.ui.Back.clicked.connect(self.back_to_Main)
        #self.ui.Quit.clicked.connect(self.close_main_window)

        #self.ui.Back.clicked.connect(self.showMessage)
        self.init_window()

    def init_window(self):
        """initialize window"""
        self.setWindowTitle("PhotoChamp: Car-Detection")
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))          #"D:\\fyp\\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name
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
        label.setFont(QtGui.QFont("Sanserif", 8))

        # text Box
        self.line_edit = QLineEdit(self)
        self.line_edit.setReadOnly(True)
        self.line_edit.setFont(QtGui.QFont("Sanserif", 8))
        self.line_edit.setGeometry(QRect(80, 40, 365, 20))
        self.line_edit.setPlaceholderText("image Name here!")

        # Button
        self.button = QPushButton("Browse", self)
        self.button.setGeometry(QRect(450, 40, 90, 20))
        self.button.setToolTip(
            "<h5>Browse image from your computer to start test!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('698831-icon-105-folder-add-512.png')))            #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\698831-icon-105-folder-add-512.png"))  # icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.getfiles)

        # Button
        self.button = QPushButton("Test", self)
        self.button.setGeometry(QRect(270, 310, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('698827-icon-101-folder-search-512.png')))           #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\698827-icon-101-folder-search-512.png"))  # icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.on_click)

        # Button
        self.button = QPushButton("Back", self)
        self.button.setGeometry(QRect(180, 310, 90, 20))
        self.button.setToolTip("<h5>test image either Forged or Not Forged!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('repeat-pngrepo-com.png')))        #"repeat-pngrepo-com.png"))  icon Pic File name
        self.button.setIconSize(QtCore.QSize(15, 15))  # to change icon Size
        self.button.clicked.connect(self.back_to_Main)

        # Button
        self.button = QPushButton(" Quit", self)
        self.button.setGeometry(QRect(360, 310, 90, 20))
        self.button.setToolTip("<h5>Close the program!<h5>")  # Notice using h2 tags From Html
        self.button.setIcon(QtGui.QIcon(resource_path('cancel-symbol-transparent-9.png')))            #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\cancel-symbol-transparent-9.png"))  icon Pic File name
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
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(10, 20)

        self.combo = QComboBox(self)
        self.combo.addItem("Convolutional Neural Network (CNN)")
        self.combo.addItem("Dense Neural Network (DNN)")

        self.combo.setGeometry(QRect(80, 15, 460, 20))

        label = QLabel(self)
        label.setText('Image Informations')
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(50, 75)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topleft.setGeometry(QRect(10, 90, 175, 200))

        label = QLabel(self)
        label.setText('Image')
        label.setFont(QtGui.QFont("Sanserif", 8))
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
        fileName, extention = QFileDialog.getOpenFileName(self, 'Single File', 'C:\'',
                                                          "*.png *.xpm *.jpg *.tiff *.jpg *.bmp")
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
            self.label_1.setText('and please wait..')
            self.label_1.setFont(QtGui.QFont("Sanserif", 12))

            self.label_2.move(410, 100)
            self.label_2.setText('click test')
            self.label_2.setFont(QtGui.QFont("Sanserif", 12))

            pixmap = QPixmap(self.file_path)
            self.label.setPixmap(pixmap)
            self.label.resize(190, 190)
            self.label.move(205, 95)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio))

            # image information
            image = Image.open(self.file_path)
            width, height = image.size
            resolution = "Resolution " + str(width) + "X" + str(height)
            self.label2.setText(resolution)
            self.label2.setFont(QtGui.QFont("Sanserif", 8))
            self.label2.move(15, 100)

            head, tail = os.path.split(self.file_path)
            tail2 = tail.split('.')[1]
            file_type = "Item Type " + str(tail2)
            self.label3.setText(file_type)
            self.label3.setFont(QtGui.QFont("Sanserif", 8))
            self.label3.move(15, 112)

            size = os.path.getsize(self.file_path)
            size = np.int(size / 1000)
            text = str(size) + "KB"
            self.label4.setText(text)
            self.label4.setFont(QtGui.QFont("Sanserif", 8))
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
            msg.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))  #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
            msg.exec_()
        else:
            if str(self.combo.currentText()) == "Convolutional Neural Network (CNN)":
                model = resource_model_path('car_detection_keras_CNN_model.h5')    #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\SourceCode\\sys_models\\car_detection_keras_CNN_model.h5"
                self.myThread = Thread()
                output, result = self.myThread.test_with_CNN(self.file_path, model_path=model)
                self.myThread.start()
                self.close()
                self.result_Window = Result_Car(self.file_path, output, result)
                #self.MainWindow.show()
            elif str(self.combo.currentText()) == "Dense Neural Network (DNN)":
                model = resource_model_path('car_detection_keras_DNN_model.h5')           #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\SourceCode\\sys_models\\car_detection_keras_DNN_model.h5"
                self.myThread = Thread()
                output, result = self.myThread.test_with_DNN(self.file_path, model_path=model)
                self.myThread.start()
                self.close()
                self.result_Window = Result_Car(self.file_path, output, result)
                #self.result_Window.show()

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
    window = Test_Car_window()
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())
