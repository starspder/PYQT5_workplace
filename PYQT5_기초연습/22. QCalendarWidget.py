"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

22. QCalendarWidget

QCalendarWidget: 사용자가 날짜를 선택할 수 있도록 달력을 표시

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True) # 날짜 사이에 그리드가 표시
        cal.clicked[QDate].connect(self.showDate) # 날짜를 클릭했을 때 showDate 메서드가 호출되도록 연결

        self.lbl = QLabel(self)
        date = cal.selectedDate() # 현재 선택된 날짜 정보를 갖고 있음(디폴트 현재 날짜)
        self.lbl.setText(date.toString())  # 현재 날짜 정보를 라벨에 표시되도록 해줌

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())