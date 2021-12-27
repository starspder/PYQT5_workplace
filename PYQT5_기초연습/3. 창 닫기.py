"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/27

3. 창 닫기

btn.resize(btn.sizeHint()): sizeHint()는 적절한 크기로 설정하도록 도와줌

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self) # 푸쉬버튼 생성
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit) # clicked 시그널은 생성되어 quit() 메서드에 연결됨

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())