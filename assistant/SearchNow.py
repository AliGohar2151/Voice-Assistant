import speech_recognition as sr
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


def takeCommand(prompt=""):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        speak("Sorry, my speech service is down.")
        return "None"
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query.lower()


def clean_query(query, unwanted_phrases):
    for phrase in unwanted_phrases:
        query = query.replace(phrase, "")
    return query.strip()


def searchGoogle(query):
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
    query = clean_query(query, unwanted_phrases)

    if query:
        speak("This is what I found on Google")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)
        except Exception as e:
            print(e)
            speak("No speakable output found on Google")
    else:
        speak("Please provide a valid search query.")


def searchYoutube(query):
    unwanted_phrases = [
        "jarvis",
        "hey jarvis",
        "hey",
        "youtube search",
        "youtube",
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
        "play",
        "watch",
        "in",
        "on",
        "from",
    ]
    query = clean_query(query, unwanted_phrases)

    if query:
        speak("This is what I found from your search")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("Would you like me to play the video?")
        while True:
            command = takeCommand()
            if "yes" in command or "ok" in command:
                pywhatkit.playonyt(query)
                break
            elif "no" in command:
                speak("Okay, not playing the video.")
                return
            else:
                speak("Please say yes or no.")
    else:
        speak("Please provide a valid search query.")


def searchWikipedia(query):
    unwanted_phrases = [
        "jarvis",
        "hey jarvis",
        "hey",
        "wikipedia search",
        "wikipedia",
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
    query = clean_query(query, unwanted_phrases)

    if query:
        speak("Searching from Wikipedia")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia.")
            print(result)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e)
            speak("There are multiple results. Please be more specific.")
        except Exception as e:
            print(e)
            speak("Sorry, I could not find anything on Wikipedia.")
    else:
        speak("Please provide a valid search query.")
