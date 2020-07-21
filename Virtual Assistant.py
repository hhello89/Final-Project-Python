import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime 
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print ("Initializing Ghost")

HALO = "sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronouce the string which is passed to it
def speak(text):
    engine.say(text)    
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + HALO)

    elif hour>=12 and hour <18:
        speak("Good Afternoon" + HALO)

    else:   
        speak("Good Evening" + HALO)

        speak("I am Ghost, Anything I can help you")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        print("Say that again please...")  
        return "None"

    return query


# Main Program starts here.. 
speak("Initializing Ghost")
wishMe()
query = takeCommand() 

# Logic for executing task as per the query 
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    print(results)
    speak(results)

elif "open youtube" in query.lower():
    webbrowser.open("youtube.com")  