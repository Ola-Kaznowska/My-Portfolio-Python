from alive_progress import alive_bar
from time import sleep
import winsound



print("Hello.")
sleep(1)


look_for_updates = input("Type Update command to find update: ")

if look_for_updates == "update":
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(00.06)
            bar()
update_windows = input("A new application update for Windows has been found. Would you like to download it? Yes/No: ")


for i in range(2):
     if update_windows == "Yes":
         print()
         print("Please do not turn off the application or your computer. Updating..." )
         with alive_bar(100) as bar:
             for i in range(100):
                sleep(1)
                bar()


                
                
if update_windows == "No":
    print("")
    
else:
    while i in range(2):
      
     with alive_bar(100) as bar:
             for i in range(100):
                sleep(1)
                bar()
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
                break
    with alive_bar(100) as bar:
             for i in range(100):
                sleep(1)
                bar()
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) 
                break   