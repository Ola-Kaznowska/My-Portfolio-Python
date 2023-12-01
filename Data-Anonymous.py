text = input("Podaj dane: ")
for digit in "0123456789":
    text = text.replace(digit, "X")
    print("Ukryte dane:", text)