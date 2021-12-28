"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/29

11. 절대적 배치

레이아웃 (Layout)은 어플리케이션 창에 위젯들을 배치하는 방식

다만 배치할떈 주로 QT 디자이너를 사용함.

방식에는 절대적 배치, 박스 레이아웃, 그리드 레이아웃이 있음

절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치
  1. 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않음
  2. 다양한 플랫폼에서 다르게 보일 수 있음
  3. 폰트를 바꾸면 레이아웃이 망가질 수 있음
  4. 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 하며, 이는 매우 번거로움
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20) # x=20, y=20에 위치시킴
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
