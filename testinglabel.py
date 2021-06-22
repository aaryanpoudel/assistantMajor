import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from untitled import Ui_MainWindow
from PyQt5 import QtCore
import os

class Start(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.movie = QMovie('ken.gif')
        self.ui.label.setMovie(self.movie)

        timerg = QTimer(self)

        self.startanimation()
        timerg.singleShot(18000, self.stopanimation)

        self.show()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()


app=QApplication(sys.argv)
demo=Start()
app.exec_()
