import sys
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent, QResizeEvent
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *

class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        self.count = 0
        self.sub_window = SubWidget(self)

        self.scene = QGraphicsScene(self)

        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)

        vl = QVBoxLayout(self)
        vl.addWidget(self.view)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print(f'Main Widget:{self}')
        self.sub_window.show()
        return super().mousePressEvent(a0)
    
    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.scene.setSceneRect(QRectF(0, 0, self.view.size().width() - 2, self.view.size().height() - 2))
        return super().resizeEvent(a0)
    
class SubWidget(QWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.setGeometry(500, 500, 150, 150)

        self.on_btn = QPushButton('On')
        self.on_btn.clicked.connect(lambda : self.call_mainwindow_count_change('On'))
        self.off_btn = QPushButton('Off')
        self.off_btn.clicked.connect(lambda : self.call_mainwindow_count_change('Off'))

        vl = QVBoxLayout(self)
        vl.addWidget(self.on_btn)
        vl.addWidget(self.off_btn)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        print(f'Sub Widget:{self}')
        print(f'Sub Widget:{self.parent}')
        return super().mousePressEvent(a0)
    
    def call_mainwindow_count_change(self, strategy):
        self.parent.count = 1 if strategy == 'On' else 0            
        print(self.parent.count)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = MainWidget()
    exe.show()
    sys.exit(app.exec_())