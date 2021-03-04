import pyttsx3  #importing this module to convert text to speech
import datetime #importing this module to use date and time

engine = pyttsx3.init() # object creation

""" RATE"""
engine.getProperty('rate')   # getting details of current speaking rate
voiceRate = 170
engine.setProperty('rate', voiceRate)     # setting up new voice rate



def speak(audio): #this function to used to speak
    engine.say(audio)
    engine.runAndWait()
    
def time():  #this function is used to calculate current time
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    

speak('i m good')
time()