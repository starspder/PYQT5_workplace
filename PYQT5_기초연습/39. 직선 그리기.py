"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2022/1/1

39. 직선 그리기

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawLine')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    # def draw_line(self, qp): # 단순한 선그리기
    #     qp.setPen(QPen(Qt.blue, 8))
    #     qp.drawLine(30, 230, 200, 50) # (x1, y1, x2, y2)임
    #     qp.setPen(QPen(Qt.green, 12))
    #     qp.drawLine(140, 60, 320, 280)
    #     qp.setPen(QPen(Qt.red, 16))
    #     qp.drawLine(330, 250, 40, 190)

    def draw_line(self, qp): # 선 종류 목록
        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        qp.drawLine(20, 20, 380, 20)
        qp.drawText(30, 40, 'Qt.SolidLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashLine))
        qp.drawLine(20, 70, 380, 70)
        qp.drawText(30, 90, 'Qt.DashLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DotLine))
        qp.drawLine(20, 120, 380, 120)
        qp.drawText(30, 140, 'Qt.DotLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashDotLine))
        qp.drawLine(20, 170, 380, 170)
        qp.drawText(30, 190, 'Qt.DashDotLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashDotDotLine))
        qp.drawLine(20, 220, 380, 220)
        qp.drawText(30, 240, 'Qt.DashDotDotLine')

        pen = QPen(Qt.black, 3, Qt.CustomDashLine)
        pen.setDashPattern([4, 3, 2, 5])
        qp.setPen(pen)
        qp.drawLine(20, 270, 380, 270)
        qp.drawText(30, 290, 'Qt.CustomDashLine')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())