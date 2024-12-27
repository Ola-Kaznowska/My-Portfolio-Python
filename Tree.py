import time
import os

# Funkcja do czyszczenia ekranu
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funkcja rysująca kwiatka
def draw_flower(stage):
    flower = [
        "     @     ",
        "    @@@    ",
        "   @@@@@   ",
        "  @@@@@@@  ",
        " @@@@@@@@@ ",
        "@@@@@@@@@@@",
        "     |     ",
        "     |     "
    ]
    
    # Rozmiar kwiatka zmienia się w zależności od etapu
    flower_stage = flower[:stage]
    
    clear_screen()
    for line in flower_stage:
        print(line)
    time.sleep(0.5)

# Główna część programu
def grow_flower():
    for stage in range(1, 9):
        draw_flower(stage)

if __name__ == "__main__":
    grow_flower()


