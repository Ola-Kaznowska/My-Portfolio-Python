# Level 1: wyświetlenie "KALKULATOR WALUT"
# Level 2: zapytać użytkownika o walutę
# Level 3: wyświetl walutę z powrotem
# Level 4: wyświetl 1 USD = 4.1234 PLN

# Level 5: znalezienie spod jakie adresu można pobrać kurs waluty
# Level 6: pobranie danych z NBP
# Level 7: wyciągnięcie kursu waluty ze wszystkich danych
# Walka z bossem: co tu jest nie tak?

import requests

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

link = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json" #Naprawiony Bug: Nie bylo instrukcji f (formatowania)

strona = requests.get(link) #naprawiony Bug: w repuetsts.get zabraklo odwolania sie do zmiennej link

dane = strona.json()

kurs = dane['rates'][0]['mid']

print(f"1 {waluta} = {kurs} pln")