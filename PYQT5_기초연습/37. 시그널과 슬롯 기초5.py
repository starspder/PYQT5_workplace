"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2022/1/1

37. 시그널과 슬롯 기초5


"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow

class Communicate(QObject):
    closeApp = pyqtSignal() # communicate 속성으로써 closeApp이라는 시그널 생성

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close) # 이 시그널을 close 슬롯에 연결함

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit() # mousePressEvent 이벤트 핸들러를 사용해서, 마우스를 클릭했을 때 closeApp 시그널이 방출

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
