import sys
import os

os.system("cls")

# Simulated database
users_db = {}
plans = {
    "Basic": 9.99,
    "Standard": 15.49,
    "Premium": 19.99
}

def register():
    print("\n--- Register New Account ---")
    while True:
        email = input("Enter your email: ").strip()
        if email in users_db:
            print("This email is already registered. Try logging in.")
        else:
            break
    password = input("Create a password: ").strip()
    users_db[email] = {"password": password, "plan": None}
    print("Account created successfully! You can now log in.")

def login():
    print("\n--- Log In ---")
    email = input("Enter your email: ").strip()
    if email not in users_db:
        print("No account found with this email. Try registering first.")
        return None
    password = input("Enter your password: ").strip()
    if users_db[email]["password"] == password:
        print("Login successful!")
        return email
    else:
        print("Incorrect password.")
        return None

def choose_plan(user_email):
    print("\n--- Choose Your Netflix Plan ---")
    print("Available Plans:")
    for plan, price in plans.items():
        print(f" - {plan}: ${price} per month")
    while True:
        choice = input("Enter the name of the plan you want (Basic/Standard/Premium): ").strip()
        if choice in plans:
            users_db[user_email]["plan"] = choice
            print(f"You have successfully subscribed to the {choice} plan for ${plans[choice]} per month.")
            break
        else:
            print("Invalid plan. Please choose again.")

def account_details(user_email):
    print("\n--- Account Details ---")
    plan = users_db[user_email]["plan"]
    if plan:
        print(f"Email: {user_email}")
        print(f"Current Plan: {plan} (${plans[plan]} per month)")
    else:
        print("You haven't subscribed to any plan yet.")

def main():
    print("Welcome to the Netflix Simulator!")
    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                while True:
                    print("\nOptions:")
                    print("1. Choose a Plan")
                    print("2. View Account Details")
                    print("3. Log Out")
                    sub_choice = input("Choose an option (1/2/3): ").strip()

                    if sub_choice == "1":
                        choose_plan(user_email)
                    elif sub_choice == "2":
                        account_details(user_email)
                    elif sub_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == "3":
            print("Thank you for using the Netflix Simulator. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
