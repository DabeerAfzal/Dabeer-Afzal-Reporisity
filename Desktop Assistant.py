import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import random
import requests
import subprocess as sp
import pyautogui
from bs4 import BeautifulSoup

# Assistant's Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak(f"Good Evening Sir!")

    strTime = datetime.datetime.now().strftime("%I:%M %p")

    search = "temperature in lahore"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    
    speak(f"The Time Is {strTime} And The Temperature  Outside is {temp} Please Tell Me How Can I Help You Today!")


def takeCommand():
   #This Function Uses Our Microphone To Take Commands

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak and print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

# Sends Email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email Address', 'Your Password')
    server.sendmail('Your Email Address Again', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# Functions Of The Assistant
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")

        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open_new("stackoverflow.com")

        elif 'how are you' in query:
            speak("I Am fine Sir is there Anything  I can Help you with today?")

        elif "I am bored" in query:
            speak("Sir Should I Play Some Music For You Or Launch Minecraft?")

        elif "launch" in query:
            speak("Tell Me The Name of The Website Sir!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir! Enjoy")

        elif 'minecraft' in query:
            sp.Popen("C:\\Users\\DELL\\Downloads\\SKlauncher 3-beta.20.exe")
            speak("Opening Minecraft Sir I Wish You Have a Good Time Playing!")
            
        elif "music" in query:
            n = random.randint(0,4)
            print(n)
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'email' in query:
            try:
                speak("What Should I Say Sir?")
                content = takeCommand()
                to = "email of person which you're sending the email"
                sendEmail(to, content)
                speak("Email Has Been Sent Sir!")
            except Exception as e:
                print(e)
                speak("Sorry Sir I Was Not Able to Send the Email!")

        elif "temperature" in query:
            search = "temperature in lahore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")

        elif "thanks" in query:
            speak("No Problem Sir Im Happy To Help!")

        elif "thank you" in query:
            speak("Im Happy To Help!")

        elif "go to sleep" in query:
            speak("Ok Sir You Can Call Me Anytime!")
            break

        elif "you need a break" in query:
            speak("Alright sir Just remember You can call me anytime you want Have a good day!")
            break
        
        elif "screenshot" in query:
            speak("Ok Sir What Should i Name that File?")
            path = takeCommand()
            path1name = path + ".png"
            path1 = "F:\Screenshat"+ path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("F:\\Screenshat")
            speak("Here is your Screenshot Sir!")

        elif 'search google' in query:
            text = query.replace("search google for", "")
            webbrowser.open("https://www.google.com/search?q=" + text)

        elif 'search youtube' in query:
            text = query.replace("search youtube for", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + text)

        elif 'open chrome' in query:
            codePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
            speak("Launching Google Chrome Sir!")

        elif 'spotify' in query:
            sp.Popen("C:\\Users\\DELL\\AppData\\Roaming\\Spotify/spotify.exe")
            speak("Done Sir!")

        elif 'code' in query:
            sp.Popen("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe")
            speak("Opening Code Sir I Wish You All The Best On Your Python Project!")
        
        else:
            speak("Sorry, I Didn't Understand Sir! Please Try Again")
            print("Sorry, I Didn't Understand Sir! Please Try Again")

        #Adding More Features Daily!

