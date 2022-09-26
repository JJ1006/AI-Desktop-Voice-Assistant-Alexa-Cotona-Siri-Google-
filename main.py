import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5') # microsoft speech api
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Opening Youtube...")
            query = query.replace("youtube", "")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak('Opening Google...')
            webbrowser.open("google.com")

        elif 'facebook' in query:
            speak('Opening Facebook...')
            webbrowser.open("facebook.com")

        elif 'instagram' in query:
            speak('Opening Instagram...')
            webbrowser.open("instagram.com")

        elif 'github' in query:
            speak('Opening Github...')
            webbrowser.open("github.com")

        elif 'linkedin' in query:
            speak('Opening Linkedin...')
            webbrowser.open("linkedin.com")

        elif 'music' in query:
            webbrowser.open("music.youtube.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


    # logic for executing tasks based on query