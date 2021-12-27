"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/28

7. 툴바 만들기

- 툴바는 자주 사용되는 명령어를 더 편리하게 사용하게 해줌

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('../example_file/pyqt5_7_exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit') # 툴바 생성
        self.toolbar.addAction(exitAction) # 툴바에 액션을 추가함

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
