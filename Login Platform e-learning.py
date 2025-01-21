from flask import Flask, request, redirect, url_for, render_template_string
import smtplib

app = Flask(__name__)

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your@email.com'
EMAIL_PASSWORD = 'ccode_application_google'

# In-memory user storage (no file)
users = {}
password_reset_requests = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''
        <h1>Python PCEP your Open Job</h1>
        <a href="/login"><button>Login</button></a><br>
        <a href="/register"><button>Register</button></a>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the in-memory "database"
        if email in users and users[email]['username'] == username and users[email]['password'] == password:
            # Sending the login message (Hello PCEP)
            try:
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    message = f"Subject: Hello PCEP {username}\n\nHello PCEP, {username}!"
                    server.sendmail(EMAIL_ADDRESS, email, message)
                return "Logged in successfully! Check your email."
            except Exception as e:
                return f"Error sending email: {str(e)}"

        return "Invalid credentials, please try again."

    return '''
        <form method="post">
            <label>Email:</label><br>
            <input type="email" name="email" required><br>
            <label>Username:</label><br>
            <input type="text" name="username" required><br>
            <label>Password (min 8 characters):</label><br>
            <input type="password" name="password" required><br>
            <input type="checkbox" name="remember_me"> Remember me<br><br>
            <button type="submit">Login</button><br><br>
            <a href="/forgot-password">Forgot Password?</a>
        </form>
    '''

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # Ensure the password is at least 8 characters long
        if len(password) < 8:
            return "Password must be at least 8 characters long."

        # Check if the email is already registered
        if email in users:
            return "Email already registered."

        # Register the user in the in-memory "database"
        users[email] = {'username': username, 'password': password}

        # Send confirmation email after registration
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                message = f"""Subject: Welcome {username}\n\n
                Hi {username}, thank you for registering on the e-learning platform WWW.gostudypythonpcep.us!
                This platform was created by a young Python Back-End developer. :)
                If you are curious about my programming skills or if you are an HR recruiter testing my amazing app, check out my portfolio on GitHub: https://github.com/Ola-Kaznowska
                On our platform, you will prepare for the PCEP exam and earn the PCEP certificate for Python developers, opening doors to work in IT as a Junior/Mid Python Developer in roles such as Tester, Web Back-End Python Developer, Machine Learning, CyberSecurity, and anywhere Python is required."""
                server.sendmail(EMAIL_ADDRESS, email, message)
            
            return '''
                <h1>Registration Successful!</h1>
                <p>You will be redirected to the login page in 20 seconds.</p>
                <script type="text/javascript">
                    setTimeout(function() {
                        window.location.href = "/login";
                    }, 20000);
                </script>
            '''
        except Exception as e:
            return f"Error sending email: {str(e)}"

    return '''
        <form method="post">
            <label>Email:</label><br>
            <input type="email" name="email" required><br>
            <label>Username (min 8 characters):</label><br>
            <input type="text" name="username" required><br>
            <label>Password (min 8 characters):</label><br>
            <input type="password" name="password" required><br>
            <button type="submit">Register</button>
        </form>
    '''

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        # Check if email is registered
        if email not in users:
            return "Email not found in our records."

        # Send verification code and temporary password
        verification_code = '25-abdv0'

        # Store the reset request for validation later
        password_reset_requests[email] = {'code': verification_code, 'used': False}

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                message = f"Subject: Password Reset Request\n\nYour verification code is: {verification_code}. Please use this to reset your password."
                server.sendmail(EMAIL_ADDRESS, email, message)
            
            return '''
                <h1>Password Reset Requested</h1>
                <p>A verification code has been sent to your email. You will be redirected to the login page in 25 seconds.</p>
                <script type="text/javascript">
                    setTimeout(function() {
                        window.location.href = "/login";
                    }, 25000);
                </script>
            '''
        except Exception as e:
            return f"Error sending email: {str(e)}"

    return '''
        <form method="post">
            <label>Email:</label><br>
            <input type="email" name="email" required><br>
            <button type="submit">Send Verification Code</button>
        </form>
    '''

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        verification_code = request.form['verification_code']
        new_password = request.form['new_password']

        # Validate verification code
        if email in password_reset_requests and password_reset_requests[email]['code'] == verification_code and not password_reset_requests[email]['used']:
            # Update the user's password with the temporary one
            users[email]['password'] = '25-abdv0'
            password_reset_requests[email]['used'] = True
            return '''
                <h1>Password has been reset</h1>
                <p>You can now login with the temporary password. Please change it after the first login.</p>
                <a href="/login">Go to Login</a>
            '''

        return "Invalid verification code or this reset request has already been used."

    return '''
        <form method="post">
            <label>Email:</label><br>
            <input type="email" name="email" required><br>
            <label>Verification Code:</label><br>
            <input type="text" name="verification_code" required><br>
            <label>New Password:</label><br>
            <input type="password" name="new_password" required><br>
            <button type="submit">Reset Password</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)





