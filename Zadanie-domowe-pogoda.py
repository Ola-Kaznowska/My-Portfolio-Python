print("Jaka jest pogoda")
print()

for i in range(3):

    liczba = int(input("Wybierz jaka jest pogoda\n1 - słonecznie\n2 - pochmurno\n3 - deszczowo\n4 - burzowo\n5 "))






    if liczba == 1:
        print("Jest piękna pogoda możesz iść na spacer :) ")
    
    elif liczba == 2:
        print("Może zabierz ze sobą parasol. ")
 
    elif liczba == 3:
        print("Załóż kalosze i koniecznie zabierz parasol! ") 
    
    elif liczba == 4:
        print("Siedź w domu bo szkoda czsu na spacery, kiedy dookoła biją pioruny. ")  
    
    else:
        print("OJ joj joj wprowadziłeś/aś błędny kod :/ ") 
        
        
godzina = int(input("Podaj godzinę"))

if godzina >= 8 and  godzina >= 18 :
    print("Możesz wujść :)")
    
else:
    print("Nie możesz wyjść na dwór")    
        
        
        
        