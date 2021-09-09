import os
import Image
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from PIL import _imaging
from playsound2 import playsound
from cv2 import cv2
import smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good morning sir")
    elif hour>12 and hour<16:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("Hey I am Jarvis, how can i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold =1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #speak("say that again please.....")
        print("say that again please.....\n")
        return "None"
    return query


if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()

        if 'hey' in query:
            speak('hello sir, how can i help you?')

        elif 'name' in query:
            speak('my name is indigo')

        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=4)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/')

        elif "open google" in query:
            speak("opening google")
            webbrowser.open('https://www.google.com/')

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'the time' in query:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            print(t)
            speak(f"sir, the time is {t}")

        elif 'open pycharm' in query:
            speak("opening pycharm")
            path="F:\\Python\\pycharm\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'send email' in query:
            sender = "shashankk279@gmail.com"
            reciever = "getinkart14@gmail.com"
            password = input(str("please enter yoaur password: "))
            message = "Hey! how are you?"

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            print("Login sucess")
            server.sendmail(sender, reciever, message)
            print("Emain has been sent to", reciever)

        elif 'what are you doing' in query:
            speak("I am sorry sir, i do some mistake")

        elif 'open my image' in query:
            speak("opening your image")
            im=Image.open(r"E:\\Starking\\IMG-20210305-WA0002.jpg")
            im.show()

        elif 'how are you' in query:
            speak("i am good sir, how  are you?")

        elif 'song for me' in query:
            playsound("C:\\Users\\Win-10\\Downloads\\beggin_you.mp3")

        elif 'audio' in query:
            playsound("C:\\Users\\Win-10\\Downloads\\skechers.mp3")

        elif 'linkedin' in query:
            speak("opening linkedin")
            webbrowser.open("https://www.linkedin.com/feed/")

        elif 'phone camera' in query:
            speak("connecting phone's camera")
            url = 'http://192.168.1.33:8080/video'
            cap = cv2.VideoCapture(url)
            while (True):
                ret, frame = cap.read()
                if frame is not None:
                    cv2.imshow('frame', frame)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break
            cv2.destroyAllWindows()

        elif 'exit' in query:
            speak('ok sir, as your wish')
            exit()

        else:
            speak("i can't recognize, say that again please!")
