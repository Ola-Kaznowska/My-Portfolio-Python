import time
import random
  

print("Energy drink calendar")
print()  

My_list = ["Oshee Rave Point 250ml",
           "Tiger Zero 250ml",
           "Black Zero Sugar 250ml",
           "RedBull Sugar Free 250ml",
           "RockStar No Sugar 250ml",
           "DOZE ZERO"]

Consumption = ["in 1 week",
               "in 2 weeks",
               "in 3 weeks"]

print("Processing...")
time.sleep(2)
print()


Selected_drink = random.choice(My_list)
Selected_time = random.choice(Consumption)
print(f"Selected {Selected_drink} {Selected_time}")