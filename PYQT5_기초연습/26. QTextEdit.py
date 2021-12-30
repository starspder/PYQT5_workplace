"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

26. QTextEdit

QTextEdit: 플레인 텍스트 (plain text)와 리치 텍스트 (rich text)를 모두 편집하고 표시할 수 있는 편집기를 제공
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence: ')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False) # 모두 플레인 텍스트로 인식
        self.lbl2 = QLabel('The number of  words is 0')

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

