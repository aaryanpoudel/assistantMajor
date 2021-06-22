import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

#
class Appdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,1000)
        layout = QVBoxLayout()

        label= QLabel('<font size=12> this is main app window </font>',self)
        label.setGeometry(200,650,500,50)

        self.label_animation = QLabel(self)
        self.movie = QMovie('listen.gif')
        self.label_animation.setMovie(self.movie)

        timerg = QTimer(self)

        self.startanimation()
        #timerg.singleShot(3, self.changegif)


        b1 =QPushButton("Change Gif",self)
        b1.clicked.connect(self.changegif)
        b1.setGeometry(200,600,500,50)
        self.startanimation()
        self.show()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()

    def changegif(self):
        self.movie=QMovie('talk.gif')
        self.label_animation.setMovie(self.movie)
        self.startanimation()


app = QApplication(sys.argv)
demo=Appdemo()
app.exit(app.exec_())