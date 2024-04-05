def menu_glowne():
    print("1. Wpłata")
    print("2. Wypłata")
    print("3. Saldo")
    print("4. Wyjście")
    
    
    
    def pobierz_wybor():
        return int(input("Twój wybór to: "))
    
    def pobierz_kwote(tekst):
        return float(input(tekst))
    
    def wyswietl_saldo(saldo):
         print(f"Aktualny stan memont{saldo}zl")
    
    def wplata(saldo):
        
        
        kwota = pobierz_kwote("ile chcesz wpłacić?: ")
        saldo = saldo + kwota
        wyswietl_saldo(saldo)
        return saldo
    
        pass
    
    def wyplata(saldo):
        kwota = pobierz_kwote("Ile chcesz wypłacić?: ")
        if kwota < saldo:
         saldo = saldo - kwota 
        else:
            print("ZAKAZ OBRABIANIA BANKÓW!!!")
        wyswietl_saldo(saldo)
        return saldo 
    pass
    def pobierz_dane(dane):
        return input("Podaj dane {dane}: ")


    def spr_zgodnosci(baza, pobrane):
        return baza == pobrane
    
    saldo = 0
    wybor = 0
    karta = "125"
    PIN = "110"
    
    
    podana_karta = pobierz_dane("karty")
    podany_PIN = pobierz_dane("PIN")
    
    if spr_zgodnosci(karta, podana_karta) and spr_zgodnosci(PIN, podany_PIN):
    
    
    
        while wybor != 4:
            #główna pętla
            menu_glowne()
            
            wybor = pobierz_wybor()
            
            if wybor == 1:
                saldo = wplata(saldo)
                pass
            elif wybor == 2:
                
                pass
            elif wybor == 3:
                wyswietl_saldo(saldo)
                pass
            elif wybor == 4:
                print("Dziękuję za wspópracę:) ")
                pass
            else:
                print("Błąd")