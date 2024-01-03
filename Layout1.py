import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGridLayout

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setGeometry(100, 100, 1000, 500)

        vertical_L = QVBoxLayout(self)

        hl = QHBoxLayout()
        hl.addWidget(UnitWidget_H(self, 'btn1'))
        hl.addWidget(UnitWidget_H(self, 'btn2'))
        hl.addWidget(UnitWidget_H(self, 'btn3'))

        gl = QGridLayout()
        gl.addWidget(UnitWidget_G(self, 1), 0,0)
        gl.addWidget(UnitWidget_G(self, 2), 0,1)
        gl.addWidget(UnitWidget_G(self, 3), 1,0)
        gl.addWidget(UnitWidget_G(self, 4), 1,1)

        vertical_L.addLayout(hl)
        vertical_L.addLayout(gl)

        
        
class UnitWidget_H(QWidget):
    def __init__(self, parent, name:str) -> None:
        super().__init__(parent)

        vl = QVBoxLayout(self)
        
        self.btn1 = QPushButton(name)

        vl.addWidget(self.btn1)

class UnitWidget_G(QWidget):
    def __init__(self, parent, number:int) -> None:
        super().__init__(parent)

        vl = QVBoxLayout(self)

        label = QLabel(self)
        label.setText(f'Value is {number}')
        
        vl.addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = MainWindow()
    exe.show()
    sys.exit(app.exec_())