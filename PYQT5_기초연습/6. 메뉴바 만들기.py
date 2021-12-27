"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/28

6. 메뉴바 만들기

"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('../example_file/pyqt5_6_exit.png'), 'Exit', self) # exit 아이콘과 exit 라벨을 갖는 하나의 action을 만듬
        exitAction.setShortcut('Ctrl+Q') # 이 액션에 대해 단축키를 만듬
        exitAction.setStatusTip('Exit application') # 상태창에 이 액션을 선택했을 때 텍스트가 나옴
        exitAction.triggered.connect(qApp.quit) # 생성된 (triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료

        self.statusBar() # 상태창 생성

        menubar = self.menuBar() # 메뉴바 생성
        menubar.setNativeMenuBar(False) # 운영체제에 따라 생성된 기본 메뉴바를 사용할건지 일반적으로 False로 설정함. default=False
        filemenu = menubar.addMenu('&File') # File 메뉴를 생성, &는 엠퍼샌드로 F앞에 &있으면 Alt+F를 하면 메뉴가 실행됨
        filemenu.addAction(exitAction) # exitAction 동작을 추가함

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())