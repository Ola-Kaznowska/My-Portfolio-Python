#Bierzesz udział w pierwszej fazie turnieju e-sportowego. O przejściu dalej decyduje
#liczba wygranych meczów oraz zdobytych odznaczeń MVP (Most Valuable Player).
#Aby przejść dalej należy zdobyć minimum 10 wygranych oraz mieć ich więcej niż
#przegranych lub zdobyć 7 odznaczeń MVP.
#Liczbę meczy wygranych, przegranych oraz liczbę odznaczeń MVP należy odczytać od
#użytkownika na początku programu.


Wygranych = int(input("Podaj liczbę wygranych meczy: "))
Przegranych = int(input("Podaj liczbe przegranych maczy: "))
MVP = int(input("Podaj liczbę NVP: "))


if Wygranych >= 10 and Wygranych > Przegranych or "NVP" >= 7:
    print("Wygrałeś")
else:
    print("Niestety przegrałeś")