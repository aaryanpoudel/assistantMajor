import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

#
class Appdemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,500)
        layout = QVBoxLayout()

        label= QLabel('<font size=12> this is main app window </font>',self)
        label.setGeometry(150,150,500,50)

        self.label_animation = QLabel(self)
        self.movie = QMovie('ken.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)

        self.startanimation()
        timer.singleShot(18000, self.stopanimation)

        self.b1 =QPushButton("Change Gif")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda: self.whichbtn(self.b1))
        layout.addWidget(self.b1)
        self.show()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()
        self.close()

        self.gift = Loadingscreen()
        self.show()

app = QApplication(sys.argv)
demo=Appdemo()
app.exit(app.exec_())