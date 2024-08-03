
input("Podaj liczbe: ")
input("Podaj druga liczbe: ")

print("Wynik dodawania to: ")

try:
    liczba1 = int(input("Podaj pierwsza liczbe: "))
    liczba2 = int(input("Podaj druga liczbe: "))

    wynik = liczba1 + liczba2

    print(f"Wynik dodawaniaa to: {wynik}")
except:
    print("Nie prawidlowa wartosc")