import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    """
    Speaks the given text using the text-to-speech engine.

    Args:
        audio (str): The text to be spoken.
    """
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    """
    Listens for user input and returns it as a lowercase string.

    Returns:
        str: The user input, or "none" if there was an error.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return "none"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "none"


def latestNews():
    """
    Fetches and displays the latest news articles based on user input.
    """
    apidict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=60effb124105464098d23a406203e42a",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=60effb124105464098d23a406203e42a",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=60effb124105464098d23a406203e42a",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=60effb124105464098d23a406203e42a",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=60effb124105464098d23a406203e42a",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=60effb124105464098d23a406203e42a",
    }

    speak(
        "Which type of news do you want? Business, Entertainment, Health, Science, Sports, Technology"
    )
    news_type = takeCommand()
    while news_type == "none":
        news_type = takeCommand()

    url = apidict.get(news_type)
    if not url:
        speak("Sorry, I couldn't find the requested news type.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        news_dict = response.json()
    except requests.exceptions.RequestException as e:
        speak("Sorry, there was an error fetching the news.")
        print(f"Error: {e}")
        return

    speak("Here are the latest news articles")
    news_articles = news_dict.get("articles", [])
    if not news_articles:
        speak("No news articles found.")
        return

    for article in news_articles:
        title = article.get("title", "No title")
        news_url = article.get("url", "No URL")
        speak(title)
        print(title)
        print(f"For more info visit: {news_url}")
        speak("Want to hear more?")

        while True:
            user_input = takeCommand()
            if user_input.lower() == "yes":
                break
            elif user_input.lower() == "no":
                return
            else:
                speak("Please say yes or no.")
