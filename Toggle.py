import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Button(QPushButton):
    """
    QPushButton 은 QWidget을 상속받고 있으므로 단일 창으로 표출 가능
    """
    def __init__(self):
        QPushButton.__init__(self, "OFF")
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-color: red")

        self.setCheckable(True)
        self.toggled.connect(self.slot_toggle)



    def slot_toggle(self, state):
        """
        toggle 상태에 따라 배경색과 상태 텍스트 변환
        """
        self.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))
        self.setText({True: "ON", False: "OFF"}[state])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Button()
    form.show()
    exit(app.exec_())