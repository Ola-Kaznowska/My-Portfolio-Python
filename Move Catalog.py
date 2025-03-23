import random
import time
import os 

os.system("cls" if os.name == "nt" else "clear")

My_list = [
    "Adolescence - Adolescence is the phase of life between childhood and adulthood, from ages 10 to 19. It is a unique stage of human development and an important time for laying the foundations of good health. Adolescents experience rapid physical, cognitive and psychosocial growth.",
    
    "Terminator Judgment Day - A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her ten-year-old son John from an even more advanced and powerful cyborg.",

    "Ex Machina - A psychological sci-fi thriller about a young programmer testing an AI robot named Ava, exploring themes of artificial intelligence, manipulation, and humanity.", 

    "AI Artificial Intelligence - A highly advanced robotic boy longs to become real so that he can regain the love of his human mother. Haley Joel Osment stars as David, a Mecha or robot of the future.",

    "Mr Robot - A psychological thriller series about Elliot Alderson, a hacker fighting against a corrupt corporation while battling personal demons."
]

for i in range(30):
    try:
        User = int(input("Enter your number film (1-5): "))
        if User not in range(1, 6):  
            print("Number out of range! Please enter a number between 1 and 5.")
            continue  
    except ValueError:
        print("Oops! Please enter a valid number (1-5).")
        continue  

    print("Please wait....")
    time.sleep(2)
    print(f"Your film is: {random.choice(My_list)}")