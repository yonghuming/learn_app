import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
