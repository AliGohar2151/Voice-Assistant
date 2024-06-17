import pyttsx3
import datetime
import os

from SpeakTakeCommand import speak, takeCommand

extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)


extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()


def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("alarm.mp3")  # You can choose any music or ringtone
        elif currenttime + "00:00:30" == Alarmtime:
            exit()


ring(time)
