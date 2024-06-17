import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from SpeakTakeCommand import speak, takeCommand


# Define application paths or commands
dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "vs code": "code",
    "powerpoint": "powerpnt",
}


def openAppWeb(query):
    speak("Opening, sir")
    query = query.lower()
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "").replace("jarvis", "").replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                try:
                    os.system(f"start {dictapp[app]}")
                except Exception as e:
                    speak(f"Sorry, I couldn't open {app}. Error: {str(e)}")


def closeappWeb(query):
    speak("Closing, sir")
    query = query.lower()
    tabs_to_close = 0
    if "one tab" in query or "1 tab" in query:
        tabs_to_close = 1
    elif "2 tabs" in query or "two tabs" in query:
        tabs_to_close = 2
    elif "3 tabs" in query or "three tabs" in query:
        tabs_to_close = 3
    elif "4 tabs" in query or "four tabs" in query:
        tabs_to_close = 4
    elif "5 tabs" in query or "five tabs" in query:
        tabs_to_close = 5

    for _ in range(tabs_to_close):
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)

    if tabs_to_close > 0:
        speak(f"{tabs_to_close} tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                try:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")
                except Exception as e:
                    speak(f"Sorry, I couldn't close {app}. Error: {str(e)}")


# Example usage:
# openAppWeb("open vscode")
# closeappWeb("close 2 tabs")
