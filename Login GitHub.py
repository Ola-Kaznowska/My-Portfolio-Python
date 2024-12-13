import getpass

def check_credentials(username, password):
    valid_username = "user"
    valid_password = "password123"
    return username == valid_username and password == valid_password

def login():
    print("Welcome to GitHub Login Simulator")
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password: ")
    
    if check_credentials(username, password):
        print("Login successful! Welcome to GitHub.")
    else:
        print("Login failed! Please check your username and password.")

if __name__ == "__main__":
    login()
