import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


query = takeCommand().lower()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap

        query = query.replace("Jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        query = query.replace("search", "")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            print(result)
            speak(result)

        except Exception as e:
            speak("No speakable output found on google")


def searchYoutube(query):
    if "youtube" in query:
        speak("This is what i found from your search")
        query = query.replace("youtube", "")
        query = query.replace("jarvis", "")
        query = query.replace("search", "")
        query = query.replace("youtube search", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done, sir")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searchning from Wikipedia")
        query = query.replace("wikipedia", "")
        query = query.replace("jarvis", "")
        query = query.replace("search", "")
        query = query.replace("wikipedia search", "")
        result = wikipedia.summary(query, 2)
        speak("according to Wikipedia.")
        print(result)
        speak(result)
