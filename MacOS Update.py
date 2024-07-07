from alive_progress import alive_bar
from time import sleep

print("Hello.")
sleep(1)


look_for_updates = input("Type Update command to find update: ")

if look_for_updates == "update":
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(00.01)
            bar()
update_OS = input("A new application update for Mac has been found. Would you like to download it? Yes/No: ")


for i in range(25):
      if update_OS == "yes":
         print()
         with alive_bar(100) as bar:
             for i in range(100):
                sleep(00.03)
                bar()


                
                
if update_OS == "no":
    print("")
    
else:
    print(":(")