# Function to add contacts
def add_contacts():
    contacts = {}  # Dictionary to store contacts

    print("Welcome to the contact book!")
    print("To stop adding contacts, type 'p' as the name.")

    while True:
        # Prompt the user for contact details
        name = input("Enter contact name (or 'q' to quit): ")

        # Check if the user wants to print
        if name == 'p':
            break
        
        phone = input("Enter phone number: ")

        # Save contact in dictionary
        contacts[name] = phone
        print(f"Added contact: {name} - {phone}")

    return contacts

# Function to display all contacts
def display_contacts(contacts):
    print(f"Your contact book:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Main code
contacts = add_contacts()
display_contacts(contacts)
