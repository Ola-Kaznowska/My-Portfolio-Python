import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginFormApp(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Login Form")
        self.setGeometry(100, 100, 300, 150)  

        
       
       
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        
        form_layout = QFormLayout()

        
        username_label = QLabel("Username:")
        self.username_field = QLineEdit()

        
        password_label = QLabel("Password:")
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        
        form_layout.addRow(username_label, self.username_field)
        form_layout.addRow(password_label, self.password_field)
        form_layout.addRow(login_button)

        
        central_widget.setLayout(form_layout)

    def login(self):
        
        username = self.username_field.text()
        password = self.password_field.text()

        
        if username == "Ola" and password == "123":
            QMessageBox.information(self, "Login Successful", "Welcome, " + username + "!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

def main():
    app = QApplication(sys.argv)
    window = LoginFormApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()