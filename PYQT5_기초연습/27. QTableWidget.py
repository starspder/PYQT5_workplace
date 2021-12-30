"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

27. QTableWidget

QTableWidget: 테이블 형태로 항목을 배치하고 다룸
{
  - horizontalHeader() 수평 헤더를 반환
  - setSectionResizeMode() 헤더의 크기를 조절하는 방식을 지정
  - QHeaderView.Stretch: 헤더의 폭이 위젯의 폭에 맞춰지도록 함
  - QHeaderView.ResizeToContents:헤더의 폭이 항목 값의 폭에 맞춰지도록 함
}
"""

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20) # 테이블의 행 (Row)의 개수를 지정
        self.tableWidget.setColumnCount(4) # 테이블의 열 (Column)의 개수를 지정

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # 테이블의 항목을 편집 가능하도록 하는 액션을 지정(편집X)
        #self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked) # 더블클릭 편집가능
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers) # 클릭, 더블 클릭 전부 수정 가능

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)\

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i + j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

