"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2022/1/1

35. 시그널과 슬롯 기초3


"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape: # esc키를 누르면
            self.close()
        elif e.key() == Qt.Key_F: # F키를 누르면
            self.showFullScreen()
        elif e.key() == Qt.Key_N: # N키를 누르면
            self.showNormal()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())