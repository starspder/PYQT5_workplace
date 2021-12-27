"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/28

5. 상태바 만들기

Main Window: 메뉴바, 툴바, 상태바를 갖는 어플리케이션임
메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 갖고 있음

QWidget vs QMainWindow

QWidget: 메뉴바를 만들 수 없음
QMainWindow: 메뉴바를 만들 수 있음. 그리고 생성하게 되면 자동으로 QWidget이 포함된 상태로 만들어짐

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready') # showMessage를 통해 상태바에 표시됨
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())