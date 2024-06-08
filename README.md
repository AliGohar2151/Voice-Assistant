# 🤖 Personal Assistant Jarvis

🚧 **Under Development**

A voice-controlled personal assistant that can perform basic tasks like greeting, searching on Google, YouTube, and Wikipedia, checking the temperature, telling the time, and more.

## 🌟 Features

- Voice interaction using `speech_recognition` and `pyttsx3`.
- Web scraping with `requests` and `BeautifulSoup`.
- Alarm setting with custom time input.
- Dynamic responses based on user commands.

## 🛠 Installation

To run this project, you'll need to install the required libraries. You can install them using `pip`:

```bash
pip install pyttsx3 speech_recognition requests beautifulsoup4
```

## 📖 Usage

To start the assistant, run the following command in your terminal:

```bash
python main.py
```
Once running, you can interact with the assistant using voice commands

## 🗣 Commands

- “wake up” - Activates the assistant.
- “go to sleep” - Deactivates the assistant.
- “hello” - The assistant will greet you.
- “how are you” - The assistant will respond with its status.
- “thank you” - The assistant will acknowledge your gratitude.
- “who are you” - The assistant will introduce itself.
- “google [query]” - Searches Google and reads out the first result.
- “youtube [query]” - Searches YouTube and reads out the first result.
- “wikipedia [query]” - Searches Wikipedia and reads out the summary of the first result.
- “temperature” - Tells the current temperature in Kamra.
- “the time” - Tells the current time.
- “open [application]” - Opens the specified application.
- “close [application]” - Closes the specified application.
- “set an alarm” - Sets an alarm for the specified time.
- “shutdown” - Shuts down the assistant.

## 👐 Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.
