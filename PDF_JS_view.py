import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets, QtGui



class WindowPDF(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, path1):
        super(WindowPDF, self).__init__()
        PDFJS = 'file:///C:/Users/Laptop/Documents/pdfjs-2.4.456-dist/web/viewer.html'
        path = 'file:///'
        path1 = path1
        PDF = path + path1
        self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))
        self.setWindowTitle("PDF with PDF.JS")
        self.setWindowIcon(QtGui.QIcon(
            "D:\\fyp\\\PhotoChamp_FYP-03\\PhotoChamp\\Icons\\icon.png"))  # icon Pic File name


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    path1 = 'C:\\Users\\Laptop\\Documents\\1627.pdf'
    window = WindowPDF(path1)
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())