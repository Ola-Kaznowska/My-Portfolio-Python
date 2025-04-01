from flask import Flask, render_template_string, request, redirect, url_for, session
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = 'supersecurekey'

users = {}

balance_options = list(range(500, 25001, 500))

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_adress_email'
EMAIL_PASSWORD = 'code_application_google'

base_style = """
<style>
    body { background-color: #0a0a23; color: white; text-align: center; font-family: Arial; }
    .button { background: rgba(255,255,255,0.2); border: none; padding: 10px 20px; color: white; cursor: pointer; }
    .button:hover { transform: scale(1.1); }
    .blik-logo { width: 100px; margin-top: 20px; cursor: pointer; }
    img { display: block; margin: 0 auto; }
</style>
"""

home_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>MyAccount24.US</title>
    {base_style}
</head>
<body>
    <h1>Welcome to MyAccount24.US</h1>
    <a href='/register'><button class='button'>Register</button></a>
    <a href='/login'><button class='button'>Login</button></a>
</body>
</html>
"""

register_html = f"""
<!DOCTYPE html>
<html>
<head><title>Register</title>{base_style}</head>
<body>
    <form method='post'>
        <input type='text' name='name' placeholder='Name' required>
        <input type='text' name='surname' placeholder='Surname' required>
        <input type='number' name='age' placeholder='Age' required>
        <input type='email' name='email' placeholder='Email' required>
        <input type='password' name='pin' placeholder='4-Digit PIN' required>
        <button type='submit'>Register</button>
    </form>
</body>
</html>
"""

login_html = f"""
<!DOCTYPE html>
<html>
<head><title>Login</title>{base_style}</head>
<body>
    <form method='post'>
        <input type='email' name='email' placeholder='Email' required>
        <input type='password' name='pin' placeholder='4-Digit PIN' required>
        <button type='submit'>Login</button>
    </form>
</body>
</html>
"""

dash_html = f"""
<!DOCTYPE html>
<html>
<head><title>Dashboard</title>{base_style}</head>
<body>
    <h1>Welcome Back</h1>
    <p>Balance: ${{{{ user.balance }}}}</p>
    <a href='/history'><button>View History</button></a>
    <br>
    <a href='/blik'><img src='https://cdn.prod.website-files.com/641f1c66b6257ec809fd0495/64d4ed18c477aeac330aca5c_01_16x9_F.png' class='blik-logo'></a>
</body>
</html>
"""

blik_html = f"""
<!DOCTYPE html>
<html>
<head><title>Blik Payment</title>{base_style}</head>
<body>
    <h1>Blik Payment</h1>
    <form method='post'>
        <input type='number' name='amount' placeholder='Amount' required>
        <input type='email' name='receiver_email' placeholder='Receiver Email' required>
        <input type='text' name='description' placeholder='Description' required>
        <button type='submit'>Send Blik</button>
    </form>
    <a href='/dashboard'><button>Back</button></a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        email = request.form['email']
        pin = request.form['pin']
        
        users[email] = {'name': name, 'surname': surname, 'age': age, 'pin': pin, 'balance': random.choice(balance_options), 'history': []}
        return redirect(url_for('home'))
    return render_template_string(register_html)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pin = request.form['pin']
        
        if email in users and users[email]['pin'] == pin:
            session['user'] = email
            return redirect(url_for('dashboard'))
    return render_template_string(login_html)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = users[session['user']]
        return render_template_string(dash_html, user=user)
    return redirect(url_for('login'))

@app.route('/blik', methods=['GET', 'POST'])
def blik():
    if 'user' in session:
        user = users[session['user']]
        if request.method == 'POST':
            amount = int(request.form['amount'])
            receiver_email = request.form['receiver_email']
            description = request.form['description']
            
            if user['balance'] >= amount:
                user['balance'] -= amount
                user['history'].append({'amount': amount, 'description': description})
                send_email(receiver_email, user['name'], amount, description)
                return redirect(url_for('dashboard'))
        return render_template_string(blik_html)
    return redirect(url_for('login'))

def send_email(receiver_email, sender_name, amount, description):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receiver_email
    msg['Subject'] = "New Transfer Received"
    
    body = f"User {sender_name} sent you ${amount} via MyAccount24.US. Description: {description}."
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)