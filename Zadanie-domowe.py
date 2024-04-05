# Zadanie domowe : napisz program który będzie pytał nas o aktualny rok następnie pytał nas o ilość lat które chcemy do tego roku dodać i na koniec wyświetli nam informacje że obecnie mamy rok a za pięć lat ten rok będzie: Przykł;ad print(f" Mamy teraz rok{rok} a za {lata} będziemy mieć {rok+lata)


import time  # Dodaję/importuję bibliotekę aby program czekał określoną liczbę sekund

print("Oto program do dodawania kolejnych lat w obecnym roku.") #Wyświetlam informację dla użytkownika o programie za pomocą funkcji print

rok = int(input("Podaj bieżący rok: ")) #Deklaruję zmienne z typem int aby odwołać się do liczb całkowitych dowolnej wartośći. Następnie oczekuję od użytkownika aby wpisał wartość liczbową
time.sleep(2) #Program czeka 2 sekundy
lata = int(input("Podaj ilość lat które chcesz dodać do bieżącego roku: "))

time.sleep(3) #Program czeka 3 sekundy


print(f" Mamy teraz rok {rok} a za {lata} lata będziemy mieć {rok+lata} rok.") #Wyświetlam użytkownikowi aplikacji wynik końcowy za pomocą funkcji print. Print odwołuję się do zmiennych za pomocą f oraz liczb w pamięci komputera ltóre są zachowane w nazwach zmiennych w nawiasach {}. Oraz dodaję zmienną do zmiennej