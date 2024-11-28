import time
import random

def clear_screen():
    """Clears the screen for better readability."""
    print("\033[H\033[J", end="")  # ANSI escape sequence for clearing the screen

def display_hud():
    """Displays the static HUD header."""
    print("=" * 50)
    print(" TERMINATOR T-800 VISION ".center(50, "="))
    print("=" * 50)
    print(f" MODE: COMBAT ".ljust(30), f"SYSTEM STATUS: ONLINE")
    print("=" * 50)

def draw_target(x, y):
    """Draws a target at given coordinates."""
    print("\n" * x, end="")  # Move down
    print(" " * y + "+-------+")  # Top of the target
    print(" " * y + "|   o   |")  # Center of the target
    print(" " * y + "+-------+")  # Bottom of the target

def move_target_randomly(duration=10):
    """Moves the target randomly around the screen."""
    start_time = time.time()
    while time.time() - start_time < duration:
        clear_screen()
        display_hud()
        x = random.randint(0, 10)  # Random vertical position
        y = random.randint(0, 30)  # Random horizontal position
        draw_target(x, y)
        time.sleep(0.5)

def charge_battery():
    """Simulates battery charging with a percentage animation."""
    print(f"INITIATING BATTERY CHARGING...\n")
    for percent in range(0, 101, 2):
        print(f"\rBATTERY CHARGING: {percent}%", end="")
        time.sleep(0.6)
    print(f"\nBATTERY FULLY CHARGED.\n")
    time.sleep(1)

def diagnose_system():
    """Simulates a system diagnosis and repair."""
    components = ["CPU", "Sensors", "Memory", "Power Core", "Optical System", "Targeting System"]
    damaged_components = random.sample(components, 3)

    print(f"INITIATING SYSTEM DIAGNOSIS...\n")
    for percent in range(0, 101, 5):
        print(f"\rDIAGNOSING: {percent}%", end="")
        time.sleep(0.7)
    print(f"\nDIAGNOSIS COMPLETE.\n")

    print(f"DAMAGED COMPONENTS DETECTED:")
    for component in damaged_components:
        print(f"- {component} [DAMAGED]")

    print(f"\nINITIATING REPAIRS...\n")
    for component in damaged_components:
        print(f"Repairing {component}...")
        for percent in range(0, 101, 20):
            print(f"\r{component}: {percent}% REPAIRED", end="")
            time.sleep(0.5)
        print(f" {component} REPAIRED.")

    print(f"\nALL SYSTEMS OPERATIONAL.\n")
    time.sleep(1)

def main_menu():
    """Main loop for the Terminator HUD."""
    while True:
        clear_screen()
        display_hud()
        
        print(f"Select an option:")
        print(f"1. Scan Area")
        print(f"2. Display Compass")
        print(f"3. Lock and Terminate Target")
        print(f"4. Display Moving Target (Randomized)")
        print(f"5. Charge Battery")
        print(f"6. Diagnose System")
        print(f"7. Exit\n")
        
        choice = input(f"Enter your choice (1-7): ").strip()
        
        if choice == "1":
            clear_screen()
            display_hud()
            print(f"SCANNING...\n")
            move_target_randomly(duration=10)
            input(f"Press Enter to return to menu...")
        elif choice == "2":
            clear_screen()
            display_hud()
            directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
            print(f"COMPASS: {random.choice(directions)}")
            input(f"Press Enter to return to menu...")
        elif choice == "3":
            clear_screen()
            display_hud()
            print(f"ACQUIRING TARGET...\n")
            move_target_randomly(duration=5)
            print(f"TARGET LOCKED.\n")
            input(f"Press Enter to return to menu...")
        elif choice == "4":
            clear_screen()
            display_hud()
            move_target_randomly(duration=15)
            input(f"Press Enter to return to menu...")
        elif choice == "5":
            clear_screen()
            display_hud()
            charge_battery()
            input(f"Press Enter to return to menu...")
        elif choice == "6":
            clear_screen()
            display_hud()
            diagnose_system()
            input(f"Press Enter to return to menu...")
        elif choice == "7":
            clear_screen()
            print(f"SHUTTING DOWN SYSTEM...\n")
            time.sleep(1)
            break
        else:
            print(f"Invalid choice. Please try again.")
            time.sleep(1)

# Run the main menu
main_menu()