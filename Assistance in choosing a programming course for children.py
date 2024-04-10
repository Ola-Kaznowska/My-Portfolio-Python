import time
import random


print("Witaj w aplikacji pomagajcej w doborze kursu programowania")

time.sleep(1)

name = input("Podaj imię dziecka: ")

time.sleep(1)

age = input("Podaj wiek dziecka: ")

time.sleep(1)

experience = input("Podaj doświadczenie dziecka w programowaniu (w jakim języku programuje/wało): ")




def main():
    course = ["Python", 
              "C#", 
              "HTML CSS JS(Front-End)", 
              "Scratch", 
              "C++",
              "Hacking i Cyberberzbieczeństwo",
              "SQL",
              "PHP",
              "Switch",
              "Kotlin",
              ]
    
    
    
    selected_course = random.sample(course, 4)
    
    for i, course in enumerate(selected_course, start=1):
        print(f"{i}. {course}")
        
        
if __name__ == "__main__":
    main()   