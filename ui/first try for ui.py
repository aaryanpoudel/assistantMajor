import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QMovie




class Loadingscreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(220,220)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.label_animation = QLabel(self)
        self.movie= QMovie('tenor.gif')
        self.label_animation.setMovie(self.movie)

        timer = QTimer(self)

        self.startanimation()
        timer.singleShot(3000,self.stopanimation)

        self.show()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()
        self.close()





class Appdemo(QWidget):
    def __init__(self):
        super().__init__()

        label= QLabel('<font size=12> this is main app window </font>',self)
        label.setGeometry(150,150,300,50)

        b1= QPushButton("load gif",self)
        b1.setCheckable(True)
        b1.clicked.connect(self.btn_clik)

    def btn_clik(self):
        print("the button was pressed")
        self.giff = Loadingscreen()
        self.close()
        #self.show()

        #self.gif = Loadingscreen()
        #self.show()




app = QApplication(sys.argv)
demo=Appdemo()
demo.show()
app.exit(app.exec_())