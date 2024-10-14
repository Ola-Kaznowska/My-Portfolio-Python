import random
import time
import os


os.system("cls")


for i in range(3):
    a = random.randint(1000, 10000)
    b = random.randint(100, a) 

    print(f'Calculate the difference between {a} and {b} ')
    
    time.sleep(2)
    print(a - b)
