#lecture 10-7-23
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id) # To check voices available on computer.
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''This function will give audio as an output.'''

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This function will greet end user and introduce itself when called.'''

    hour = int(datetime.datetime.now().hour) # Will fetch time from datetime module.

    if hour>= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Steve Sir. Please tell me how may I help you.") # AI intro.
