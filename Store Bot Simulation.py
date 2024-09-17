from time import sleep
import os
import random

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to PS store 2.0")
print()

sleep(2)

# Display the game list
games_list = [
    "GTA 6 PS5 - 350PLN",
    "GTA 5 PS5/PS4 - 170PLN",
    "Cyberpunk 2077 PS5/PS4 - 150PLN",
    "Unravel 2 PS5/PS4 - 125PLN",
    "Unravel PS5/PS4 - 70PLN",
    "Little nightmares 2 PS5/PS4 - 75PLN",
    "Beat Saber PSVR2/PSVR - 180PLN"
]

for game in games_list:
    print(game)


PS_PLUS = [
    "discount -80%",
    "discount -50%",
    "discount -25%",
    "FREE"
]


this_month = random.choice(PS_PLUS)

print()


user = input("Please enter the PS5 game from the list: ")


if user == "GTA 6":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added GTA6 PS5/PS4 to your shopping cart at 350PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
        
        
if user == "GTA 5":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added GTA5 PS5/PS4 to your shopping cart at 170PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
        
        
        
if user == "Cyberpunk 2077":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added Cyberpunk 2077 PS5/PS4 to your shopping cart at 150PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        

if user == "Unravel 2":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added Unravel 2 PS5/PS4 to your shopping cart at 125PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
        
        
if user == "Unravel":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added Unravel PS5/PS4 to your shopping cart at 70PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
        
if user == "Little nightmares 2":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added Nightmares 2 PS5/PS4 to your shopping cart at 75PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
        
if user == "Beat Saber":
    ps_plus_subscriber = input("Are you a PS PLUS subscriber? (yes/no): ").lower()
    if ps_plus_subscriber == "yes":
        print("Processing...")
        sleep(2)
        print(f"You received this game with a {this_month} discount!")
    elif ps_plus_subscriber == "no":
        print("Added Beat Saber PSVR2/PSVR to your shopping cart at 130PLN.")
        print()
        print("Transaction in progress...")
        sleep(3)
        print("Thank you for your purchase.")
        
   


else:
    print("This game is not available for PS PLUS promotions or has not been selected.")    