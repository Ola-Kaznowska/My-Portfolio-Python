import json 
from pprint import pprint

slownik = {"zwirze" : "pies",
           "rasa" : "husky",
           "imie" : "janusz"}
print(slownik["imie"])
print(slownik)
pprint(slownik)

print()

json_data = json.dumps(slownik)
pprint(json_data)


with open("new_file.json", "w") as file:
    json.dump(slownik, file, indent = 4)
    
    
with open("new_file.json", "r") as file:
    new_json = json.load(file)  
pprint(new_json)
    