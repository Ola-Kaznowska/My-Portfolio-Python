from flask import Flask, render_template_string, request, jsonify
import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

app = Flask(__name__)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'yourgmail@gmail.com'
EMAIL_PASSWORD = 'Your_Code_Application_GOOGLE'

CARD_FEATURES = [
    "NFC", "Hologram", "Fingerprint Sensor", "Dynamic CVV", "Dual Interface",
    "Biometric Security", "Contactless", "3D Secure", "Magstripe Backup"
]
CARD_BRANDS = ["Visa", "MasterCard"]
FLAGS = ["USA", "RPA"]
COLORS = ["glass", "gradient", "black", "white", "blue", "sky", "lightred", "pink", "purple"]

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Premium Card Ordering</title>
<h1><center>PremiumCard Studio</center></h1>
<h2><center>Design your own premium payment card with smart features and stunning styles.
Choose your color, brand, and security options — all in one click.
NFC, biometric security, and a personalized look, just for you.
Fast, secure delivery right to your doorstep.</center></h2>
<h2><center>Premium cards from the USA and South Africa — top quality, full personalization, and advanced security.</center></h2>
<style>
body {
    background: #111;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
}
.card {
    width: 320px; height: 200px;
    margin: 15px; padding: 20px;
    border-radius: 20px;
    position: relative;
    display: flex; flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 0 10px rgba(255,255,255,0.2);
    transition: transform 0.3s;
    cursor: pointer;
}
.card:hover { transform: scale(1.05); }
.card:hover .card-info { transform: translateY(0); opacity: 1; }
.card.selected { box-shadow: 0 0 30px cyan; }

.card-info {
    position: absolute;
    left: 10px; bottom: 10px;
    background: rgba(0,0,0,0.6);
    padding: 8px 12px;
    border-radius: 10px;
    font-size: 13px;
    max-width: 80%;
    transition: all 0.4s ease;
    transform: translateY(20px);
    opacity: 0;
}

.chip {
    width: 50px; height: 35px;
    border-radius: 8px;
    background: linear-gradient(135deg, gold, #d4af37);
    margin-bottom: 10px;
}

.flag-emoji {
    position: absolute;
    top: 10px; right: 15px;
    font-size: 24px;
}

.brand-label {
    position: absolute;
    bottom: 10px; right: 15px;
    font-weight: bold; font-size: 20px;
    text-shadow: 0 0 5px black;
}

/* COLORS */
.glass { backdrop-filter: blur(8px); background: rgba(255,255,255,0.1); }
.gradient { background: linear-gradient(135deg, red, orange, yellow, green); }
.black { background: #000; }
.white { background: #fff; color: #000; }
.blue { background: #3498db; }
.sky { background: #87CEEB; color: #000; }
.lightred { background: #ff6b6b; }
.pink { background: #ff69b4; }
.purple { background: #8e44ad; }

.form {
    position: fixed;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    background: #222;
    padding: 30px;
    border-radius: 15px;
    display: none;
    flex-direction: column; gap: 10px;
    width: 50%;
}
input, button {
    padding: 10px; border-radius: 8px;
    border: none; font-size: 16px;
}
button:disabled { background: grey; }
#buyBtn:enabled { background: dodgerblue; color: white; }
#success {
    position: fixed;
    top: -100px; left: 0; right: 0;
    background: lime; color: black;
    text-align: center;
    padding: 20px;
    transition: top 0.5s;
}
</style>
</head>
<body>
<div id="success">Success! Your card has been ordered.</div>
{% for c in cards %}
  <div class="card {{ c.color }}" onclick="openForm('{{c.id}}','{{c.brand}}','{{c.color}}', this)">
    <div class="chip"></div>
    <div class="flag-emoji">{{ c.flag }}</div>
    <div><span class="card-number">1234 5678 9012 3456</span></div>
    <div><span class="card-name">JOHN DOE</span></div>
    <div>CVV: <span class="card-cvv">***</span></div>
    <div class="brand-label">{{ c.brand }}</div>
    <div class="card-info">Secure {{ c.brand }} card with unique design ({{ c.color }})</div>
  </div>
{% endfor %}

<div class="form" id="form">
  <input placeholder="Full name" id="name" oninput="updateCard()">
  <input placeholder="Email address" id="email" oninput="checkForm()">
  <input placeholder="Card number (16 digits)" maxlength="16" id="cardnum" oninput="updateCard()">
  <input placeholder="CVV (3 digits)" maxlength="3" id="cvv" oninput="updateCard()">
  <button onclick="submitForm()" id="buyBtn" disabled>Order Now</button>
  <button onclick="closeForm()">Close</button>
</div>

<script>
let selectedCard = {}, lastCardDiv = null;

function openForm(id, brand, color, el) {
  selectedCard = {id, brand, color};
  document.getElementById('form').style.display = 'flex';
  if (lastCardDiv) lastCardDiv.classList.remove("selected");
  el.classList.add("selected");
  lastCardDiv = el;
}

function closeForm() {
  document.getElementById('form').style.display = 'none';
}

function updateCard() {
  document.querySelector(".card-name").innerText = document.getElementById('name').value || "JOHN DOE";
  document.querySelector(".card-number").innerText = document.getElementById('cardnum').value || "1234 5678 9012 3456";
  document.querySelector(".card-cvv").innerText = document.getElementById('cvv').value || "***";
  checkForm();
}

function checkForm() {
  const filled = document.getElementById('name').value &&
                 document.getElementById('email').value &&
                 document.getElementById('cardnum').value.length === 16 &&
                 document.getElementById('cvv').value.length === 3;
  document.getElementById('buyBtn').disabled = !filled;
}

function submitForm() {
  fetch('/buy', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({
      name: document.getElementById('name').value,
      email: document.getElementById('email').value,
      ...selectedCard
    })
  }).then(() => {
    document.getElementById('form').style.display='none';
    document.getElementById('success').style.top='0px';
    setTimeout(()=> document.getElementById('success').style.top='-100px', 3000);
  });
}
</script>
</body>
</html>
'''

@app.route("/")
def index():
    cards = []
    for i in range(12):
        cards.append({
            "id": i,
            "brand": random.choice(CARD_BRANDS),
            "color": random.choice(COLORS),
            "flag": random.choice(FLAGS)
        })
    return render_template_string(TEMPLATE, cards=cards)

@app.route("/buy", methods=["POST"])
def buy():
    data = request.json
    name, email = data['name'], data['email']
    brand, color = data['brand'], data['color']
    delivery = datetime.now() + timedelta(days=random.randint(3,14))
    msg = MIMEText(f"Dear {name},\n\nYour {brand} card in {color} color is being prepared for shipment.\nExpected delivery date: {delivery:%B %d, %Y}.\n\nThank you for your order!\n\nBest regards,\nCardTeam by O.K.")
    msg['Subject'] = f"Your {brand} Card Order Confirmation"
    msg['From'], msg['To'] = EMAIL_ADDRESS, email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls(); smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD); smtp.send_message(msg)
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True)