# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ellle import sendmail


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(906, 368)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 886, 350))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(170, 170, 255);\n"
"    color: rgb(211, 212, 255);\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addlabel = QtWidgets.QLabel(self.frame)
        self.addlabel.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addlabel.setFont(font)
        self.addlabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.addlabel.setObjectName("addlabel")
        self.sublabel = QtWidgets.QLabel(self.frame)
        self.sublabel.setGeometry(QtCore.QRect(20, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sublabel.setFont(font)
        self.sublabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.sublabel.setObjectName("sublabel")
        self.bodylabel = QtWidgets.QLabel(self.frame)
        self.bodylabel.setGeometry(QtCore.QRect(20, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bodylabel.setFont(font)
        self.bodylabel.setStyleSheet("color: rgb(0, 0, 0);")
        self.bodylabel.setObjectName("bodylabel")
        self.add = QtWidgets.QLineEdit(self.frame)
        self.add.setGeometry(QtCore.QRect(180, 20, 651, 41))
        self.add.setObjectName("add")
        self.subject = QtWidgets.QLineEdit(self.frame)
        self.subject.setGeometry(QtCore.QRect(180, 70, 651, 41))
        self.subject.setObjectName("subject")
        self.body = QtWidgets.QLineEdit(self.frame)
        self.body.setGeometry(QtCore.QRect(180, 130, 651, 101))
        self.body.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.body.setObjectName("body")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 250, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.5, stop:0 rgba(255, 170, 255, 255), stop:0.0909091 rgba(255, 170, 255, 255), stop:0.9375 rgba(254, 255, 244, 255));\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.close = QtWidgets.QPushButton(self.frame)
        self.close.setGeometry(QtCore.QRect(840, 0, 41, 41))
        self.close.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"border-radius: 10px;")
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/chatbot assests/1200px-Flat_cross_icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setIconSize(QtCore.QSize(32, 32))
        self.close.setObjectName("close")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addlabel.setText(_translate("Dialog", "<html><head/><body><p>Reviever\'s Email:</p></body></html>"))
        self.sublabel.setText(_translate("Dialog", "Subject:"))
        self.bodylabel.setText(_translate("Dialog", "Email Content:"))
        self.pushButton.setText(_translate("Dialog", "Send Email"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
