
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
from emaile import Ui_Dialog
import time
import threading
import datetime
import webbrowser
import pyttsx3
import wikipedia
import speech_recognition as sr
import subprocess
import pyowm
import pygame
from pyowm.utils import timestamps
import calendar
import playsound
from playsound import playsound
from pygame import mixer
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

sys.setrecursionlimit(3000)
n=0
Flag=False
emailflag=False
counter = 0
bot_name = "Arya"
song_list=["Prayforthem.mp3","raindrops.mp3","Slay.mp3"]


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def wish():
    current_time=time.localtime()
    if current_time[3] < 12 :
        engine.say("Good Morning!")
    elif current_time[3] in range(12,18):
        engine.say("Good Afternoon")
    else:
        engine.say("Good Evening")

class Splashscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow= QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.label_animation = QLabel(self)
        self.label_animation.setFixedSize(250, 300)
        self.label_animation.move(150, 150)
        self.movie = QMovie('taiga.gif')
        self.label_animation.setMovie(self.movie)

        mixer.init()
        mixer.music.load("loading.mp3")
        mixer.music.play(-1)

        timerg = QTimer(self)

        self.startanimation()
        timerg.singleShot(18000, self.stopanimation)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter>100:
            self.timer.stop()
            self.main=Starting()
            self.main.show()
            self.close()
        counter += 1



