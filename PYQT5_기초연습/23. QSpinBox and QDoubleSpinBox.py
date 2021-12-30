"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

23. QSpinBox and QDoubleSpinBox

QSpinBox: 정수를 선택, 조절하도록 하는 스핀 박스 위젯
QDoubleSpinBox: 실수를 선택, 조절하도록 하는 더블 스핀 박스 위젯
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout, QDoubleSpinBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        #vbox.addStretch() # 여기를 저쪽 addStretch하고 똑같이하면 빈공간 동일하게 위젯이 가운데로 배치됨
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch() # 신축성 있는 빈 공간을 제공(default = 0)

        #### double
        self.bbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100) # 최소값은 0.0, 최대값은 99.99가 디폴트
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ') # 숫자 앞에 올 문자를 설정
        self.dspinbox.setDecimals(1) # 소수점 아래 표시될 자리수
        self.bbl2 = QLabel('$ 0.0')
        self.dspinbox.valueChanged.connect(self.value_changed2)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.bbl1)
        vbox2.addWidget(self.dspinbox)
        vbox2.addWidget(self.bbl2)
        vbox2.addStretch()

        total_vbox = QVBoxLayout()
        total_vbox.addLayout(vbox)
        total_vbox.addLayout(vbox2)



        self.setLayout(total_vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))

    def value_changed2(self):
        self.bbl2.setText('$ ' + str(self.dspinbox.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())