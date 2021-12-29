"""
PYQT5 프로젝트 연습
사용자: 박성우
날짜: 2021/12/30

17. QProgressbar


QProgressBar 위젯: 수평, 수직의 진행 표시줄을 제공
{
 -  setMinimum()과 setMaximum() 메서드로 진행 표시줄의 최소값과 최대값을 설정
 -  setRange() 메서드로 한 번에 범위를 설정(기본값은 0과 99)
 -  setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고, reset() 메서드는 초기 상태로 되돌림
 - 진행 표시줄의 최소값과 최대값을 모두 0으로 설정하면,
   행 표시줄은 위의 그림과 같이 항상 진행 중인 상태로 표시됩니다.
   이 기능은 다운로드하고 있는 파일의 용량을 알 수 없을 때 유용하게 사용함
}

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() # 진행 표시줄을 활성화하기 위해, 타이머 객체를 사용
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e): # 타이머 실행할때 계속 호출하는 함수
        if self.step >= 100:
            self.timer.stop() # 타이머 멈춰
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self): # 버튼을 클릭하여 타이머 상태를 확인함
        if self.timer.isActive(): # 타이머가 활성화 되어 있으면
            self.timer.stop() # 타이머를 멈추고
            self.btn.setText('Start') # start로 버튼을 변경
        else:
            self.timer.start(100, self) # 100은 종료시간(10초), 두번째 인자는 이벤트가 수행될 객체
            self.btn.setText('Stop')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())