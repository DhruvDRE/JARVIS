#boltiot module for connecting server
# pywhatkit is used for youtube and other web protocoals
#sudo apt-get install python_setuptools
# git clone https://github.com/DexterInd/BrickPi_Python.git
# sudo python setup.py install 
# pyttsx3 , pyaudio and speech recognition class and libraries pip install
# for sharing of emails we need server of our own so we use smtp library
# for email funtionality we add email class from python
from email.message import EmailMessage # for setting ideals of email
import smtplib # server for the mail
import thingspeak as ts
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
from boltiot import Bolt
import sys
# for web applications
from PyQt5.QtWidgets import *  # they import application widgets
from PyQt5.QtWebEngineWidgets import * # they import all the widgets required >
from PyQt5.QtCore import *


#validating bolt iot keys

API_KEY = ""   # Bolt API Key
DEVICE_ID = "" # Bolt Device ID
mybolt=Bolt(API_KEY,DEVICE_ID)
#response=mybolt.digitalWrite("1","HIGH")

listener=sr.Recognizer()
engine=pt.init()
#voice tone conv
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
	engine.say(text)
	engine.runAndWait()

#take command
def take_command():
	try:
		with sr.Microphone() as source:
			voice=listener.listen(source)
			command=listener.recognize_google(voice)
			command=command.lower()
			if 'jarvis' in command:
				command=command.replace('jarvis',"")
				#print(command)
				return command
	except:
		pass


def run_jarvis():
	command=take_command()
	print(command)
	if 'search' in command:
		online_search(command)
	elif 'find' in command:
		online_search(command)
	elif 'email' in command:
		get_email_info()
	elif 'mail' in command:
		get_email_info()
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
			# self.setWindowIcon(QtGui.QIcon('logo.png'))# for setting icon of browser
			self.browser= QWebEngineView()
			self.browser.setUrl(QUrl("http://google.com/search?source=hp&q="+c+"/"))
			self.setCentralWidget(self.browser)
			self.showMaximized() #browser screen will be o
	app=QApplication(sys.argv) # to create an application
	QApplication.setApplicationName("KANAK") #Main app name
	window = MainWindow() # open and create window for app
	app.exec_() # to make this code into app execute

# for accessing email through voice 
def get_info():
	try:
		with sr.Microphone() as source:
			print('listening....')
			voice=listener.listen(source)
			info=listener.recognize_google(voice) #voice to text
			print(info)
			return info.lower()
	except:
		pass





def send_email(receiver,subject,message):
	# create a server
	server = smtplib.SMTP('smtp.gmail.com',587) # smtp server name and port number
	server.starttls() # start transport layer security
	server.login('','') #id and password
	# server.sendmail('piyushrparikh24@gmail.com','dhruvdre@gmail.com','this is mt automated mail for the emailbot') # sender,receiver and message
	email =EmailMessage()
	email['From']='' # your mail id
	email['To']= receiver
	email['Subject']=subject
	email.set_content(message)
	server.send_message(email)

#to create favourite email list 
email_list={
        'dude' : 'dhruvdre@gmail.com',
        'dad'  : 'piyushrparikh9@gmail.com',
        'mom'  : 'kananpparikh@gmail.com',
	'merin': 'merinshibu78@gmail.com',
	'friend': 'merinshibu78@gmail.com'     
 }


def get_email_info():
	talk('To Whom you want to send email to')
	name= get_info()
	receiver = email_list[name] # search input name in list 
#	receiver=name+"@gmail.com"
	print(receiver)
	talk("What is the subject of your email")
	subject= get_info()
	talk("tell me the content for the email")
	content= get_info()
	send_email(receiver,subject,content)




#while True:
#	run_jarvis()
run_jarvis()
