import random 
import os  


os.system("cls")

random_num = random.randrange(1, 200)
print("Liczba zostala wylosowana. Zgadnij :D ")


input_num = int(input("Zgadnij: "))




while input_num != random_num:
    if input_num < random_num:
        print("za mało")
    elif input_num > random_num:
        print("Za dużo")
    input_num = int(input("Zgadnij :D "))
print("Brawo wygrłałeś")
print(f"Wylosowaną liczbą było {random_num}")




