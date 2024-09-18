import random
from time import sleep
import os
from alive_progress import alive_bar


os.system("cls" if os.name == "nt" else "clear")

name_user = input("What is your name?: ")

def multiplication_quiz():
    print(f"Welcome to the Multiplication Quiz {name_user}!")
    print()
    print("Click the mouse in the console and enter the result.")
    print()
    print("Have fun learning the multiplication tables!")
    
    score = 0
    total_questions = 5  
    
    
    for i in range(total_questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2
        
        print("Processing...")
        sleep(2)
        
        print(f"\nQuestion {i + 1}:")
        user_answer = input(f"What is {num1} x {num2}?: ")
        
        print("Checking the result in progress...")
        with alive_bar(100) as bar:
            for _ in range(100):
                sleep(0.03)
                bar()
            sleep(1)

        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print("Yes!")
                score += 1
            else:
                print(f"Incorrect! The right answer was {correct_answer}.")
        except ValueError:
            print("Please enter a valid number.")
        
        print()
    
    print(f"{name_user}, Quiz finished! Your score: {score}/{total_questions} :D")

if __name__ == "__main__":
    multiplication_quiz()