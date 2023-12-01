czy_dobry_klucz = False
czy_kontynuacja = True


while czy_kontynuacja:
    #sprawdzenie poprawnośći klucza
    while not czy_dobry_klucz:
        klucz = input("Podaj klucz do szyfrowania: ")
        klucz = klucz.lower()
        czy_dobry_klucz = True
        
        #warunek parzystej ilości liter
        liczba_liter_klucza = len(klucz)
        if not liczba_liter_klucza % 2 == 0:
            czy_dobry_klucz = False
            print(f"klucz {klucz} jest błędny")
            break
        
        
        
        #Szyfrowanie
        
        
        tekst = input("Podaj tekst do zaszyfrowania: ")
        tekst = tekst.lower()
        zaszyfrowany = ""
        
        
        
        
        
        
        for litera in tekst:
            if litera in klucz:
                miejsce_w_kluczu = klucz.find(litera)
                if miejsce_w_kluczu % 3 == 0:
                    zaszyfrowany += klucz[miejsce_w_kluczu+1]
                else:
                    zaszyfrowany += klucz[miejsce_w_kluczu-1]
            else:
                zaszyfrowany += litera
        print(f"{tekst} po zaszyfrowaniu kluczem {klucz} wygląda następująco {zaszyfrowany}")
        
        
        
        kontynuacja = input("Czy chcesz coś jeszcze zaszyfrować?: ")
        kontynuacja = kontynuacja.lower()
        if kontynuacja == "tak" or "Tak":
            czy_kontynuacja = True
            czy_nowy_klucz = input("czy chcesz zmienić klucz szyfrowania?: ")
            czy_nowy_klucz = czy_nowy_klucz.lower()
            if czy_nowy_klucz == "tak":
                czy_dobry_klucz = False
        else:
            czy_kontynuacja = False
    
    print("Koniec programu")
                
            
        
                   
                   
                   
                   