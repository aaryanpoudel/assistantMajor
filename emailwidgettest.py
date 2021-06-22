import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words,tokenize
import random
from ellle import sendmail
import os
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Splashscreen import Ui_MainWindow
from Starting import Ui_Starting
from Working import Ui_Working
from emaile import Ui_EmailWindow
import time
import threading
import datetime
import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr

class Email(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_EmailWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.ui.close.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.send)
        self.setWindowModality(QtCore.Qt.ApplicationModal)


    def send(self):
        emailadd=self.line_value()
        subject=self.line_value2()
        body=self.line_value3()
        sendmail(emailadd,subject,body)

    def line_value(self):
        # return text value of line edit
        return self.ui.lineEdit.text()
        print(self.ui.lineEdit.text())

    def line_value2(self):
        # return text value of line edit
        return self.ui.lineEdit_2.text()

    def line_value3(self):
        # return text value of line edit
        return self.ui.lineEdit_3.text()

    def close(self):
        sys.exit(0)

app=QApplication(sys.argv)
window=Email()
window.show()
app.exec_()