import pyttsx3
import speech_recognition
from datetime import datetime
import os
from SpeakTakeCommand import speak, takeCommand


def remember(query):
    if "remember that" in query:
        remember_message = (
            query.replace("remember that", "").replace("jarvis", "").strip()
        )

        if remember_message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp}: {remember_message}\n"

            with open("Remember.txt", "a+") as remember_file:
                remember_file.seek(0)
                existing_messages = remember_file.read()

                if remember_message not in existing_messages:
                    remember_file.write(entry)
                    speak("Got it. I'll remember that " + remember_message)
                else:
                    speak("You already told me to remember that.")
        else:
            speak("You didn't provide anything for me to remember.")

    elif "what do you remember" in query:
        if os.path.exists("Remember.txt"):
            with open("Remember.txt", "r") as remember_file:
                remembered_messages = remember_file.readlines()

            if remembered_messages:
                for message in remembered_messages:
                    print(message.strip())
                speak("You told me to remember the following:")
                for message in remembered_messages:
                    speak(message.strip())
            else:
                speak("I don't have anything to remember.")
