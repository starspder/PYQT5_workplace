"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

24. QDateEdit and QTimeEdit

QDateEdit: 사용자에게 날짜를 선택, 편집하도록 할 때 사용
QTimeEdit: 사용자에게 시간을 선택, 편집하도록 할 때 사용
QDateTimeEdit: 사용자에게 날짜와 시간을 선택, 편집하도록 할 때 사용
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout, QDateEdit, QDateTimeEdit
from PyQt5.QtCore import QDate, QTime, QDateTime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QDateEdit')

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        ######
        lbl2 = QLabel('QTimeEdit')
        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(lbl2)
        vbox2.addWidget(timeedit)
        vbox2.addStretch()

        #####

        lbl3 = QLabel('QTimeDateEdit')
        date_time_edit = QDateTimeEdit(self)
        date_time_edit.setDateTime(QDateTime.currentDateTime())
        date_time_edit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        date_time_edit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox3 = QVBoxLayout()
        vbox3.addWidget(lbl3)
        vbox3.addWidget(date_time_edit)
        vbox3.addStretch()


        total_box = QVBoxLayout()
        total_box.addLayout(vbox)
        total_box.addLayout(vbox2)
        total_box.addLayout(vbox3)



        self.setLayout(total_box)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())