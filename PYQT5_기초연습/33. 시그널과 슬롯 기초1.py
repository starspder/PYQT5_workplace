"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2022/1/1

33. 시그널과 슬롯

시그널 <- 위젯에 정의된 이벤트
슬롯 <- 이벤트가 발생할 때 호출되는 함수나 메서드



"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) # LCD 화면과 같이 숫자를 표시함
        dial = QDial(self) # 회전해서 값을 조절하는 위젯

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
