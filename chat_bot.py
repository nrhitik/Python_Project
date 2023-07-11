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

def takeCommand():
    '''It takes microphone input from the user and returns string output.'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recogninzing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) # Will print exception/error.
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while 1:
        # Logic for executing tesks based on query.
        query = takeCommand().lower()
        if 'open spotify' in query:
            codepath = "" #target of spotify
            os.startfile(codepath)
