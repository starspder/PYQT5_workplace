"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/27

1. 창 띄우기

QWidget: 그림 그릴 때 사용되는 캔버스, QWidget위에 다양한 Widget들을 배치시켜 화면에 나타나게 함
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # 타이틀바에 나타나는 창의 제목을 설정
        self.move(300, 300) # 위젯을 스크린의 x=300px, y=300px의 위치로 이동
        self.resize(400, 200) # 위젯의 크기를 너비 400px, 높이 200px로 조절
        self.show() #  위젯을 스크린에 보여줌


if __name__ == '__main__':
   app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야함
   ex = MyApp() # wow
   sys.exit(app.exec_())