import math  


depositAmount = float(input("Specify the amount of money: "))
termInMonths = int(input("Enter the month: "))
annualInterestRate = float(input("procent: ")) / 100

amount = depositAmount +  termInMonths* ((depositAmount * annualInterestRate / 12))
print(f"Twoj zysk to:",{amount})

