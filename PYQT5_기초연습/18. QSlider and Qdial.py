"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

18. QSlider and Qdial

QSlider는 수평 또는 수직 방향의 슬라이더를 제공
{
  - 슬라이더의 틱(tick)의 간격을 조절하기 위해서는 setTickInterval() 메서드, 틱(tick)의 위치를 조절하기 위해서는 setTickPosition() 메서드를 사용
  - setTickInterval() 메서드의 입력값은 픽셀이 아니라 값을 의미
  - setTickPosition()
     QSlider.NoTicks	0	틱을 표시하지 않습니다.
     QSlider.TicksAbove	1	틱을 (수평) 슬라이더 위쪽에 표시합니다.
     QSlider.TicksBelow	2	틱을 (수평) 슬라이더 아래쪽에 표시합니다.
     QSlider.TicksBothSides	3	틱을 (수평) 슬라이더 양쪽에 표시합니다.
     QSlider.TicksLeft	TicksAbove	틱을 (수직) 슬라이더 왼쪽에 표시합니다.
     QSlider.TicksRight	TicksBelow	틱을 (수직) 슬라이더 오른쪽에 표시합니다.
}

QDial은 슬라이더를 둥근 형태로 표현한 다이얼 위젯
{
 - 다이얼 위젯에 노치(notch)를 표시하기 위해서는 setNotchesVisible() 메서드를 사용
 - True로 설정하면 둥근 다이얼을 따라서 노치들이 표시
}

QSlider & QDial 시그널
====
valueChanged()	슬라이더의 값이 변할 때 발생합니다.
sliderPressed()	사용자가 슬라이더를 움직이기 시작할 때 발생합니다.
sliderMoved()	사용자가 슬라이더를 움직이면 발생합니다.
sliderReleased()	사용자가 슬라이더를 놓을 때 발생합니다.
====

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2) # . setSingleStep() 메서드는 조절 가능하는 최소 단위

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())