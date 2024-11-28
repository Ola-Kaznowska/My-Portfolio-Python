import random
import os
import time
import winsound
import threading

# Function to generate a random alphanumeric string
def generate_random_string(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

    

# Function to clear the console screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the 'IDENTIFICATION PROGRAM' header
def display_identification_program():
    pin_and_program = [
        "PPPP  III  N   N    IDENTIFICATION",
        "P   P  I   NN  N        PROGRAM    ",
        "PPPP   I   N N N                   ",
        "P      I   N  NN                   ",
        "P      I   N   N                   ",
    ]
    for line in pin_and_program:
        print(line)

# Function to generate a random 4-digit PIN code
def generate_pin_code():
    return ''.join(random.choice('0123456789') for _ in range(4))

# Function to play a beep sound at the start of the program
def play_beep(frequency=1000, duration=200):
    winsound.Beep(frequency, duration)

# Function to play a continuous "processing" beep sound during scrolling
def play_processing_sound():
    while processing:  # This will keep playing the sound during the animation
        winsound.Beep(600, 125)  # Short beep for processing sound
        time.sleep(0.05)  # Small pause between beeps

# Function to play a short beep sound for each key press during PIN entry
def play_typing_sound():
    winsound.Beep(800, 100)  # Beep sound for each key press

# Function for the main program logic
def main():
    global processing
    pin_code = generate_pin_code()  # Generate random PIN

    # Display the "IDENTIFICATION PROGRAM" and "PIN" title
    clear_console()
    display_identification_program()  # Display the identification header

    # Play beep sound when the program starts
    play_beep()

    input("\nPress Enter to start...")  # Wait for user to press Enter

    # Start the processing sound in a separate thread
    processing = True
    processing_thread = threading.Thread(target=play_processing_sound, daemon=True)
    processing_thread.start()

    # Parameters for the scrolling effect
    initial_num_rows = 20  # Initial number of rows to display
    string_length = 60  # Length of each alphanumeric string
    scroll_speed = 0.26  # Speed of the scrolling effect (slower than before)
    scroll_reduction_rate = 1  # Number of rows to reduce each iteration

    num_rows = initial_num_rows
    while num_rows > 0:
        clear_console()
        display_identification_program()  # Display the identification header
        print()

        # Generate and display random alphanumeric rows
        for _ in range(num_rows):
            random_string = generate_random_string(string_length)
            print(random_string)

        # Reduce the number of rows and shorten their length
        num_rows -= scroll_reduction_rate
        string_length = max(10, string_length - 2)  # Shorten string length gradually

        # Small delay for scrolling effect
        time.sleep(scroll_speed)

    # Stop the processing sound after the scrolling animation ends
    processing = False

    # After the animation ends, display the generated PIN
    clear_console()
    display_identification_program()  # Display the identification header
    print(f"\nPIN IDENTIFICATION NUMBER: {pin_code}\n")
    play_beep()  # Beep when the PIN is revealed

    # User enters the PIN
    user_pin = input("Enter the PIN: ")

    # Play typing sound for each character entered
    for _ in user_pin:
        play_typing_sound()

    # Check if the entered PIN matches the generated PIN
    if user_pin == pin_code:
        print("Access granted.")
        play_beep(frequency=1200, duration=400)  # Success beep
    else:
        print("Access denied. Incorrect PIN.")
        play_beep(frequency=400, duration=400)  # Error beep

if __name__ == "__main__":
    main()

