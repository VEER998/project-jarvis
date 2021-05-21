
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour <0 and hour >12:
        speak("good morning sir")
    elif hour >=12 and hour <=17:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        audio = r.listen(source)
    try:
        Text = r.recognize_google(audio, language= 'eng-in')
        print("recognizing......")
        print(Text)
    except Exception:
        s = "sorry didn't understood"
        speak(s)
        print(s)
        return "none"
    return Text

if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching results please wait....")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)
        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.in")
        
        elif "who are you" in query:
            speak("hello my name is jarvis. i am a ai personal assiatnt")
        elif "hello" in query or "hi" in query:
            speak("hello i am jarvis")
        
        elif "what can you do" in query:
            ans = "i can do simple things like opening apps processing commands and many more"
            speak(ans)
        elif "good bye" in query:
            speak("okay, good bye, nice to meet with you!!")
            exit()
        elif "close program" in query:
            speak("okay, closing program goodbye!")

        else:
            print('sorry')

        
