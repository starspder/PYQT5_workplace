import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType('../desginer/example2.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.btn_clicked)


    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
