from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMessageBox, QPushButton, QDialog, QHBoxLayout
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMessageBox, QPushButton, QDialog, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\media\\Icons")

    return os.path.join(base_path, relative_path)  #resource_path('icon.png')))


def resource_remodel_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\Re_Traind_Models")
    catch: base_path = os.path.abspath("D:\\FYP-3\\PhotoChampEXE\\Re_Traind_Models")

    return os.path.join(base_path, relative_path)


class ResultWindow(QDialog):
    def __init__(self , label , prob ):
        super().__init__()
        self.title = "Result"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 400
        self.button_Test_again = QPushButton("Test Again", self)
        self.button_quit = QPushButton("Quit", self)
        label = label
        prob = prob
        self.init_window(label , prob)

    def init_window(self,label , prob):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.png')))                   #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icons8-cbs-512.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        m = PlotCanvas(self, width=5, height=4, dpi=80, label=label, prob=prob)
        m.move(0, 0)

        self.button_Test_again.setToolTip("<h5>to test Another image just Click Test button<h5>")
        self.button_Test_again.setIcon(QtGui.QIcon(resource_path('698827-icon-101-folder-search-512.png')))                     #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\698827-icon-101-folder-search-512.png"))
        self.button_Test_again.setIconSize(QtCore.QSize(15, 15))
        self.button_Test_again.clicked.connect(self.test_again)
        hbox.addWidget(self.button_Test_again)

        self.button_quit.setToolTip("<h5>Close the program<h5>")
        self.button_quit.setIcon(QtGui.QIcon(resource_path('cancel-symbol-transparent-9.png')))                #"D:\\fyp\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\cancel-symbol-transparent-9.png"))
        self.button_quit.setIconSize(QtCore.QSize(15, 15))
        self.button_quit.clicked.connect(self.close_main_window)
        hbox.addWidget(self.button_quit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

    def test_again(self):
        from Test_window_Final import Test_window
        self.Main_window = Test_window()
        self.Main_window.show()
        self.close()

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

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=80 , label = "Forged" , prob = 0.1):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.label = label
        self.prob = prob
        self.plotpie(self.label, self.prob)

    def plotpie(self , label , prob):
        ax = self.figure.add_subplot(111)
        if label == "Forged":
            labels = [label, "Not Forged"]
            probs = [np.abs(prob * 100), np.abs(prob - 1) * 100]
            print(np.abs(prob * 100), np.abs(prob - 1) * 100)
            colors = ['Red', 'Blue']
            ax.text(0.25, 0.95, 'Decision ' + "Forged", transform=ax.transAxes)
            ax.axis("equal")
            ax.pie(probs, autopct='%1.1f%%', shadow=True, colors=colors, radius=1.5, counterclock=True)
            ax.legend(labels, loc=3)
            self.draw()
        elif label == "Not_Forged":
            labels = [label, "Forged"]
            probs = [np.abs(prob * 100), np.abs((prob - 1) * 100)]
            print(np.abs(prob * 100), np.abs(prob - 1) * 100)
            colors = ['Blue', 'Red']
            ax.text(0.25, 0.95, 'Decision ' + " Not Forged", transform=ax.transAxes)
            ax.axis("equal")
            ax.pie(probs, autopct='%1.1f%%', shadow=True, colors=colors, radius=1.5, counterclock=True)
            ax.legend(labels, loc=3)
            self.draw()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = ResultWindow(label = "Test" , prob = 50)
    sys.exit(App.exec())