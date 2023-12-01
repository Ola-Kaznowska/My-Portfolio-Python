class Moto:
    
    def __init__(self, capacity, mark, power, id):
        
        self.capacity = capacity
        self.mark = mark
        self.power = power
        self.id = id
        
        
    def description(self):
        print(f"Cross o ID {self.id}:\ncapacity: {self.capacity}, n\mark {self.mark}, n\power {self.power} ")
        
        
        
        
motorcycles = []
id = 0
while True:
    name = input("n\Jeżeli chcesz dodać Cross'a do bazy danych - wpisz markę, jeżeli chcesz wyszukać wśród bazy wpisz ID: ")
    
    if capacity.isdigit() == True:
        capacity = int(capacity)
        if capacity < len(motorcycles):
            motorcycles[capacity].description()
        else:
            print("Niestety takiego Cross'a nie mamy w bazie")
    else:
        capacity = input("Proszę wprowadzić pojemność Cross'a: ")
        mark= input("Proszę wprowadzić markę Cross'a: ")
        power = input("Proszę wprowadzić moc Cross'a: ")
        motorcycles.append(Moto(capacity, mark, power, id))
        print("Cross został dodany do bazy ma ID: ", id)
        id += 1  