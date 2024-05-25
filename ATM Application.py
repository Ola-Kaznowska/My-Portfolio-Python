import time

print("-------------------------")

debit_card = "visa"
debit_card2 = "mastercard"
PIN = "1257", "1114", "5555"
currency = "PLN"
currency = "$"




user_id_data = input("Choose your peyment card: ")
if user_id_data == "visa":
    print("Visa card selected")
elif user_id_data == "mastercard":
    print("MasterCard selected")
    print("Processing...")
    time.sleep(3)
    
    
user_id_data = input("Enter PIN: ")
if user_id_data == "1257":
    print("Processing...")
    time.sleep(3)
    print("PIN confirmed succesfuly")
elif user_id_data == "1114":
    print("Processing...")
    time.sleep(3)
    print("PIN confirmed succesfuly")
elif user_id_data == "5555":
    print("Processing...")
    time.sleep(3)
    print("PIN confirmed succesfuly")
else:
    print("Error. Enter the correct PIN")
    
    
user_id_data = input("Select a currency - PLN/$: ")
if user_id_data == "PLN":
    print("Processing...")
    time.sleep(3)
    print("Selected PLN")
elif user_id_data == "$":
    print("Processing...")
    time.sleep(3)
    print("Selected $")
else:
    print("Error")