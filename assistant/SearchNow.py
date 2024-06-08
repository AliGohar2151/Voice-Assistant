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

        unwanted_phrases = [
            "jarvis",
            "hey jarvis",
            "hey",
            "google search",
            "google",
            "search",
            "please",
            "could you",
            "would you",
            "can you",
            "will you",
            "tell me about",
            "show me",
            "find",
            "look for",
            "what is",
            "who is",
            "for",
            "where is",
        ]

        query = query.lower()
        for phrase in unwanted_phrases:
            query = query.replace(phrase, "")

        query = query.strip()

        if query:
            speak("This is what I found on Google")
            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query, sentences=1)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("No speakable output found on Google")
        else:
            speak("Please provide a valid search query.")


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
