import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def select_level():
    print("Choose a difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Difficult (1–100)")

    while True:
        select = input("Select 1, 2 or 3: ")
        if select == "1":
            return 1, 10
        elif select == "2":
            return 1, 50
        elif select == "3":
            return 1, 100
        else:
            print("Incorrect selection, try again.")

def game():
    min_number, max_number = select_level()
    number_to_guess = random.randint(min_number, max_number)
    attempts = 0

    print(f"\nGuess the number from {min_number} to {max_number}!")

    while True:
        try:
            guess = int(input("Your answer: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too little!")
            elif guess > number_to_guess:
                print("Too much!")
            else:
                print(f"Bravo! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Enter a valid number.")


while True:
    clear_screen()
    game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye!")
        break
