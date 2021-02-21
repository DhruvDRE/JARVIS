# boltiot module for connecting server
# pywhatkit is used for youtube and other web protocoals
# sudo apt-get install python_setuptools
# sudo python setup.py install 
# pyttsx3 , pyaudio and speech recognition ,qtwidgets, qtwebenginewidgets class and libraries pip install for base requirnments of the work
import thingspeak as ts
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
from boltiot import Bolt
import sys
# for web applications
from PyQt5.QtWidgets import *  # they import application widgets
from PyQt5.QtWebEngineWidgets import * # they import all the widgets required 
from PyQt5.QtCore import *


#Future aspects for home automation with jarvis

API_KEY = ""   # Bolt API Key
DEVICE_ID = "" # Bolt Device ID
# mybolt=Bolt(API_KEY,DEVICE_ID) #remove comment when you want to use bolt setup
#response=mybolt.digitalWrite("1","HIGH")
#for any appliance you want to control with that pin on bolt 

listener=sr.Recognizer()
engine=pt.init()
#voice tone conversion
# 1-- female
# 0-- male
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#function will talk out any text u want to show
def talk(text): 
	engine.say(text)
	engine.runAndWait()

#take command from the user and replace jarvis or any name the want to give their assistant
def take_command():
	try:
		with sr.Microphone() as source:
			voice=listener.listen(source)
			command=listener.recognize_google(voice)
			command=command.lower()
      # the name jarvis can be changed to any name you want to give your voice assistant change that in nxt two line
			if 'jarvis' in command: 
				command=command.replace('jarvis',"")
				#print(command)
	except:
		pass
	return command
# main program that will control every funtionality
def run_jarvis():
	command=take_command()
	print(command)
	if 'search' or 'find' in command:
		online_search(command)
	elif 'stop' in command:
		talk("Okay, I will be waiting for your next command")
		sys.exit()
	elif 'quit' in command:
		talk("Okay, I am leaving will be available at your service")
		sys.exit()
	elif 'end' in command:
		talk("Okay , see you soon again")
		sys.exit()
	elif 'play' in command:
		song=command.replace('play','')
		talk("playing "+song)
		pk.playonyt(song)
	elif 'turn on' in command:
		tt=command.replace('turn on','')
		talk("turning the "+command+" On ")
		if 'fan' in tt:
			talk("turning on the burner")
			print("turning on the burner")
		elif 'lights' in tt:
			talk("turning on the lights ")
			print("turing on lights") 
	elif '' in command:
		pass
	else:
		pass
def online_search(command):
	c=command.replace("search","")
	c=command.replace("find","")
	class MainWindow(QMainWindow):
		def __init__(self):
			super(MainWindow,self).__init__()
			self.browser= QWebEngineView()
			self.browser.setUrl(QUrl("http://google.com/search?source=hp&q="+c+"/"))
			self.setCentralWidget(self.browser)
			self.showMaximized() #browser screen will be o
	app=QApplication(sys.argv) # to create an application
	QApplication.setApplicationName("KANAK") #Main app name you can define your own webbrowser name
	window = MainWindow() # open and create window for app
	app.exec_() # to make this code into app execute



while True:
	run_jarvis()

