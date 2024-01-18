import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class mainwindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 800, 800)

        self.btn1 = QPushButton('Test', self)
        self.btn1.setGeometry(60, 100, 384, 548)
        self.btn1.setStyleSheet("border-radius: 55px; background: #FF0303;")
        
        self.btn2 = QPushButton("text", self)
        self.btn2.setGeometry(112, 127, 280, 176)
        self.btn2.setStyleSheet("\
                                QPushButton{border-radius: 20px;border: 1px solid rgba(0, 0, 0, 0.20);background: #FFF;}\
                                QPushButton:hover{background: #FFA2A2;}\
                                QPushButton:pressed{background: #00FFC2;}\
                                ")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = mainwindow()
    exe.show()
    sys.exit(app.exec_())