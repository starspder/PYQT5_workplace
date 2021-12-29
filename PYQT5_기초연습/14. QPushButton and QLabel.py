"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

14. QPushButton and QLabel

QPushButton
{
setCheckable() 	True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
toggle()	상태를 바꿉니다.
setIcon()	버튼의 아이콘을 설정합니다.
setEnabled()	False 설정 시, 버튼을 사용할 수 없습니다.
isChecked()	버튼의 선택 여부를 반환합니다.
setText()	버튼에 표시될 텍스트를 설정합니다.
text()	버튼에 표시된 텍스트를 반환합니다.

clicked()	버튼을 클릭할 때 발생합니다.
pressed()	버튼이 눌렸을 때 발생합니다.
released()	버튼을 눌렀다 뗄 때 발생합니다.
toggled()	버튼의 상태가 바뀔 때 발생합니다.
}

QLabel: 텍스트 or 이미지 라벨을 만들 때 사용, 상호작용 X
{
 -> 기본적으로 수평 방향으로는 왼쪽, 수직 방향으로는 가운데 정렬임
 -> setAlignment() 통해 조절이 가능함
}

font: 크기 설정안하면 default로 13이 설정됨

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel('First Label:', self)
        label1.setAlignment(Qt.AlignCenter) # 수평, 수직 방향 모두 가운데로 됨

        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True) # 어플이 시작될 때 선택이 되어 있음
        btn1.toggle() # 버튼 상태가 클릭 상태로 바뀜

        label2 = QLabel('Second Label:', self)
        label2.setAlignment(Qt.AlignVCenter) # 세로 방향 가운데 정렬


        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        font1 = label1.font()
        font1.setPointSize(20) # 폰트의 크기,

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True) # 진하게

        label1.setFont(font1)
        label2.setFont(font2)

        label_layout1 = QHBoxLayout()

        label_layout1.addWidget(label1)
        label_layout1.addWidget(btn1)

        label_layout2 = QHBoxLayout()

        label_layout2.addWidget(label2)
        label_layout2.addWidget(btn2)

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # 버튼이 비활성화 됨됨

        vbox = QVBoxLayout()
        vbox.addLayout(label_layout1)
        vbox.addLayout(label_layout2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton & QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


