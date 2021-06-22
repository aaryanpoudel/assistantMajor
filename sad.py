import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

class Window(QWidget):



    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        button = QPushButton(self.tr("Click me!"))
        button.clicked.connect(self.fade)
        layout = QVBoxLayout(self)
        layout.addWidget(button)

    def fade(self):
        self.setWindowOpacity(0.5)
        QTimer.singleShot(1000, self.unfade)

    def unfade(self):
        self.setWindowOpacity(1)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())