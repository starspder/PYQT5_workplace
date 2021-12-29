"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

16. QComboBox and QLineEdit

QComboBox는 작은 공간을 차지하면서, 여러 옵션들을 제공하고 그 중 하나의 옵션을 선택할 수 있도록 해주는 위젯

QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯
{
  - echoMode()를 설정함으로써 '쓰기 전용' 영역으로 사용할 수 있습니다. 이 기능은 비밀번호와 같은 입력을 받을 때 유용하게 사용
  - setEchoMode() 메서드로 이러한 모드를 설정가능(default=normal)
      QLineEdit.Normal	0	입력된 문자를 표시합니다. (기본값)
      QLineEdit.NoEcho	1	문자열을 표시하지 않습니다. 이 설정은 비밀번호의 글자수도 공개하지 않을 때 유용합니다.
      QLineEdit.Password	2	입력된 문자 대신 비밀번호 가림용 문자를 표시합니다.
      QLineEdit.PasswordEchoOnEdit	3	입력할 때만 문자를 표시하고, 수정 중에는 다른 문자를 표시합니다.
  - maxLength() 메서드로 입력되는 텍스트의 길이를 제한할 수 있고, setValidator() 메서드로 입력되는 텍스트의 종류를 제한
  - setText() 또는 insert() 메서드로, 텍스트를 편집, text()로 입력된 텍스트를 가져올 수 있음
  - echoMode가 입력 텍스트와 표시되는 텍스트가 다르다면 displayText()로 표시되는 텍스트를 가져올 수 있음
  - setSelection(), selectAll() 메서드로 텍스트를 선택하거나, cut(), copy(), paste() 메서드를 통해 잘라내기, 복사하기, 붙여넣기
  - setAlignment() 메서드로 텍스트의 정렬
  - textChanged(), cursorPositionChanged()와 같은 시그널이 발생
  cursorPositionChanged()	커서가 움직일 때 발생하는 신호를 발생합니다.
  editingFinished()	편집이 끝났을 때 (Return/Enter 버튼이 눌릴 때) 신호를 발생합니다.
  returnPressed()	Return/Enter 버튼이 눌릴 때 신호를 발생합니다.
  selectionChanged()	선택 영역이 바뀔 때 신호를 발생합니다.
  textChanged()	텍스트가 변경될 때 신호를 발생합니다.
  textEdited()	텍스트가 편집될 때 신호를 발생합니다.

}

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QHBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        self.lbl2 = QLabel(self)
        self.lbl2.move(170, 50)

        qle = QLineEdit(self)
        qle.move(130, 150)
        qle.textChanged[str].connect(self.onChanged)


        cb.activated[str].connect(self.onActivated) # 옵션을 선택하면, onActivated() 메서드가 호출

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize() # , adjustSize() 메서드를 이용해서 라벨의 크기를 자동으로 조절

    def onChanged(self, text):
        self.lbl2.setText(text)
        self.lbl2.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()