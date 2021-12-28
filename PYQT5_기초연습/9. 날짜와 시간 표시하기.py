"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/28

9. 날짜와 시간 표시하기

"""

from PyQt5.QtCore import QDate, Qt, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    now = QDate.currentDate()
    print(now.toString())
    print(now.toString('d.M.yy'))
    print(now.toString('dd.MM.yyyy'))
    print(now.toString('ddd.MMMM.yyyy'))
    print(now.toString(Qt.ISODate))
    print(now.toString(Qt.DefaultLocaleLongDate))
    print('=' * 10)

    time = QTime.currentTime()
    print(time.toString())
    print(time.toString('h.m.s'))
    print(time.toString('hh.mm.ss'))
    print(time.toString('hh.mm.ss.zzz'))
    print(time.toString(Qt.DefaultLocaleLongDate))
    print(time.toString(Qt.DefaultLocaleShortDate))
    print('=' * 10)

    datetime = QDateTime.currentDateTime()
    print(datetime.toString())
    print(datetime.toString('d.M.yy hh:mm:ss'))
    print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
    print(datetime.toString(Qt.DefaultLocaleLongDate))
    print(datetime.toString(Qt.DefaultLocaleShortDate))

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


