import pyttsx3  #importing this module to convert text to speech
import datetime #importing this module to use date and time
import speech_recognition as sr #importing this module to convert speech into text
import smtplib  #importing this module to send emails
from secret import senderEmail, epwd, to #importing sender email id(senderEmail), password(epwd) and receiver email id(to)
from email.message import EmailMessage #importing to send message and subject 
import pyautogui          #importing this module for screenshort
import webbrowser as web  #importing this module to open different website
from time import sleep  #importing this module to sleep the part of program for some time
import wikipedia  #importing this module to search anything on wikipedia using word 'wikipedia'
import pywhatkit  #importing this module to open video on youtube
import pyperclip  #importing this module to convert selected text to speech
import os         #importing this module to access the file location in computer
import pyjokes    #imorting this module to get jokes
import time as tt 
import psutil #importing this module to get the system information
from playsound import playsound  #importing this module to play music from computer
import random
from openpyxl import Workbook
import calendar

engine = pyttsx3.init() # object creation

""" RATE"""
engine.getProperty('rate')   # getting details of current speaking rate
voiceRate = 190
engine.setProperty('rate', voiceRate)     # setting up new voice rate

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)


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
def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th','14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    print('Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1]) 
    speak('Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1])  

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12 :
        print('good morning')
        speak('good morning sir!') 
        speak('How can i help you sir?')
       
    elif hour >=12 and hour <18 :
        print('good afternoon')
        speak('good afternoon sir!')
        speak('How you doing today? and how can i help you sir?')
    elif hour >=18 and hour < 24 :
        print('good evening')
        speak('good evening sir!')
        speak('How was your day sir?')
    else:
        print('good night sir! its time to sleep')
        speak('good night sir! its time to sleep')
        speak('But we can interact for some time!')    

def wishMe(): #this is used to initiate the program
    print('welcome back sir!')
    speak('welcome back sir!')    
    time()
    date()
    speak('junior, at your service , please tell me how can i help you sir?')

def takeCommandTer():
    query = input('Please tell me, how can i help you sir? \n')  
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
    
def screenSort():
    img_name = tt.time()
    img_name = f'C:\\Users\\GAURAV\\Desktop\\python_projects\\screenshort\\{img_name}.png'
    speak('sceenshort taken')
    img = pyautogui.screenshot(img_name)
    img.show()

def cpu():
    usage = str(psutil.cpu_percent()) 
    print('Well, Cpu utilization is at ' + usage)
    speak('Well, thecpu utilization is at')
    speak('{}%'.format(usage) )
    battery = psutil.sensors_battery()
    print('battery is at' )  
    print(battery.percent)
    print(battery)

    speak('battery is at')
    speak('{}%'.format(battery.percent) )
    batteryInfo = str(battery.power_plugged)
    print(batteryInfo)
    
    if battery.percent < 25 and batteryInfo == 'False':
        speak(' Since, Battery is  {} percent, I suggest you to charge system sir!'.format(battery.percent))
    if battery.percent < 15 and battery.power_plugged == False :
        speak('battery is at critical level(<15%), whould you like to exit program!')    
        info = takeCommandMic().lower()
        if 's' in info:
            speak('closing the application')
            quit()
        else:
            speak('i strogly recommend you to charge the system sir!')  
    if battery.power_plugged == True: 
        speak(' and the system is charging')
    else:
        speak(' and the system is running on battery')
    
   

if __name__ == "__main__" :
    #wishMe()
   
    greeting()
    #speak('would you like to know about my status')
    tak = takeCommandMic().lower()
    if 's' in tak:
        cpu()
    
    
    while True: 
         
        shutdown = 'offline'
       
        
        query = takeCommandMic().lower()
        if 'time' in  query:
            time()
        elif 'today' in query:
            getDate()
        elif 'date' in query:
            date()    
           

        elif 'shutdown' in query:
            speak('closing the program')
            exit() 

        elif 'who are you'  in query:
            speak('i am junior, a voice assistant, created by gaurav! using python programming language')    
        elif 'how are you' in query:
            speak('i am fine and hope you are also doing well sir!!')
        elif 'hello' in query:
            speak('ohh hello sir, please tell me how can i help you?')    
        elif 'junior' in query:
            speak('yes sir, how can i help you?')
        elif 'what can you do for me' in query:
            speak('there is so much thing that i can do, but in short')
            speak('I can open different files/applications, search on google, play youtube video, send mail, search and read things from wikipedia, can take screenshorts and can open most of websites( like facebook, messenger, github, instragram, reddit,etc).')    
            speak('what you want me to do sir?')
        elif 'open' in query:
            quer = query.replace('open',"")
            print('Opening'+quer)
            speak('opening '+quer) 
            link = 'https://www.' + quer + ' .com/'
            link = link.replace(" ", "")
            print(link)
            web.open(link, new=0, autoraise=True)
            tt.sleep(4)
            try:
                
                if 'google' in quer:
                    speak('what would you like to search on google sir?')
                    getinfoo = takeCommandMic().lower()
                    pyautogui.write(getinfoo)
                    pyautogui.press('enter') 

                else :
                    print('search completed sir!')
                    speak('search completed sir!')

            except Exception as e:
                print(e)   
         
          
        elif 'status' in query:
            cpu()
    
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

        elif 'play your favourite song' in query:
            web.open('https://www.youtube.com/')

            speak('playing  Luis Fonsi - Despacito') 
            pywhatkit.playonyt('despacito')   

        elif 'stop' in query:
            pyautogui.press('space')   
            speak('video paused')
            
        elif 'play the video' in query:
            pyautogui.press('space')   
            speak('video playing start')

        elif 'skip' in query:
            speak('skiping 5second sir!')
            pyautogui.press('right')     

        elif 'new tab' in query:
            speak('opening new tab sir!')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('t')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('t')
            pyautogui.press('enter')
            speak('what would you like to search on new tab sir?')
            getinfo = takeCommandMic().lower()
            pyautogui.write(getinfo)
            pyautogui.press('enter') 

        elif 'switch tabs' in query:
            speak('swithing between tabs sir!')  
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('tab')
            pyautogui.press('enter') 

        
        elif 'exit tab' in query:
            speak('closing tab sir!')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('w')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('w')
            pyautogui.press('enter')
        
        elif 'close chrome' in query:
            speak('Closing chrome')
            pyautogui.keyDown('alt')
            pyautogui.keyDown('f4')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('f4')
            pyautogui.press('enter')

        elif 'exit app' in query:
            speak('Closing chrome')
            pyautogui.keyDown('alt')
            pyautogui.keyDown('f4')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('f4')
            pyautogui.press('enter')
        
            

        elif 'youtube' in query:
            web.open('https://www.youtube.com/') 
            speak('opening youtube')

        elif 'gmail' in query: 
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

        elif 'premier pro' in query:
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

        elif 'local d' in query:
            codepath5 = 'D:\\'
            speak('opening local disk d')
            os.startfile(codepath5)  

        elif 'desktop' in query:
            codepath6 = 'C:\\Users\\GAURAV\\Desktop\\'
            speak('opening desktop')
            os.startfile(codepath6)

        elif 'keyboard' in query:
            speak('opening keyboard')
            codepath7 = 'C:\\WINDOWS\\system32\\osk.exe'
            os.startfile(codepath7)  
            sleep(4)
            speak('waiting for your response sir')


        elif 'joke' in query:
            jokesss = pyjokes.get_joke()
            print(jokesss)
            speak(jokesss)

        elif 'screenshot' in query:
            screenSort()   

        elif 'play music' in query:
            speak('playing music sir!')
            playsound('C:\\Users\\GAURAV\\Music\\songs\\romanticsong.mp3') 

        elif 'play some romantic music' in query:
            speak('playing romantic music sir!')
            playsound('C:\\Users\\GAURAV\\Music\\songs\\bu.mp3')  

        elif 'play my favourite song' in query:
            speak('Playing Tujhe Kitna Chahne Lage song on youtube!')
            print('listening...')
            web.open('https://www.youtube.com/watch?v=h7gyJRWrjbg') 


            
        elif 'shutdown' in query:
            speak('Shutting down computer may close all your unfinished work. say ok to shutdown computer')
            lis = takeCommandMic().lower()
            if 'ok' in lis:
                speak('shutting down in 10 second')
                speak('say stop or exit to stop the shutdown!')
                
                sound = takeCommandMic().lower()
                if 'stop' in sound:
                    print('stoped')
                    speak('stoped')
                elif 'exit' in sound:
                    exit()
                    speak('closing the program')
                    
                else:
                    os.system("shutdown /s /t 10")    
            else :
                print('shutdown process stoped sir!')
                speak('shutdown process stoped sir!')
                
        elif 'restart' in query:
            speak('Do you really want to restart your computer. say ok to restart your program')
            liss = takeCommandMic().lower()
            if 'ok' in liss:
                speak('Restarting in 10 second')
                speak('say stop or exit to stop the restart!')
                
                soundd = takeCommandMic().lower()
                if 'stop' in soundd:
                    print('stoped')
                    speak('stoped')
                elif 'exit' in soundd:
                    exit()
                    speak('closing the program')
                    
                else:
                    os.system("shutdown /r /t 10")    
            else :
                print('restart process stoped sir!')
                speak('restart process stoped sir!')

        elif 'facebook' in query:
            username = {
                
                'unnat' : 'https://www.facebook.com/messages/t/100003722177427',
                'rupesh' : 'https://www.facebook.com/messages/t/100008186652735',
                'ayush' : 'https://www.facebook.com/messages/t/100015820215428',
                'gaurav':  'https://www.messenger.com/t/100009440677937',
                'sanjay': 'https://www.facebook.com/messages/t/100004372715683',
                'vishal': 'https://www.facebook.com/messages/t/100010536152143',
                'ishwor': 'https://www.facebook.com/messages/t/100012682471101',
                'subash': 'https://www.facebook.com/messages/t/100007389842562',
                'pastha': 'https://www.facebook.com/messages/t/100021935493384'

            }
            speak('opening facebook')
            web.open('https://www.facebook.com/')
            tt.sleep(4)
            speak('To whom you want to send message')
            namee = takeCommandMic().lower()
            print(username)
            try:
                
                receiver = username[namee]
                web.open(receiver)

                speak('what should be the message sir')
                message = takeCommandMic()
                print(message)
                pyautogui.typewrite(message)
                pyautogui.press('enter')
                speak('message sent successfully')

            except Exception as e:
                print(e)
                inf = 'username not found'
                speak(inf)
                speak('Say it again please')

        elif 'send email' in query:
            speak('would you send mail through terminal or voice command')
            info = takeCommandMic().lower()
            email_list = {
                
                'vishal' : 'bishalkhatri675@gmail.com',
                'bhupesh' : 'bhupeshjoshi293@gmail.com',
                'ayush' : 'joshiayush20582059@gmail.com',
                'gaurav':  'developer.gaurav77@gmail.com'

            }

            if 'terminal' in info:
                    print('To whom you want to send the mail\n')
                    name = takeCommandTer().lower()
                    print(name)
                    receiver = email_list[name]
                    print('what should be the subject of mail sir?')
                    subject = takeCommandTer()
                    print('what should you write in mail sir?')
                    content = takeCommandTer()
                    sendEmail(receiver,subject,content)
                    speak('email sent successfully')
                    print('email sent successfully')
               
            
            else:
                try:
                    speak('To whom you want to send the mail\n')
                    nam = takeCommandMic().lower()
                    print(nam)
                    receiver = email_list[nam]
                    speak('what should be the subject of mail sir?')
                    subjec = takeCommandMic()
                    speak('what should i write in mail sir?')
                    conten = takeCommandMic()
                    sendEmail(receiver,subjec,conten)
                    speak('email sent successfully')
                    print('email sent successfully')
                except Exception as e:
                    print(e)    
                    speak('unable to send email')
            
              
            
                