# Język programowania: Python  https://www.python.org/downloads/
# Edytor kodu (Word dla programistów): Visual Studio Code  https://code.visualstudio.com

# PLN USD EUR

# Narodowy Bank Polski

# 1) Wybór języka programowania
# 2) Programowanie = kodowanie
# 3) Testowanie = Quality Assurance (QA) = Kontrola Jakość

# W terminalu:
# python program.py
# clear / cls

# instrukcja(argument)
# zmienna = instrukcja(argument)
 
 
#(http://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/)
#(http://api.nbp.pl/api/exchangerates/rates/a/usd/2023-03-27/?format=json)

# A = kurs średnich
# B = kursów zakupu i sprzedaży

# 1. pójść do Castoramy po skrzynkę z narzędziami (z wiertarką)
# 2. wyjąć wiertarkę ze skrzynki na biurko
# 3. użyć wiertarkę

# from skrzynka import wiertarka
from requests import get

print("KALKULATOR WALUT")

waluta = input("Podaj walutę: ")

dzien = input("Podaj dzień (RRRR-MM-DD): ")

strona = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json")

dane = strona.json()

dane = {
      "table": "A",
      "currency": "dolar amerykański",
      "code": "USD",
      "rates": [
          {
              "no": "060/A/NBP/2023",
             "effectiveDate": "2023-03-27",
              "mid": 4.3518
          }
      ]
  }

kurs = dane["rates"][0]["mid"]

print(f"1 {waluta} = {kurs} PLN w dniu {dzien}")

# kwadratowa = ["jan", "alicja", "wojtek"]  # Excel z jedną kolumną (A)
# print(kwadratowa)
# print(kwadratowa[0])

# wasata = {  # Excel z dwoma kolumnami (A, B)
#     "imie": "jan",
#     "nazwisko": "kowalski",
# }
# print(wasata)
# print(wasata["nazwisko"])

# osoby = [
#     {
#         "imie": "jan",
#         "nazwisko": "kowalski",
#     },
#     {
#         "imie": "alicja",
#         "nazwisko": "wisniewska",
#     }
# ]
# print(osoby)
# print(osoby[1]["nazwisko"])   # => wisniewska

dane = {
      "table": "A",
      "currency": "dolar amerykański",
      "code": "USD",
      "rates": [
          {
              "no": "060/A/NBP/2023",
              "effectiveDate": "2023-03-27",
              "mid": 4.3518
          }
      ]
  }
print(dane["rates"][0]["mid"])  # => 4.3518