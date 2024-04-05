#Moje zadanie dodatkowe z poprzedniej lekcji
#Dołączam bibliotekę time aby program czekał określoną liczbę sekund
import time

#Początek programu-wyświetlam informacje dla użytkownika przy pomocy print
print("Mój ulubiony film. Proszę podać swój ulubiony film: ")

print("---------------------------")

#Dekraluję zmienne oraz tworzę dodatkowe pole do integracji z użytkownikiem
Terminator = input("Jaki jest twój ulubiony film?: ")
time.sleep(1)
Rok_wydania = input("W którym roku powstał ten film?: ")
time.sleep(2)
Ilu_bylo_widzow = input("Ilu było widzów na tym filmie?: ")
time.sleep(2)
O_czym_jest_ten_film = input("O czym jest ten film?: ")
time.sleep(3)

#Raport z odpowiedziami użytkownika
print(f"Twój ulubiony film to {Terminator}, flim został wydany w roku {Rok_wydania}. Na twojim ulubionym filmie było {Ilu_bylo_widzow} widzów, film jest o {O_czym_jest_ten_film}.   ")

#Print warunkowy/bool
Informacja_dodatkowa = input("Czy chcesz mi podać dodadkowe informacje? {Tak, Nie, Nie_wiem}: ")

#Dekraluję instrukcję warunkową if
if Informacja_dodatkowa == "Tak":
    print("Super że rozmowa ze mną ci się podoba:)")
elif Informacja_dodatkowa =="Nie":
    print("Szkoda że nie chcesz podać mi więcej informacji :(")
elif Informacja_dodatkowa == "Nie wiem":
    print("Hmm....:/ A może podasz mi dalsze informacje:)")
else:
    print("Oto kolejny zestaw pytań:")