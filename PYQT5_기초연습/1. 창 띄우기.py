"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/27

1. 창 띄우기

QWidget: 그림 그릴 때 사용되는 캔버스, QWidget위에 다양한 Widget들을 배치시켜 화면에 나타나게 함

기본적으로 앱 생성 및 종료는 main코드에 포함되어야함
1. app = QApplication(sys.argv)
 -> 인자를 sys.argv를 받음. sys.argv는 .py의 절대경로를 인자로 넣어줌. 즉 QApllication 객체가 실행할 파일이 현재
 파이썬 코드 라는 것을 알려줌

2. sys.exit(app.exec_())
  -> 나는 프로그램을 계속 실행하고 싶음 그래서 대기 상태에 있어야함. 무한 루프 상태로 만들어야함. 그것이 바로 app.exec_()임
  -> execute 약자이고 app이 종료되면 0을 반환함 즉 sys.exit(0)은 루프에서 빠져나와 정상 종료를 함

위젯: 어플리케이션을 이루는 기본적인 구성 요소
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