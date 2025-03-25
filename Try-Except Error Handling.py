print("Hello")

try:
    User = int(input("Enter a number: "))
    print(User)
except ValueError:
    print("Please enter a number")