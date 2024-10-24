import speech_recognition as sr
import pyttsx3
import os
import datetime
from googletrans import Translator
import math

# Inicjalizacja rozpoznawania mowy, syntezatora mowy i tłumacza
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Funkcja do mówienia przez asystenta
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Funkcja do rozpoznawania mowy użytkownika
def listen():
    with sr.Microphone() as source:
        print("Słucham...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            query = recognizer.recognize_google(audio, language="pl-PL")
            print(f"Ty: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "Nie zrozumiałem. Spróbuj ponownie."
        except sr.RequestError:
            return "Nie mogę połączyć się z serwisem rozpoznawania mowy."

# Funkcja do tłumaczenia tekstu
def translate_text(text, dest_lang='en'):
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

# Funkcja do odczytywania aktualnej daty i godziny
def tell_time():
    now = datetime.datetime.now()
    return f"Aktualna data i godzina to {now.strftime('%Y-%m-%d %H:%M:%S')}."

# Funkcja do wykonywania prostych obliczeń matematycznych
def calculate(expression):
    try:
        result = eval(expression)
        return f"Wynik to {result}."
    except Exception as e:
        return "Nie mogłem wykonać obliczeń."

# Funkcja do otwierania aplikacji
def open_application(command):
    if "przeglądarka" in command:
        os.system("start chrome")
        return "Otwieram przeglądarkę internetową."
    
    elif "notatnik" in command:
        os.system("start notepad")
        return "Otwieram notatnik."

    else:
        return "Nie wiem, jak uruchomić tę aplikację."

# Funkcja do rozmowy na różne tematy
def conversation_on_topic(command):
    if "python" in command:
        return ("Python to język programowania wysokiego poziomu, "
                "Python został wynaleziony pod koniec lat 80. XX wieku [ 41 ] przez Guido van Rossuma"
                "który jest popularny dzięki swojej prostocie i wszechstronności. "
                "Można go używać w wielu dziedzinach, takich jak web development, "
                "analiza danych, uczenie maszynowe czy automatyzacja. Python jest językiem Back-End.")
    
    elif "terminator" in command or "opowiedz mi o T-800" in command:
        return ("Seria 800 Terminator zawiera procesor sieci neuronowej CPU , czyli „komputer uczący się”, umieszczony w endoskullu i chroniony przez bezwładnościowe amortyzatory wstrząsów. CPU, opracowany przez Cyberdyne Systems, jest jednym z najpotężniejszych mikroprocesorów, jakie kiedykolwiek zbudowano."
                "Seria 800 jest również wyposażona w wokale, które umożliwiają jej odtworzenie dowolnego wzorca ludzkiej mowy, którego odpowiedni okaz usłyszała. Robi to poprzez nagrywanie i przechowywanie sylab głosów badanych, które następnie odtwarza i wykorzystuje do cyfrowej syntezy wzorców ich mowy. Czujniki słuchowe T-800 znajdują się po obu stronach głowy, gdzie znajdowałyby się ludzkie uszy. Jeden czujnik rejestruje pełen zakres dźwięków zewnętrznych, podczas gdy drugi może automatycznie filtrować sygnały do ​​wąskiego zakresu dla określonego sygnału słuchowego."
                "Czujniki optyczne T-800 mogą pobierać próbki z rozszerzonego zakresu widzialnych częstotliwości, w tym podczerwieni (co pozwala mu widzieć rozgrzane ciała w całkowitej ciemności)."
                "T-800 jest zdolny do śledzenia ruchu, trybów wyszukiwania, identyfikacji i rozpoznawania twarzy oraz ma rozbudowane możliwości poprawy widzenia, w tym „zoom” dalekiego zasięgu (T-800 może powiększyć obraz o około x15).")
        
    elif "Czym jesteś" in command or "wersja" in command:
        return ("Jestem Asystentem głosowym typu ChatGPT-x, można mnie nazwać ChatGPT-x"
                "Mogę otworzyć aplikację, Sprawdzić pogodę i opowiedzieć tobie ciekawe rzeczy"
                "Jestem projektem Open-Source co oznacza że każdy programista może mnie rozwijać i dodawać nowe funkcję"
                "Moim celem jest również pomaganie osobom słabo widzącym w korzystaniu z komputera, poprzez komunikaty głosowe")
    
    elif "data" in command:
        time_info = tell_time()
        return time_info

    else:
        return "Nie jestem pewien, jak odpowiedzieć na to pytanie. Możesz zapytać o Pythona lub film Terminator."

# Główna funkcja asystenta
def assistant():
    speak("Witaj! Jestem twoim asystentem głosowym. Jak mogę ci pomóc?")
    print("Komendy: tłumacz, aplikacja, oblicz, rozmowa, czas, koniec")

    while True:
        command = listen()

        if "tłumacz" in command:
            speak("Powiedz, co mam przetłumaczyć.")
            text_to_translate = listen()
            speak("Na jaki język chcesz przetłumaczyć?")
            lang = listen()  # Np. "angielski", "niemiecki"
            
            language_map = {
                "angielski": "en",
                "niemiecki": "de",
                "francuski": "fr",
                "hiszpański": "es",
                "włoski": "it"
            }
            
            dest_lang = language_map.get(lang, "en")  # Domyślnie angielski, jeśli nie rozpozna
            translation = translate_text(text_to_translate, dest_lang)
            
            print(f"Tłumaczenie: {translation}")
            speak(f"Tłumaczenie: {translation}")
        
        elif "aplikacja" in command:
            speak("Jaką aplikację mam otworzyć?")
            response = open_application(listen())
            print(response)
            speak(response)
        
        elif "czas" in command:
            time_info = tell_time()
            print(time_info)
            speak(time_info)
        
        elif "oblicz" in command:
            speak("Podaj wyrażenie do obliczenia.")
            expression = listen()
            result = calculate(expression)
            print(result)
            speak(result)
        
        elif "rozmowa" in command or "rozmawiaj" in command:
            speak("O czym chcesz porozmawiać?")
            topic_response = conversation_on_topic(listen())
            print(topic_response)
            speak(topic_response)

        elif "koniec" in command or "zakończ" in command:
            speak("Do widzenia!")
            break
        
        else:
            speak("Nie rozumiem tej komendy.")

# Uruchomienie asystenta
if __name__ == "__main__":
    assistant()