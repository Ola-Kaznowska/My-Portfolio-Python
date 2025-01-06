import os
import time
import random
from colorama import Fore, Style, init
from alive_progress import alive_bar

os.system("cls") #Clear terminal

# Initialize colorama
init()

# Function to display the Kali Linux logo animation
def display_logo():
    dragon_logo = """
           ██╗  ██╗ █████╗ ██╗     ██╗
           ██║ ██╔╝██╔══██╗██║     ██║
           █████╔╝ ███████║██║     ██║
           ██╔═██╗ ██╔══██║██║     ██║
           ██║  ██╗██║  ██║███████╗██║
           ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    """
    for line in dragon_logo.splitlines():
        print(Fore.BLUE + line + Style.RESET_ALL)
        time.sleep(0.1)
    print()

# Function to simulate login
def login():
    print(Fore.BLUE + "Welcome to Kali Linux" + Style.RESET_ALL)
    while True:
        username = input(Fore.BLUE + "kali@kali:~$ " + Style.RESET_ALL + "Username: ")
        if username == "kali":
            break
        print("Invalid username. Try again.")

    while True:
        password = input(Fore.BLUE + "kali@kali:~$ " + Style.RESET_ALL + "Password: ")
        if password == "kali":
            break
        print("Invalid password. Try again.")

# Function to display the terminal prompt
def terminal_prompt(user, is_root=False):
    if is_root:
        return f"{Fore.RED}root@kali:~$ {Style.RESET_ALL}"
    else:
        return f"{Fore.BLUE}kali@kali:~$ {Style.RESET_ALL}"

# Function to simulate root access
def access_root():
    while True:
        password = input(Fore.RED + "root@kali:~$ " + Style.RESET_ALL + "Enter root password: ")
        if password == "kali":
            return True
        print("Invalid root password. Try again.")

# Function to simulate attacks with random success/failure reports
def simulate_attack(attack_type):
    print(f"Starting {attack_type} attack...")
    
    # Adjust duration based on attack type
    attack_duration = 25  # Attack duration is 25 seconds by default
    total_steps = int(attack_duration / 0.25)

    with alive_bar(total_steps) as bar:
        for _ in range(total_steps):
            time.sleep(0.25)  # Adjust attack duration to 25 seconds
            bar()

    # Generate random results for the attack
    result = random.choice(["success", "failure", "partial success"])
    if result == "success":
        print(Fore.GREEN + f"[*] Attack successful! Information gathered!" + Style.RESET_ALL)
    elif result == "failure":
        print(Fore.RED + f"[-] Attack failed! Unable to gather information." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"[~] Partial success. Some information was gathered, but further action needed." + Style.RESET_ALL)

    # Simulate the information gathered during the attack
    gathered_info = [
        "Email: testuser@example.com",
        "Password: 12345password",
        "Username: admin",
        "IP: 192.168.1.100",
        "Login credentials: user123 / pass456",
        "Credit Card: 4111 1111 1111 1111",
        "API Key: 87abcde123fghijklm",
        "Phone Number: +1234567890",
        "Social Security Number: 987-65-4321",
        "Wi-Fi Password: my_secure_wifi_pass",
        "Document: sensitive_info.docx",
        "Documents: index.html style.css scripts.js",
        "File: Project.py",
        "File: My_CV.pdf",
        "Document: main.cpp"
        "GitHub Token: ghp_s3cr3t_t0k3n",
        "Crypto Wallet: 1A2B3C4D5E6F7G8H9I10J"
    ]

    gathered_info.append("PIN card: 9009")
    
    print(Fore.CYAN + "Information gathered during the attack:")
    for _ in range(random.randint(1, 6)):  # Random number of pieces of information
        print(random.choice(gathered_info))
    print(Style.RESET_ALL)

    # Randomly simulate some logs
    logs = [
        "Scanning completed successfully.",
        "No vulnerabilities found, but further analysis needed.",
        "Firewall bypassed, system compromised!",
        "Access granted to the remote system.",
        "Blocked by security measures!"
    ]
    print(Fore.CYAN + random.choice(logs) + Style.RESET_ALL)
    
    # User confirmation to continue
    while True:
        continue_input = input(Fore.BLUE + "Proceed? (y/n): " + Style.RESET_ALL).lower()
        if continue_input == 'y':
            break
        elif continue_input == 'n':
            print("Exiting the attack...")
            break
        elif continue_input == '':
            break
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")

# Simulate 'apt update' operation (3 minutes)
def simulate_apt_update():
    print("Running 'apt update'...")

    # Simulate the update progress (exactly 3 minutes)
    update_duration = 180  # 3 minutes
    total_steps = int(update_duration / 0.25)

    with alive_bar(total_steps) as bar:
        for _ in range(total_steps):
            time.sleep(0.25)  # Simulate time for update
            bar()

    print(Fore.GREEN + "[*] System successfully updated!" + Style.RESET_ALL)
    print("All packages are up-to-date.")

# Main simulation loop
def kali_terminal():
    # Extended list of commands, including root access (Open Source)
    commands = {
        "1": "Simulate DDOS attack",
        "2": "Simulate DOS attack",
        "3": "Simulate BruteForce attack",
        "4": "Simulate network scan",
        "5": "Simulate phishing attack",
        "6": "Simulate malware injection",
        "7": "Simulate SQL injection",
        "8": "Simulate XSS attack",
        "9": "Simulate Man-in-the-middle attack",
        "10": "Simulate DNS spoofing",
        "11": "Simulate ARP poisoning",
        "12": "Simulate port scanning",
        "13": "Simulate vulnerability scan",
        "14": "Simulate password cracking",
        "15": "Simulate social engineering attack",
        "16": "Simulate web scraping",
        "17": "Simulate spoofing",
        "18": "Simulate RAT (Remote Access Trojan)",
        "19": "Simulate email spoofing",
        "20": "Simulate keylogging",
        "21": "Simulate IP Spoofing",
        "22": "Simulate Ransomware",
        "23": "Simulate Botnet attack",
        "24": "Simulate Cross-Site Request Forgery (CSRF)",
        "25": "Simulate DNS Cache Poisoning",
        "apt update": "Simulate apt update (System update)",
        "sudo su": "Switch to root (sudo su)",
        "exit": "Exit terminal"
    }

    # Add remaining commands dynamically up to 120 (Open Source)
    for i in range(26, 121):
        commands[str(i)] = f"Simulate generic attack {i}"

    current_user = "kali"
    is_root = False

    while True:
        # Display available commands at the top before each operation
        print("\nAvailable commands:")
        for key, value in commands.items():
            print(f"{key}: {value}")
        
        command_input = input(terminal_prompt(current_user, is_root))

        #exit command
        if command_input == "exit":
            print("Exiting Kali Linux terminal...")
            break

        #root access (sudo su)
        elif command_input == "sudo su":
            print("Switching to root mode...")
            if access_root():
                is_root = True
                current_user = "root"
                print(f"{Fore.RED}root@kali:~$ {Style.RESET_ALL}")
                continue

        #Update Kali Linux
        elif command_input == "apt update":
            simulate_apt_update()

        #other commands
        elif command_input in commands:
            print(f"\nExecuting command: {commands[command_input]}")
            simulate_attack(commands[command_input])
        else:
            print(f"Unknown command: {command_input}")
#vThe End
if __name__ == "__main__":
    display_logo() # Close draw logo function
    login() # Close login user
    kali_terminal() # Close terminarl 





