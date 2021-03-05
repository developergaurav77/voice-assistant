import pyttsx3  #importing this module to convert text to speech
import datetime #importing this module to use date and time
import speech_recognition as sr #importing this module to convert speech into text
import smtplib  #importing this module to send emails
from secret import senderEmail, epwd, to #importing sender email id(senderEmail), password(epwd) and receiver email id(to)
from email.message import EmailMessage #importing to send message and subject 
import pyautogui
import webbrowser as web
from time import sleep


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
        query = r.recognize_google(audio,language='en-IN')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again please')
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

if __name__ == "__main__" :
   # wishMe()
    while True:
        
        query = takeCommandMic().lower()
        if 'time' in  query:
            time()
        elif 'date' in query:
            date()

        elif 'exit' in query:
            speak('closing the program')
            exit()   
      
        elif 'messenger' in query:
            speak('opening messenger') 
            web.open('https://www.messenger.com/')  
            sleep(5)

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
       
                