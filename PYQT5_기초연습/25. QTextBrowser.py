"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

25. QTextBrowser

QTextBrowser: 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 (서식있는 텍스트) 브라우저를 제공
{
  - QTextEdit의 확장형으로서 하이퍼텍스트 문서의 링크들을 사용(
  - 오로지 읽기 전용, 편집할려면 QTextEdit을 사용함
  - 하이퍼텍스트 네비게이션이 없는 텍스트 브라우저를 사용하기 위해서는 QTextEdit을 setReadOnly()를 사용해서 편집이 불가능하도록 해줌
  - 짧은 리치 텍스트를 표시하기 위해서는 QLabel을 사용
}
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit() # 줄 편집기
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True) # setAcceptRichText()를 True로 설정해주면, 서식 있는 텍스트 (Rich text)를 사용(디폴트=True)
        self.tb.setOpenExternalLinks(True) # 외부 링크로의 연결이 가능

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()


    def clear_text(self):
        self.tb.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())