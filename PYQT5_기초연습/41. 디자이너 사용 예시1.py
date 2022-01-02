"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2022/1/2

41. 디자이너 사용 예시1

"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("../desginer/example1.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()