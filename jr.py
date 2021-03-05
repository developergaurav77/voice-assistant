import pyttsx3  #importing this module to convert text to speech
import datetime #importing this module to use date and time
import speech_recognition as sr #importing this module to convert speech into text
import smtplib  #importing this module to send emails
from secret import senderEmail, epwd, to #importing sender email id(senderEmail), password(epwd) and receiver email id(to)
from email.message import EmailMessage #importing to send message and subject 
import pyautogui
import webbrowser as web  #importing this module to open different website
from time import sleep  #importing this module to sleep the part of program for some time
import wikipedia  #importing this module to search anything on wikipedia using word 'wikipedia'
import pywhatkit  #importing this module to open video on youtube
import pyperclip  #importing this module to convert selected text to speech
import os         #importing this module to access the file location in computer



engine = pyttsx3.init() # object creation

""" RATE"""
engine.getProperty('rate')   # getting details of current speaking rate
voiceRate = 180
engine.setProperty('rate', voiceRate)     # setting up new voice rate



def speak(audio): #this function to used to speak
    engine.say(audio)
    engine.runAndWait()
    
def time():  #this function is used to calculate current time
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speak("the current time is ")
    speak(time)

def date():  #this function is used to calculate current date
    year = int(datetime.datetime.now().year) 
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("today date is")
    print(year,month,day)
    speak(year)
    speak(month)
    speak(day)  

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12 :
        print('good morning')
        speak('good morning sir!')    
    elif hour >=12 and hour <18 :
        print('good afternoon')
        speak('good afternoon sir!')
    elif hour >=18 and hour < 24 :
        print('good evening')
        speak('good evening sir!')
    else:
        print('good night sir! its time to sleep')
        speak('good night sir! its time to sleep')    

def wishMe(): #this is used to initiate the program
    print('welcome back sir!')
    speak('welcome back sir!')    
    time()
    date() 
    greeting()
    speak('junior, at your service , please tell me how can i help you sir?')

def takeCommandTer():
    query = input('Please tell me, how can help you sir? \n')  
    return query

def takeCommandMic():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      audio = r.listen(source)  
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        #speak('Say that again please')
        print('Say that again please')
        
        return 'None'
    return query

def sendEmail(receiver,subject,content):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls 
    server = smtplib.SMTP(smtp_server,port)   
    server.starttls()
    server.login(senderEmail,epwd)
    email = EmailMessage()
    email['From'] = senderEmail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

def searchGoogle():
    print('Searching on google')
    speak('what should i search on google')
    search = takeCommandMic().lower()
    print(search)
    
    web.open('https://www.google.com/search?q='+search)

def textToSpeech(): 

    text = pyperclip.paste()
    print('sure')
    speak('sure')
    print(text)
    speak(text)   
    


if __name__ == "__main__" :
    wishMe()
    while True:
        shutdown = 'offline'
        
        query = takeCommandMic().lower()
        if 'time' in  query:
            time()
        elif 'date' in query:
            date()

        elif shutdown in query:
            speak('closing the program')
            exit() 

        elif 'who are you' in query:
            speak('i am voice assistant, created by gaurav! using python programming language')    
        elif 'how are you' in query:
            speak('i am fine and hope you are also doing well sir!!')
        elif 'hello' in query:
            speak('ohh hello sir, please tell me how can i help you?')    
        elif 'junior' in query:
            speak('yes sir, how can i help you?')
        elif 'open' in query:
            query = query.replace('open',"")
            print('Opening'+query)
            speak('opening '+query) 
            link = 'https://www.' + query + ' .com/'
            link = link.replace(" ", "")
            print(link)
            web.open(link, new=0, autoraise=True)
          

          

        elif 'wikipedia' in query:
            print('Searching on wikipedia')
            speak('Searching on wikipedia')
            query = query.replace('wikipedia'," ")
            result = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'search' in query:
            query = query.replace('google'," ")
            query = query.replace('search'," ")
            query = query.replace('on', " ")
            web.open('https://www.google.com/search?q='+query)
            sleep(2)  

        elif 'google search' in query:
            web.open('https://www.google.com/') 
            sleep(1)
            searchGoogle()

        elif 'play video on youtube' in query:
            web.open('https://www.youtube.com/')
            speak('opening youtube')
            sleep(2)
            print('what should i play on youtube?')
            speak('what should i play on youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic) 

        elif 'youtube' in query:
            web.open('https://www.youtube.com/') 
            speak('opening youtube')

        elif 'mail' in query:
            web.open('https://mail.google.com/')
            speak('opening gmail')


        elif 'read' in query:
            textToSpeech()

        elif 'code' in query:
            codepath = 'C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            print('opening vs code')
            speak('opening vs code')
            os.startfile(codepath)

        elif 'spotify' in query:
            codepath2 = 'C:\\Users\\GAURAV\\AppData\\Roaming\\Spotify\\Spotify.exe'
            print('opening Spotify')
            speak('opening Spotify')
            os.startfile(codepath2)
        
        elif 'android studio' in query:
            codepath3 = 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'
            print('opening Android Studio')
            speak('opening android studio')
            os.startfile(codepath3)

        elif 'pro' in query:
            codepath4 = 'C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe'
            print('opening premier pro')
            speak('opening premier pro')
            os.startfile(codepath4)

        elif 'documents' in query:
            try:
                print('Opening...')
                speak('Opening...')
                os.system('explorer C://{}'.format(query.replace('Open',' ')))
               
            except Exception as e:
                print(e)
               #speak('Say that again please')
                print('can you please repeat again!')
        elif 'send email' in query:
            email_list = {
                
                'bishal' : 'bishalkhatri675@gmail.com',
                'bhupesh' : 'bhupeshjoshi293@gmail.com',
                'ayush' : 'joshiayush20582059@gmail.com'

            }
            try:
                speak('To whom you want to send the mail')
                name = takeCommandMic().lower()
                print(name)
                receiver = email_list[name]
                speak('what should be the subject of mail sir?')
                subject = takeCommandMic()
                speak('what should i write in mail sir?')
                content = takeCommandMic()
                sendEmail(receiver,subject,content)
                speak('email sent successfully')
            except Exception as e:
                print(e)    
                speak('unable to send email')
       
                