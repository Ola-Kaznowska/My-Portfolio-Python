from alive_progress import alive_bar
from time import sleep
from colorama import init
from termcolor import colored
 
init()
 




linux = "sudo apt update"

print(colored("Hello", "white"))

user_linux = input(colored("[+]Kali@kali- Wheter to update the application?: y/n: ", "blue"))

 




if user_linux == "n":
    print(colored("[+] kali@kali", "blue"))
    
    
elif user_linux == "sudo apt update":
    print(colored("root", "red"))
    print(colored("root- Update system", "red")) 
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.03)
            bar()
               
    
    
elif user_linux == "y":
    print(colored("kali@kali", "blue"))
    print(colored("kali@kali- Update system", "blue")) 
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.03)
            bar()
else:
    print("Oh no! System Crash XD")