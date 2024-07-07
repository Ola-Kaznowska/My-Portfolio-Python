import time
import getpass


def get_masked_input(prompt):
    return getpass.getpass(prompt)

def verifly_input(input1, input2):
    return input1 == input2


pin1 = get_masked_input("Please enter PIN: ")
pin2 = get_masked_input("Please confirm PIN: ")

password1 = get_masked_input("Please enter password: ")
password2 = get_masked_input("Please enter password: ")

if verifly_input(pin1, pin2) and verifly_input(password1, password2):
    print("Processing...")
    time.sleep(3)
    print("Authorization of the user passed successfully. Copy the link to your browser to go to Santander Bank Polska website: https://www.santander.pl/klient-indywidualny")
else:
    print("Processing...")
    time.sleep(3)
    print("PIN or password invalid")