"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

21. QTabWidget and QPixmap

QTabWidget: 가로로 된 블록단위 메뉴바

QPixmap: 이미지를 다룰 때 사용되는 위젯

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        ### pixmap

        pixmap = QPixmap('../example_file/pyqt5_21_landscape')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap) # pixmap을 라벨에 표시될 이미지로 설정해야함
        lbl_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox.addWidget(lbl_img)
        vbox.addWidget(lbl_size)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())