import random  # Import the random module to use its random number generation functions

# Randomly select a number from 1 to 10
random_number = random.randint(1, 10)  # Generate a random integer between 1 and 10 and assign it to `random_number`

print("Welcome! I have selected a number between 1 and 10. Try to guess it!")  # Print a welcome message to the user

while True:  # Start an infinite loop for repeated guessing attempts
    try:
        guess = int(input("Enter your guess: "))  # Prompt the user for a guess and convert the input to an integer
    except ValueError:  # Catch any errors if the input is not an integer
        print("Please enter an integer.")  # Inform the user that only integers are allowed
        continue  # Skip to the next loop iteration if input was not an integer
    
    # Check if the guess is correct
    if guess < random_number:  # If the guess is lower than the random number
        print("The chosen number is higher!")  # Tell the user the number is higher than their guess
    elif guess > random_number:  # If the guess is higher than the random number
        print("The chosen number is lower!")  # Tell the user the number is lower than their guess
    else:  # If the guess is equal to the random number
        print("Congratulations! You guessed correctly.")  # Congratulate the user for guessing correctly
        break  # Exit the loop since the user has guessed correctly