import speech_recognition as sr
import pyttsx3
import os
import datetime
from googletrans import Translator
import math

# Initialization of speech recognition, speech synthesizer, and translator
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Function for assistant to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for recognizing user speech
def listen():
    with sr.Microphone() as source:
        print("I'm listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            query = recognizer.recognize_google(audio, language="pl-PL")
            print(f"You: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "I didn't understand. Please try again."
        except sr.RequestError:
            return "I can't connect to the speech recognition service."

# Function to translate text (to English)
def translate_text(text, dest_lang='en'):
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

# Function to read the current date and time
def tell_time():
    now = datetime.datetime.now()
    return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}."

# Function to perform simple mathematical calculations
def calculate(expression):
    try:
        result = eval(expression)
        return f"The result is {result}."
    except Exception as e:
        return "I couldn't perform the calculation."

# Function to open applications
def open_application(command):
    if "browser" in command:
        os.system("start chrome")
        return "Opening the web browser."
    
    elif "notepad" in command:
        os.system("start notepad")
        return "Opening notepad."

    else:
        return "I don't know how to open that application."

# Function for conversation on different topics
def conversation_on_topic(command):
    if "python" in command:
        return ("Python is a high-level programming language, "
                "Python was invented in the late 1980s by Guido van Rossum, "
                "and it is popular for its simplicity and versatility. "
                "It can be used in many fields such as web development, "
                "data analysis, machine learning, or automation. Python is a back-end language.")
    
    elif "terminator" in command or "tell me about the T-800" in command:
        return ("The T-800 series features a neural network CPU, a 'learning computer', housed in the endoskull and protected by inertial shock dampers. "
                "The CPU, developed by Cyberdyne Systems, is one of the most powerful microprocessors ever built. "
                "The T-800 series is also equipped with vocal capabilities, allowing it to replicate any human speech pattern it has heard. "
                "It does this by recording and storing the syllables of the voices it has heard, which are then synthesized to reproduce speech patterns. "
                "The T-800's auditory sensors are located on both sides of the head, where human ears would be. "
                "One sensor captures the full range of external sounds, while the other can filter sounds for specific auditory signals. "
                "The T-800's optical sensors can sample an extended range of visible frequencies, including infrared, allowing it to see heated bodies in complete darkness."
                "The T-800 is capable of tracking movement, search modes, face recognition, and has extensive vision enhancement capabilities, including long-range zoom (up to about 15x).")
        
    elif "What are you" in command or "version" in command:
        return ("I am a voice assistant called ChatGPT-x. "
                "I can open applications, check the weather, and tell you interesting facts. "
                "I am an open-source project, which means any developer can expand my functionality. "
                "My goal is also to help visually impaired people use the computer through voice commands.")
    
    elif "date" in command:
        time_info = tell_time()
        return time_info

    else:
        return "I'm not sure how to respond to that. You can ask about Python or the movie Terminator."

# Main assistant function
def assistant():
    speak("Hello! I am your voice assistant. How can I help you?")
    print("Commands: translate, application, calculate, conversation, time, exit")

    while True:
        command = listen()

        if "translate" in command:
            speak("Tell me what to translate.")
            text_to_translate = listen()
            speak("Which language do you want to translate from?")
            lang = listen()  # For example: "Polish", "German"
            
            language_map = {
                "polish": "pl",
                "german": "de",
                "french": "fr",
                "spanish": "es",
                "italian": "it"
            }
            
            source_lang = language_map.get(lang, "pl")  # Default to Polish if not recognized
            translation = translate_text(text_to_translate, 'en')  # Always translate to English
            
            print(f"Translation: {translation}")
            speak(f"Translation: {translation}")
        
        elif "application" in command:
            speak("Which application should I open?")
            response = open_application(listen())
            print(response)
            speak(response)
        
        elif "time" in command:
            time_info = tell_time()
            print(time_info)
            speak(time_info)
        
        elif "calculate" in command:
            speak("Please provide an expression to calculate.")
            expression = listen()
            result = calculate(expression)
            print(result)
            speak(result)
        
        elif "conversation" in command or "talk" in command:
            speak("What would you like to talk about?")
            topic_response = conversation_on_topic(listen())
            print(topic_response)
            speak(topic_response)

        elif "exit" in command or "end" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I don't understand that command.")

# Run the assistant
if __name__ == "__main__":
    assistant()
