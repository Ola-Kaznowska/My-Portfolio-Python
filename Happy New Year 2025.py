import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_2025_with_text():
    text_2025 = [
        " 222222   0000   222222   55555 ",
        "     22  00  00      22  55    ",
        "  2222   00  00   2222   5555  ",
        " 22      00  00  22         55 ",
        " 222222   0000   222222   5555 "
    ]
    

    print("HAPPY NEW YEAR PROGRAMMING")

    print()

    for line in text_2025:
        print(line)

def show_new_year_message():
    clear_screen()
    print_2025_with_text()
    time.sleep(5)

def animate_2025():
    clear_screen()
    show_new_year_message()

def main():
    try:
        animate_2025()
    except KeyboardInterrupt:
        clear_screen()
        print("Goodbye and Happy New Year!")

if __name__ == "__main__":
    main()



