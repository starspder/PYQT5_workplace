"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/28

8. 창을 화면의 가운데로


"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry() # 창의 위치와 크기 정보를 가져옴.
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면의 가운데 위치를 파악함
        qr.moveCenter(cp) # 직사각형 위치를 화면 중심의 위치로 이동
        self.move(qr.topLeft()) # 실제 창을 직사각형 위치로 이동시킴

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

