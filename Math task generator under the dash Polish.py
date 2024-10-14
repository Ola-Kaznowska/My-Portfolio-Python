import random 
import time 
import os 

os.system("cls")

for i in range(3):
    
    a = random.randint(1000,10000)
    b = random.randint(100, a) 

    print(f'Oblicz różnicę pomiędzy {a} i {b} ')
    time.sleep(2)
    print(a-b)
 