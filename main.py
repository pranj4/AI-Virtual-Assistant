import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}")
        return query.lower()  # Return the recognized command
    except Exception as e:
        print("Please repeat")
        return None

def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")  # Example: "10:30 AM"
    speak(f"The time is {time_str}")
    print(f"The time is {time_str}")

def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any results.")

def open_website(command):
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    else:
        speak("Sorry, I can't open that website.")

def tell_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")  # Example: "Friday, March 15, 2025"
    speak(f"Today's date is {date_str}")
    print(f"Today's date is {date_str}")


# Speak a greeting
speak("Hello, I am your virtual assistant called Hisenberg , How may I assist you today.")

# Listen for a command
command = takecommand()

# Process the command
while True:
    command = takecommand()

    if command:
        #if "assistant" in command:
            #command = command.replace("assistant", "").strip()

            if "time" in command:
                tell_time()

            elif "date" in command:
                tell_date()

            elif "wikipedia" in command:
                query = command.replace("wikipedia", "").strip()
                search_wikipedia(query)

            elif "open" in command:
                open_website(command)

            elif "stop" in command or "exit" in command:
                speak("Goodbye!")
                break  # Exit the loop

            else:
                speak("Sorry, I didn't understand.")


