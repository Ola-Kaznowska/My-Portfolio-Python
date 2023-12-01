class Dog:
    
    def __init__(self, name, age, breed, id):
        
        self.name = name
        self.age = age
        self.breed = breed
        self.id = id
        
        
    def description(self):
        print(f"Dog with ID{self.id}:\nname: {self.name}, n\breed {self.breed}, n\age {self.age} ")
        
        
        
        
dogs = []
id = 0
while True:
    name = input("n\If you want to add a dog to the database - enter the name, if you want to search the database, enter the ID: ")
    
    if name.isdigit() == True:
        name = int(name)
        if name < len(dogs):
            dogs[name].description()
        else:
            print("Niestety takiego psa nie mamy w bazie")
    else:
        age = input("Proszę wprowadzić wiek psa: ")
        breed = input("Please enter your dog breed: ")
        dogs.append(Dog(name, age, breed, id))
        print("The dog has been added to the database and has the ID: ", id)
        id += 1       