class Starting(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Starting()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.label_animation = QLabel(self)
        self.label_animation.setFixedSize(500,500)
        self.label_animation.move(100,00)
        self.movie = QMovie('Slptaiga.gif')
        self.label_animation.setMovie(self.movie)

        timerg = QTimer(self)

        self.startanimation()
        ##timerg.singleShot(18000, self.stopanimation)


        self.ui.pushButton.clicked.connect(self.b1_clicked)
        self.ui.close.clicked.connect(self.b2_clicked)

    def startanimation(self):
        mixer.init()
        mixer.music.load("bgm.mp3")
        mixer.music.play(-1)
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()

    def b1_clicked(self):
        click=mixer.Sound('click.mp3')
        click.play()
        global Flag
        Flag = True
        mixer.music.stop()
        #self.work=Works()
        #self.work.show()
        self.close()

    def b2_clicked(self):
        click=mixer.Sound('click.mp3')
        click.play()
        self.close()

app=QApplication(sys.argv)
window1=Splashscreen()
window1.show()
app.exec_()


class Works(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_Working()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.baseframe.setGraphicsEffect(self.shadow)

        self.label_animation = QLabel(self)
        self.label_animation.setFixedSize(700, 500)
        self.label_animation.move(328, 50)
        self.movie = QMovie('listen.gif')
        self.label_animation.setMovie(self.movie)

        self.ui.close.clicked.connect(self.b2_clicked)
        #timerg = QTimer(self)
        self.startanimation()
        #timerg.singleShot(3000, self.changegif)

    def b2_clicked(self):
        click=mixer.Sound('click.mp3')
        click.play()
        sys.exit(0)

    def changegif1(self):
        self.movie=QMovie('talk.gif')
        self.label_animation.setMovie(self.movie)
        self.startanimation()

    def changegif2(self):
        self.movie=QMovie('listen.gif')
        self.label_animation.setMovie(self.movie)
        self.startanimation()

    def startanimation(self):
        self.movie.start()

    def stopanimation(self):
        self.movie.stop()


class Email(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui=Ui_Dialog()
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
        #self.setWindowModality(QtCore.Qt.ApplicationModal)

    def send(self):
        emailadd=self.line_value()
        subject=self.line_value2()
        body=self.line_value3()
        sendmail(emailadd,subject,body)
        engine.say("The email has been sent successfully!")
        engine.runAndWait()
        self.work=Works()
        self.work.show()
        self.close()

    def line_value(self):
        # return text value of line edit
        return self.ui.add.text()

    def line_value2(self):
        # return text value of line edit
        return self.ui.subject.text()

    def line_value3(self):
        # return text value of line edit
        return self.ui.body.text()

    def closeer(self):
        sys.exit(0)


work=Works()
work.show()

wish()

while Flag == True:
    app.processEvents()
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{bot_name}: ""I am listening.")
        work.changegif2()
        work.ui.update_arya("I am listening.")
        app.processEvents()

        # app.processEvents()
        engine.say("I am listening.")
        engine.runAndWait()
        audio = r.listen(source, phrase_time_limit=7)
        try:
            print("You said:- " + r.recognize_google(audio))
            work.ui.update_user(r.recognize_google(audio))
            app.processEvents()
            app.processEvents()
            app.processEvents()
            app.processEvents()
            sentence = r.recognize_google(audio)
            sentence = tokenize(sentence)
            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X)

            output = model(X)
            _, predicted = torch.max(output, dim=1)
            tag = tags[predicted.item()]
            app.processEvents()
            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]
            app.processEvents()
            if prob.item() > 0.75:
                for intent in intents["intents"]:
                    if tag == intent["tag"]:
                        if tag == "time ask":
                            print(now.strftime(f"{bot_name}: ""The time is %H:%M"))
                            work.ui.update_arya(now.strftime(f"The time is %H:%M"))
                            engine.say(now.strftime("The time is %H:%M"))
                            work.changegif1()
                            app.processEvents()
                            app.processEvents()
                            app.processEvents()
                            engine.runAndWait()

                        elif tag=="worldnews":
                            print(f"{bot_name}: ""Bringing up the news")
                            engine.say("Bringing up the world news")
                            webbrowser.open('https://www.bbc.com/news/world')
                            engine.runAndWait()

                        elif tag=="goalnews":
                            engine.say("Bringing up the live scores")
                            webbrowser.open('https://www.goal.com/en/live-scores')
                            engine.runAndWait()

                        elif tag=="nepalnews":
                            print(f"{bot_name}: ""Bringing up the news")
                            engine.say("Bringing up Nepal's news")
                            webbrowser.open('https://kathmandupost.com/')
                            engine.runAndWait()

                        elif tag =="date ask":
                            print(now.strftime(f"{bot_name}: ""The date is %y-%m-%d"))
                            work.ui.update_arya(now.strftime(f"The date is %y-%m-%d"))
                            engine.say(now.strftime("Displaying today's date"))
                            work.changegif1()
                            app.processEvents()
                            engine.runAndWait()

                        elif tag == "song":
                            song=random.choice(song_list)
                            print(song)
                            song_name=song.replace(".mp3","")
                            print(song_name)
                            engine.say("Playing the song" + song_name)
                            engine.runAndWait()
                            playsound(song)

                        elif tag=="share":
                            engine.say("Opening Share sansar")
                            webbrowser.open('https://www.sharesansar.com/?show=home')
                            engine.runAndWait()

                        elif tag=="questionaire":
                            engine.say("Okay I will try my best to answer your questions. Say Thank You to stop asking questions")
                            work.ui.update_arya("Okay I will try my best to answer your questions. Say Thank You to stop asking questions")
                            app.processEvents()
                            engine.runAndWait()
                            app.processEvents()
                            t=sr.Recognizer()
                            statement="nothing"
                            while statement!= "thank you":
                                with sr.Microphone() as source:
                                    engine.say("Ask your question")
                                    work.ui.update_arya("Ask your question.")
                                    app.processEvents()
                                    engine.runAndWait()
                                    audii=t.listen(source,phrase_time_limit=7)
                                    try:
                                        statement = t.recognize_google(audii)
                                        print(statement)
                                        work.ui.update_user(statement)
                                        app.processEvents()
                                        app_id="Y9Q5JA-3V863KWPX3"
                                        client=wolframalpha.Client(app_id)
                                        res=client.query(statement)
                                        answer=next(res.results).text
                                        print("the answer is "+ answer)
                                        engine.say("the answer is "+ answer)
                                        work.ui.update_arya("The answer is "+ answer)
                                        app.processEvents()
                                        engine.runAndWait()
                                    except sr.UnknownValueError:
                                        engine.say("I didn't understand your question.")
                                        engine.runAndWait()
                                        break


                        elif tag == "weathercheck":
                            owm = pyowm.OWM('3693169274e8597dcefd15d1166f7c02')
                            mgr = owm.weather_manager()
                            observation = mgr.weather_at_place('Kathmandu, NP')
                            w = observation.weather
                            print(w.detailed_status)
                            temp_dict_celsius = w.temperature('celsius')
                            print(temp_dict_celsius)
                            print(temp_dict_celsius['temp'])
                            wind_dict_in_meters_per_sec = observation.weather.wind()
                            print(wind_dict_in_meters_per_sec)
                            print(wind_dict_in_meters_per_sec['speed'])
                            rain_dict = observation.weather.rain
                            print(rain_dict)
                            #print(rain_dict['1h'])
                            work.changegif1()
                            app.processEvents()
                            engine.say("Today's weather is "+ w.detailed_status)
                            work.ui.update_arya("Today's weather is "+ w.detailed_status+".")
                            app.processEvents()
                            engine.runAndWait()
                            engine.say("Today's temperature is"+ str(temp_dict_celsius['temp'])+" degree celsius")
                            work.ui.update_arya("Today's temperature is "+ str(temp_dict_celsius['temp'])+" degree celsius.")
                            app.processEvents()
                            engine.runAndWait()
                            engine.say("Today's windspeed is"+ str(wind_dict_in_meters_per_sec['speed'])+"meters per second")
                            work.ui.update_arya("Today's windspeed is "+ str(wind_dict_in_meters_per_sec['speed'])+" meters per second.")
                            app.processEvents()
                            engine.runAndWait()
                            if float(wind_dict_in_meters_per_sec['speed'])>20:
                                engine.say("today is rather windy")
                                work.ui.update_arya("Today is rather windy.")
                                app.processEvents()
                            engine.runAndWait()

                        elif tag == "raincheck":
                            owm = pyowm.OWM('3693169274e8597dcefd15d1166f7c02')
                            mgr = owm.weather_manager()
                            three_h_forecaster = mgr.forecast_at_place('Kathmandu,NP', '3h')
                            tomorrow = timestamps.tomorrow()
                            three_h_forecaster.will_be_rainy_at(tomorrow)
                            work.changegif1()
                            app.processEvents()
                            if three_h_forecaster.will_be_rainy_at(tomorrow)==True:
                                engine.say("Let me check. Ah yes, it will rain tomorrow")
                                work.ui.update_arya("Let me check. Ah yes, it will rain tomorrow")
                                app.processEvents()
                            else:
                                engine.say("Let me check. No, it doesnt look like it will rain tomorrow")
                                work.ui.update_arya("Let me check. No, it doesnt look like it will rain tomorrow")
                                app.processEvents()
                            engine.runAndWait()

                        elif tag == "calculator":
                            subprocess.call('calc.exe')
                            work.changegif1()
                            app.processEvents()
                            engine.say("Opening Calculator")
                            work.ui.update_arya("Opening Calculator.")
                            app.processEvents()
                            engine.runAndWait()

                        elif tag == "google search":
                            tabUrl="https://google.com/?#q="
                            said=r.recognize_google(audio)
                            #print(said)
                            qury=said.replace("find me the","")
                            qury=qury.replace("search the internet for","")
                            qury=qury.replace("search google for","")
                            qury=qury.replace("Google","")
                            print(f"the query is: {qury}")
                            webbrowser.open('https://google.com/search?q=' + qury)
                            work.changegif1()
                            app.processEvents()
                            work.ui.update_arya("Bringing up the search")
                            work.ui.update_user("...")
                            app.processEvents()
                            app.processEvents()
                            app.processEvents()
                            engine.say("Bringing up the search")
                            engine.runAndWait()

                        elif tag == "open youtube":
                            work.changegif1()
                            app.processEvents()
                            work.ui.update_arya("Opening youtube in your default browser")
                            app.processEvents()
                            engine.say("Opening youtube in your default browser")
                            webbrowser.open('www.youtube.com')
                            engine.runAndWait()

                        elif tag == "facebook":
                            work.changegif1()
                            app.processEvents()
                            work.ui.update_arya("Opening facebook in your default browser")
                            app.processEvents()
                            engine.say("Opening facebook in your default browser")
                            webbrowser.open('www.facebook.com')
                            engine.runAndWait()

                        elif tag == "send email":
                            #global emailflag
                            work.close()
                            maile=Email()
                            maile.exec_()
                            #maile.show()

                            app.processEvents()
                            #add=input("Enter the email id of reciever")
                            #subject=input("Enter the subject of the email")
                            #body=input("Enter the body of the email")
                            #sendmail(add,subject,body)
                            #engine.say("Your email has been sent successfully")
                            #work.ui.update_arya("Your email has been sent successfully")
                            #work.ui.update_user("...")
                            #work.changegif1()
                            app.processEvents()
                            engine.runAndWait()

                        elif tag == "calendar":
                            work.changegif1()
                            app.processEvents()
                            yy = 2021
                            mm = 3
                            print(calendar.month(yy, mm))
                            engine.say("Showing Calendar")
                            work.ui.update_arya("Showing Calendar...")
                            app.processEvents()
                            engine.runAndWait()


                        elif tag == "quit":
                            engine.say("Thank you for using me!")
                            work.ui.update_arya("Than you for using me!")
                            app.processEvents()
                            engine.runAndWait()
                            sys.exit(0)

                        elif tag == "ending":
                            rep = random.choice(intent['responses'])
                            print(rep)
                            work.ui.update_arya(rep)
                            work.changegif1()
                            engine.say(rep)
                            app.processEvents()
                            engine.runAndWait()
                            sys.exit(0)

                        else:
                            rep = random.choice(intent['responses'])
                            print(rep)
                            work.ui.update_arya(rep)
                            work.changegif1()
                            app.processEvents()
                            engine.say(rep)
                            app.processEvents()
                            engine.runAndWait()
            else:
                work.ui.update_arya("I didnt find it in my database. Would you like to search about it online?")
                app.processEvents()
                app.processEvents()
                app.processEvents()
                engine.say("I didnt find it in my database. Would you like to search about it online?")
                work.changegif1()

                app.processEvents()
                # print(f"{bot_name}: ""I didnt find it in my database. Would you like to search about it online?")
                engine.runAndWait()
                pr = sr.Recognizer()
                with sr.Microphone() as source:
                    audi = pr.listen(source, phrase_time_limit=5)
                    repp = pr.recognize_google(audi)
                    # print(repp)
                    if repp == "yes" or repp == "sure" or repp == "okay" or repp == "yeah" or repp == "why not" or repp == "please do":
                        work.ui.update_user(repp)
                        # print(f"{bot_name}:" "You said yes so here you go.")
                        work.ui.update_arya("You said yes so here you go.")

                        app.processEvents()
                        engine.say("You said yes so here you go.")
                        try:
                            # print(wikipedia.summary(sentence))
                            work.ui.update_arya(wikipedia.summary(sentence))
                            work.changegif1()
                            app.processEvents()
                            engine.say(wikipedia.summary(sentence))
                            engine.runAndWait()
                        except wikipedia.DisambiguationError as e:
                            engine.say("The topic you wanted to search in wikipedia is disambiguos. So I will search it in google instead.")
                            work.ui.update_arya("The topic you wanted to search in wikipedia is disambiguos. So I will search it in google instead.")
                            app.processEvents()
                            tabUrl = "https://google.com/?#q="
                            said = r.recognize_google(audio)
                            # print(said)
                            qury = said.replace("find me the", "")
                            qury = qury.replace("search the internet for", "")
                            qury = qury.replace("search google for", "")
                            qury = qury.replace("Google", "")
                            print(f"the query is: {qury}")
                            webbrowser.open('https://google.com/search?q=' + qury)
                            work.ui.update_arya("Bringing up the search")
                            work.ui.update_user("...")
                            app.processEvents()
                            app.processEvents()
                            app.processEvents()
                            engine.say("Bringing up the search")
                            engine.runAndWait()



                    else:
                        # print(f"{bot_name}: ""Okay then moving on.")
                        work.ui.update_arya("Okay then moving on.")
                        work.changegif1()

                        app.processEvents()
                        engine.say("okay then moving on.")
                        engine.runAndWait()

        except sr.UnknownValueError:
            engine.runAndWait()
            # print(f"{bot_name}: ""Could not understand audio")
            work.ui.update_arya("I didnt get that")
            work.ui.update_user("...")
            app.processEvents()
            engine.say('I didnt get that')
            engine.runAndWait()
            n = n + 1
            if n >= 5:
                # print(f"{bot_name}: ""It seems that you are preoccupied. So I'll see you later.")
                work.ui.update_arya("It seems that you are preoccupied. So I'll see you later.")
                work.changegif1()
                app.processEvents()
                engine.say("It seems that you are preoccupied. So I'll see you later")
                engine.runAndWait()
                break
