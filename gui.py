import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from playsound import playsound
app = QApplication(sys.argv)

due = input("Enter the time for alert (format: hh:mm): ")
message = input("Enter message for alert")

try:
	hours,mins= due.split(":")
	due = QTime(int (hours), int (mins))
	if not due.isValid():
		raise ValueError
except ValueError:
	message = "Invalid time"

while QTime.currentTime()<due:
	time.sleep(20)

label = QLabel("<font color = red size = 36><b>" + message+ "</b></font>")
label.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
label.show()
playsound("alarm.mp3")
QTimer.singleShot(60000,app.quit)
sys.exit(app.exec_())