"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

15. QCheckbox and QRadioButton

QCheckbox : on(체크됨)/off(체크안됨)으로 구분함, 이 위젯은 하나의 텍스트 라벨과 함께 체크 박스를 제공
{
  체크 박스가 선택되거나 해제될 때, stateChanged() 시그널을 발생
  체크 박스의 선택 여부를 확인하기 위해서, isChecked() 메서드를 사용
  일반적인 체크 박스는 선택/해제 상태만을 갖지만, setTristate() 메서드를 사용하면 '변경 없음(no change)' 상태를 가질 수 있음
  세 가지 상태를 갖는 체크 박스의 상태를 얻기 위해서는 checkState() 메서드를 사용합니다. 선택/변경 없음/해제 여부에 따라 각각 2/1/0 값을 반환
  QButtonGroup 클래스를 사용하면 여러 개의 버튼을 묶어서 exclusive/non-exclusive 버튼 그룹을 만들 수 있음

  text()	체크 박스의 라벨 텍스트를 반환합니다.
  setText()	체크 박스의 라벨 텍스트를 설정합니다.
  isChecked()	체크 박스의 상태를 반환합니다. (True/False)
  checkState()	체크 박스의 상태를 반환합니다. (2/1/0)
  toggle()	체크 박스의 상태를 변경합니다.

  pressed()	체크 박스를 누를 때 신호를 발생합니다.
  released()	체크 박스에서 뗄 때 신호를 발생합니다.
  clicked()	체크 박스를 클릭할 때 신호를 발생합니다.
  stateChanged()	체크 박스의 상태가 바뀔 때 신호를 발생합니다.


}

QRadioButton: 사용자가 선택할 수 있는 버튼을 만들 때 사용(라디오 버튼은 autoExclusive 즉 하나의 버튼을 선택하면 나머지는 선택 해제가 됨)
{
  -> 한 번에 여러 버튼을 선택할 수 있도록 하려면 setAutoExclusive() 메서드에 False를 입력
  -> 한 위젯 안에 여러 개의 exclusive 버튼 그룹을 배치하고 싶다면 QButtonGroup() 메서드를 사용
  -> 체크 박스와 마찬가지로 버튼의 상태가 바뀔 때, toggled() 시그널이 발생
  -> 정 버튼의 상태를 가져오고 싶을 때, isChecked() 메서드를 사용

  text()	버튼의 텍스트를 반환합니다.
  setText()	라벨에 들어갈 텍스트를 설정합니다.
  setChecked()	버튼의 선택 여부를 설정합니다.
  isChecked()	버튼의 선택 여부를 반환합니다.
  toggle()	버튼의 상태를 변경합니다.

  pressed()	버튼을 누를 때 신호를 발생합니다.
  released()	버튼에서 뗄 때 신호를 발생합니다.
  clicked()	버튼을 클릭할 때 신호를 발생합니다.
  toggled()	버튼의 상태가 바뀔 때 신호를 발생합니다.


}

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle() # 디폴트로 체크가 되어있지 않은 off 상태로 나타나기 때문에 on 상태로 바꾸기 위해 toggle() 메서드를 사용
        cb.stateChanged.connect(self.changeTitle)

        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True) # 프로그램이 실행될 때 버튼이 선택되서 표시

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setWindowTitle('QCheckBox & QRadioButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())