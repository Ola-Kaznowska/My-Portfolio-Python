from flask import Flask, request, redirect, url_for, render_template_string
import time
import smtplib

app = Flask(__name__)

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email' # Open source
EMAIL_PASSWORD = 'your_password_application' # Open source

# Sample login credentials
USERNAME = 'your_user_name' # Open source
PASSWORD = 'your_password'  # Open source

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('loading'))
        else:
            return "<h3>Invalid credentials. Please try again.</h3>"

    return render_template_string('''
        <!doctype html>
        <title>Login</title>
        <form method="post" style="width: 300px; margin: auto;">
            <h2>Login</h2>
            <label>Username:</label><br>
            <input type="text" name="username" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
            <label>Password:</label><br>
            <input type="password" name="password" minlength="5" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
            <button type="submit" style="background-color: rgb(3, 86, 252); color: white; padding: 10px 20px; border: none; cursor: pointer;">Log In</button>
        </form>
    ''')

@app.route('/loading')
def loading():
    return render_template_string('''
        <!doctype html>
        <title>Loading...</title>
        <div style="width: 100%; text-align: center; margin-top: 50px;">
            <h2>Logging in...</h2>
            <div style="background-color: #d4edda; height: 30px; width: 50%; margin: auto; border-radius: 5px; overflow: hidden;">
                <div style="background-color: #28a745; height: 100%; width: 0%; animation: load 30s linear forwards;"></div>
            </div>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = "/email";
            }, 30000);
        </script>
        <style>
            @keyframes load {
                from { width: 0%; }
                to { width: 100%; }
            }
        </style>
    ''')

@app.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                email_message = f"Subject: {subject}\n\n{message}"
                server.sendmail(EMAIL_ADDRESS, recipient, email_message)
            return "<h3>Email send successfully!</h3>"
        except Exception as e:
            return f"<h3>Error sending email: {str(e)}</h3>"

    return render_template_string('''
        <!doctype html>
        <title>Send Email</title>
        <form method="post" style="width: 300px; margin: auto;">
            <h2>Send Email</h2>
            <label>Recipient:</label><br>
            <input type="email" name="recipient" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
            <label>Subject:</label><br>
            <input type="text" name="subject" required style="width: 100%; padding: 8px; margin-bottom: 10px;"><br>
            <label>Message:</label><br>
            <textarea name="message" rows="5" required style="width: 100%; padding: 8px; margin-bottom: 10px;"></textarea><br>
            <button type="submit" style="background-color: #007BFF; color: white; padding: 10px 20px; border: none; cursor: pointer;">Send Email</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
