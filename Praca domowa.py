# Zadanie domowe:
# Z klawiatury wprowadzamy następujące dane:
# imię, wiek, ilośc_lat. Niech nasz program napisze zdanie „jestem *wprowadzone imie*, teraz mam *nasz wiek*, a za *ilość_lat* lat będę mieć *suma naszego wieku i ilość_lat*. Byloby super jakby program nam podpowiadał co dokładnie wprowadzamy poprzez wydruk odpowiednich pytań



imie = input("Jak masz na imię?: ")
wiek = int(input("Ile masz lat?: "))
ilosc_lat = int(input("Podaj ilość lat: "))


print(f"Mam na imię {imie}, mam teraz lat {wiek} a za 5 lat będę mieć {ilosc_lat + wiek} lat/lata.")