import pyttsx3  #importing this module to convert text to speech

engine = pyttsx3.init() # object creation

""" RATE"""
engine.getProperty('rate')   # getting details of current speaking rate
voiceRate = 170
engine.setProperty('rate', voiceRate)     # setting up new voice rate

engine.say("I will speak this text")
engine.runAndWait()