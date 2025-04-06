from flask import Flask, request, redirect, url_for, render_template_string
import smtplib
from email.mime.text import MIMEText
import uuid

app = Flask(__name__)


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Your_E-mail'
EMAIL_PASSWORD = 'Your Code Application GOOGLE'

# Fake Database (demo)
pending_confirmations = {}
confirmed_emails = set()


HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: black;
        }
        form {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input[type="email"], button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <form id="signupForm" method="POST" action="/signup">
        <h2>Sign up for the Project</h2>
        <h3>Join the TurboCoders development team for an<br>internship with the opportunity to work as a <br>Junior/MID Python WEB Developer!</h3>
        <input type="email" name="email" placeholder="Your email address" required>
        <button type="submit">Sign Up</button>
    </form>
    <script>
        const form = document.getElementById('signupForm');
        form.addEventListener('submit', function() {
            alert('If you entered a valid email, you will receive a confirmation link.');
        });
    </script>
</body>
</html>
'''


SUCCESS_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Confirmation</title></head>
<body style="font-family:Arial; text-align:center; margin-top:50px; color:black;">
    <h2>Thank you! Your email has been confirmed ✅</h2>
    <script>
        alert('Welcome to TurboCoders! You are now part of our project team. 🚀');
    </script>
</body>
</html>
'''


ERROR_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Error</title></head>
<body style="font-family:Arial; text-align:center; margin-top:50px; color:black;">
    <h2>Oops! The link is invalid or has expired ❌</h2>
</body>
</html>
'''


LONG_DESCRIPTION = '''
    <h3>Welcome to the TurboCoders project!</h3>
    <p>TurboCoders is a collaborative web development project that involves a passionate team of developers. 
    The team consists of experienced Front-End Developers, Back-End Developers (Python Developers), and full-stack enthusiasts.</p>
    <p>The project is targeted for Junior Python Developers and students learning Python who are looking for practical experience in web development using Flask.</p>
    <p>By joining the project, you will:</p>
    <ul>
        <li>Collaborate with others on building real-world applications.</li>
        <li>Improve your skills and gain hands-on experience in web development.</li>
        <li>Work in a dynamic and supportive team environment.</li>
        <li>Learn best practices and improve your coding style.</li>
    </ul>
    <p>We are excited to have you onboard! Let’s build something amazing together!</p>
'''


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    confirmation_token = str(uuid.uuid4())
    pending_confirmations[confirmation_token] = email
    send_confirmation_email(email, confirmation_token)
    return redirect(url_for('home'))


@app.route('/confirm/<token>')
def confirm_email(token):
    if token in pending_confirmations:
        email = pending_confirmations.pop(token)
        confirmed_emails.add(email)
        return render_template_string(SUCCESS_PAGE)
    else:
        return render_template_string(ERROR_PAGE)


def send_confirmation_email(to_email, token):
    confirmation_link = f"http://127.0.0.1:5000/confirm/{token}"
    subject = "Confirm your project registration"
    body = f"""
    <h3>Welcome to the TurboCoders project!</h3>
    <p>TurboCoders is a collaborative web development project that involves a passionate team of developers. 
    The team consists of experienced Front-End Developers, Back-End Developers (Python Developers), and full-stack enthusiasts.</p>
    <p>The project is targeted for Junior Python Developers and students learning Python who are looking for practical experience in web development using Flask.</p>
    <p>By joining the project, you will:</p>
    <ul>
        <li>Collaborate with others on building real-world applications.</li>
        <li>Improve your skills and gain hands-on experience in web development.</li>
        <li>Work in a dynamic and supportive team environment.</li>
        <li>Learn best practices and improve your coding style.</li>
    </ul>
    <p>We are excited to have you onboard! Let’s build something amazing together!</p>
    
    <a href="{confirmation_link}" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;">Confirm Registration</a>
    """

    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        print(f"Confirmation email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(debug=True)