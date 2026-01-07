from tqdm import tqdm
import random
import time
import os

os.system("cls")

choice = [
    "1: Scanning",
    "2: Exit"
]

threats = [
    "Scam attempt detected",
    "Malware activity found",
    "Keylogger detected",
    "Phishing website connection",
    "Suspicious login attempt"
]

support_number = "+1 555-0123"
account_id = f"US-{random.randint(100000,999999)}-{random.randint(1000,9999)}"
block_time = random.randint(5, 10)  

print(choice)
print("Welcome to the threat detection area of your bank account.\n")
print(f"Account ID: {account_id}\n")

option = input("Please enter an option: ")

if option == "1":
    print("\n🔍 Initializing security scan...\n")
    for _ in tqdm(range(100)):
        time.sleep(0.03)

    print("\nScan completed.\n")

    detected = random.choice([True, False])

    if detected:
        threat = random.choice(threats)

        print("⚠⚠⚠ SECURITY ALERT ⚠⚠⚠")
        print(f"Threat detected: {threat}")
        print(f"Account ID: {account_id}\n")

        print("🔐 Auto-Blocking System engaged:\n")
        for step in [
            "Blocking suspicious transactions",
            "Securing login access",
            "Isolating detected threat",
            "Applying temporary account lock"
        ]:
            print(step)
            for _ in tqdm(range(40)):
                time.sleep(1.40)
            print()

        print("⛔ ACCOUNT TEMPORARILY BLOCKED")
        print(f"⏳ Block duration: {block_time} minutes (simulated)\n")

        print("📞 Bank Security Support:")
        print(f"Support number: {support_number}\n")

        print("🔓 Waiting for automatic unlock...\n")
        for minute in tqdm(range(block_time)):
            time.sleep(8.10)

        print("\n✅ ACCOUNT UNLOCKED")
        print("Access has been restored.")
        print("Please change your password and review recent activity.")

    else:
        print("✅ No threats detected.")
        print("Your account is fully secure.")

elif option == "2":
    print("Exiting system...")
    for _ in tqdm(range(30)):
        time.sleep(0.03)
else:
    print("Invalid option!")