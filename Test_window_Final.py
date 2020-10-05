import os

from PIL import Image, ImageChops, ImageEnhance
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QComboBox, QLineEdit, QLabel, QPushButton, QWidget, \
    QMessageBox
from Result_Window_Final import ResultWindow
from keras.models import load_model
from pylab import *
from multiprocessing import freeze_support
import exifread
from GPS_Mapping import map_html
from metaExtract_window import *
from metaExtract_window import Ui_metaExtract_window
from simple_PIL_code import extractPIL


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\FYP-3\PhotoChampEXE\media\Icons")

    return os.path.join(base_path, relative_path)



def resource_model_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\FYP-3\PhotoChampEXE\sys_models")

    return os.path.join(base_path, relative_path)


class Thread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def test_image_with_ela(self, image_path, model_path):
        """
            Error Level Analysis
            :param model_path:
            :param  image_path
            :return label[Forged , Not Forged] , prob[class probability]
        """
        # loading Model
        model = load_model(model_path)
        # Read image
        image_saved_path = image_path.split('.')[0] + '.saved.jpg'

        # calculate ELA
        image = Image.open(image_path).convert('RGB')
        image.save(image_saved_path, 'JPEG', quality=90)
        saved_image = Image.open(image_saved_path)
        ela = ImageChops.difference(image, saved_image)
        extrema = ela.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
        scale = 255.0 / max_diff
        ela_im = ImageEnhance.Brightness(ela).enhance(scale)

        # prepare image for testing
        image = array(ela_im.resize((128, 128))).flatten() / 255.0
        image = image.reshape(-1, 128, 128, 3)
        # prediction
        prob = model.predict(image)[0]
        idx = np.argmax(prob)
        pred = model.predict(image)
        pred = pred.argmax(axis=1)[0]

        label = "Forged" if pred == 1 else "Not_Forged"
        return label, prob[idx]

    def test_image_with_vgg16(self, image_path, model_path):
        """
                VGG16 GoogleNet Competition Pre-trained Model
                :param model_path:
                :param  image_path
                :return label[Forged , Not Forged] , prob[class probability]
        """
        model = load_model(model_path)
        # Read image
        image = Image.open(image_path).convert('RGB')

        # prepare image for testing
        image = array(image.resize((100, 100))).flatten() / 255.0
        image = image.reshape(-1, 100, 100, 3)

        # Make predictions on the input image
        prob = model.predict(image)[0]
        idx = np.argmax(prob)

        # predictions
        prob = model.predict(image)[0]
        idx = np.argmax(prob)
        pred = model.predict(image)
        pred = pred.argmax(axis=1)[0]

        label = "Forged" if pred == 1 else "Not_Forged"
        return label, prob[idx]

    def test_image_with_vgg19(self, image_path, model_path):
        """
                VGG19 GoogleNet Competition Pre-trained Model
                :param model_path:
                :param  image_path
                :return label[Forged , Not Forged] , prob[class probability]
        """
        model = load_model(model_path)
        # Read image
        image = Image.open(image_path).convert('RGB')

        # prepare image for testing
        image = array(image.resize((100, 100))).flatten() / 255.0
        image = image.reshape(-1, 100, 100, 3)

        prob = model.predict(image)[0]
        idx = np.argmax(prob)
        pred = model.predict(image)
        pred = pred.argmax(axis=1)[0]

        label = "Forged" if pred == 1 else "Not_Forged"
        return label, prob[idx]

    def extract_with_ExifRead(self, image_path):
        f = open(image_path, 'rb')
        tags = exifread.process_file(f)
        data_All = []
        data = []
        i = 1
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                data = ("%s : %s" % (tag, tags[tag]))
                data_All.append(data)

        # print(data_All)
        return data_All

    def extract_with_PIL(self, image_path):
        try:
            lat, lon, date, tags = extractPIL(image_path)
            dataPil = []
            i = 1
            for tag in tags.keys():
                if tag not in (
                        'JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote', 'MakerNote', 'UserComment'):
                    data1 = ("%s : %s" % (tag, tags[tag]))
                    dataPil.append(data1)

            return lat, lon, date, dataPil
        except Exception as e:
            return lat, lon, e, e


