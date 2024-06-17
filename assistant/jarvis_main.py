import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
from SpeakTakeCommand import speak, takeCommand


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if "wake up" in query:
            from GreetMe import greetMe

            greetMe()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, How can I help you?")
                elif ("fine") in query or ("good") in query:
                    speak("that's great, sir")
                elif ("how are you") in query:
                    speak("Perfect, sir. What about you?")
                elif ("thank you") in query:
                    speak("you are welcome, sir")
                elif ("who are you") in query:
                    speak("I am your Jarvis, your personal assistant")

                elif "open" in query:
                    from Dictapp import openAppWeb

                    openAppWeb(query)
                elif "close" in query:
                    from Dictapp import closeappWeb

                    closeappWeb(query)
                elif "google" in query:
                    from SearchNow import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube

                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in kamra"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text

                    print(f"The temperature in kamra is {temp}")
                    speak(f"The temperature in kamra is {temp}")

                elif "weather" in query:
                    search = "temperature in kamra"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text

                    print(f"The temperature in kamra is {temp}")
                    speak(f"The temperature in kamra is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video resumed")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Video unmuted")

                elif "volume up" in query or "increase volume" in query:
                    from Keyboard import volumeUp

                    speak("Turning volume up, sir")
                    volumeUp()

                elif "volume down" in query or "decrease volume" in query:
                    from Keyboard import volumeDown

                    speak("Turning volume down, sir")
                    volumeDown()

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "news" in query:
                    from NewsRead import latestNews

                    latestNews()
                elif (
                    "remember that" in query
                    or "remember this" in query
                    or "what do you remember" in query
                    or "remeber history" in query
                ):
                    from Remember import remember

                    remember(query)
                elif "shutdown" in query:
                    speak("Ok sir, shutting down")
                    exit()
