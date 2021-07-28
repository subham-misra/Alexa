import speech_recognition as sr
#import pywhatkit
import wikipedia
import datetime
import sys
import pyjokes
import pyttsx3
import webbrowser
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from alexaui import Ui_MainWindow

# voice recognize
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice", "english")
# saying responce
def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning ,subham!")

    elif hour>=12 and hour<18:
        talk("Good after noon ,subham!")

    else:
        talk("Good evening ,subham !")

    talk("i am alexa 2.0 , please tell me  subham how may i help you ")

class mainthread(QThread):
    def __init__(self):
        super(mainthread, self).__init__()

    def run(self):
            self.run_geekspeak()


    def take_command(self):
        try:
            with sr.Microphone() as source:
                # listener = sr.Recognizer()
                listener.adjust_for_ambient_noise(source, duration=2)
                print("listening................")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()

                print(command)
        except:
            command = "not recognized sir"

        return command

# command interpretation

    def run_geekspeak(self):
        wishMe()
        #while True:
        #
        #self.command = self.take_command()
        #self.command = self.run_geekspeak()
        print(self.command)

        if 'wikipedia' in self.command:
            talk('Searching Wikipedia.....')
            self.command = self.command.replace("wikipedia", "")
            results = wikipedia.summary(self.command, sentences=2)
            print(results)
            talk(results)
        elif 'open youtube' in self.command:
            webbrowser.open("youtube.com")

        elif 'open google' in self.command:
            webbrowser.open("google.com")

        elif 'play music' in self.command:
            music_dir='C:\\Users\\dell\\Music\\12 Baarish - Atif Aslam (Half Girlfriend) 190Kbps'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir))

        elif 'the time' in self.command:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"Sir the time is {strTime}")

        elif 'about me' in self.command:
            talk("sir apnar name subham misra apnar babar name sankar prasad misra apnar maa er name archana misra apni akjon coder web developer apni drawing korta khub valo basan apni apnar family ta sobai ka valo basan apnar bon er name patla misra oa apnaka khub disturb kora  apni game khalta khub valo basan apni boro hoha software engineer hota chan  ")

        elif 'about you' in self.command:
            talk("sir i am alexa 2.0 coded by you,you have given me this wonder full life,i can do many things wishyou wikipedia open google youtube playing music time sending mess...")


# saying response
while True:
    p = mainthread()
    p.run_geekspeak()


    startExecution = mainthread()

    class Main(QMainWindow):

        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton.clicked.connect(self.close)

        def startTask(self):
            self.ui.movie = QtGui.QMovie("images/back.gif")
            self.ui.label.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("images/bar.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start()
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(1000)
            startExecution.start()

        def showTime(self):
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(label_date)
            self.ui.textBrowser_2.setText(label_time)


    app = QApplication(sys.argv)
    alexa = Main()
    alexa.show()
    exit(app.exec())