class Test_window(QWidget):
    def __init__(self, parent=None, model_path= resource_model_path('ELA_Model.h5')):
        super().__init__(parent=parent)
        self.title = "PhotoChamp IFT App"
        self.top = 200
        self.left = 500
        self.width = 550
        self.height = 345
        self.file_path = ""
        self.model_path = model_path
        self.tags = ""
        dataPil = ''
        lat = ''
        lon = ''
        date = ''
        self.metaExtract_window = QtWidgets.QMainWindow()
        self.gui_EMD = Ui_metaExtract_window()
        # Ui_metaExtract_window(self.metaExtract_window, self.tags, lat, lon, date, dataPil)
        # self.gui_EMD.Extract_metadata(self.metaExtract_window, tags, lat, lon, date, dataPil)
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
        label.setFont(QtGui.QFont("Sanserif", 8))
        label.move(10, 20)

        self.combo = QComboBox(self)
        self.combo.addItem("Error Level Analysis")
        self.combo.addItem("VGG16")
        self.combo.addItem("VGG19")
        self.combo.addItem("Extract MetaData")
        self.combo.addItem("GPS Coordinates Mapping")

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
        self.Model_menu1 = ModelMenu_Window()
        self.Model_menu1.show()
        self.close()

    @pyqtSlot()
    def getfiles(self):
        fileName, extention = QFileDialog.getOpenFileName(self, 'Single File', 'C:\\',
                                                          "*.png *.xpm *.jpg *.tiff *.jpeg *.bmp")
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
            msg.setWindowIcon(QtGui.QIcon(resource_path('icons8-cbs-512.ico')))         #   "D://fyp//PhotoChamp_FYP-03//PhotoChamp//Icons//icons8-cbs-512.ico"))
            msg.exec_()
        else:
            if str(self.combo.currentText()) == "Error Level Analysis":
                model = "D:\\FYP-3\\PhotoChamp_FYP-03\\PhotoChamp\\SourceCode\\sys_models\\ELA_Bothdataset.h5"
                self.myThread = Thread()
                label, prob = self.myThread.test_image_with_ela(self.file_path, model_path=model)
                self.myThread.start()
                self.close()
                self.result_window = ResultWindow(label, prob)
                self.result_window.show()

            elif str(self.combo.currentText()) == "VGG16":
                model = resource_model_path('VGG16_CMFD.h5')             #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\SourceCode\\sys_models\\VGG16_CMFD.h5"
                self.myThread = Thread()
                label, prob = self.myThread.test_image_with_vgg16(self.file_path, model_path=model)
                self.myThread.start()
                self.close()
                self.result_window = ResultWindow(label, prob)
                self.result_window.show()

            elif str(self.combo.currentText()) == "VGG19":
                model = resource_model_path('VGG19_719868.h5')             #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\SourceCode\\sys_models\\VGG19_719868.h5"
                self.myThread = Thread()
                label, prob = self.myThread.test_image_with_vgg19(self.file_path, model_path=model)
                self.myThread.start()
                self.close()
                self.result_window = ResultWindow(label, prob)
                self.result_window.show()

            elif str(self.combo.currentText()) == "Extract MetaData":
                self.myThread = Thread()
                tags = self.myThread.extract_with_ExifRead(self.file_path)
                lat, lon, date, dataPil = self.myThread.extract_with_PIL(self.file_path)
                self.myThread.start()
                self.close()
                self.result_out = self.gui_EMD.Extract_metadata(self.metaExtract_window, tags, lat, lon, date, dataPil)

                # Ui_metaExtract_window(self.metaExtract_window, tags, lat, lon, date, dataPil)
                self.metaExtract_window.show()


            elif str(self.combo.currentText()) == "GPS Coordinates Mapping":
                self.result_window = map_html(self.file_path)

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
    window = Test_window()
    sys.exit(App.exec())
