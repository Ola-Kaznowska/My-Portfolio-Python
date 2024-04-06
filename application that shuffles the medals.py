# Napisz program używając biblioteki random który będzie losował z dostępnej tablicy lub słownika trzy posiłki które danego dnia można sobie przygotoeać. Program na początku prosi o imię i wiek po to aby w momencie podsumowania wyświetlić info o posilkach wraz z wiekiem i nazwą użytkownika


import time
import random


print("Witaj w programie losującym ")


def main():
    meals = [
        "sałatka warzywna", 
        "bataty", 
        "sałata",  
        "orzeszki nerkowca",
        "rosół",
        "zupa pomidorowa",
        "kanapka z sałatą",
        "tosty z serem",
        "pieczone żiemniaki",
        "frytki",
        ]
    
   
    name = input("Podaj swoje imię: ")
    time.sleep(2)
    
    age = input("Podaj swój wiek: ")
    
    time.sleep(2)
    
    selected_meals = random.sample(meals, 3)
    
    print("\nDzień dobry,", name, "!")
    print("Dzisiaj masz", age, "lat.")
    print("Oto trzy pomysły na posiłki na dziś:")
    for i, meal in enumerate(selected_meals, start=1):
        print(f"{i}. {meal}")

if __name__ == "__main__":
    main()