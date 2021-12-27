"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/27

4. 툴팁 나타내기
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SanSerif', 10)) # 10px 크기의 SansSerif 폰트 사용
        self.setToolTip('This is a <b>QWidget</b> widget') # self니까 widget을 뜻함 widget의 툴팁임

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') # button의 툴팁임
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())