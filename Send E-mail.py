from flask import Flask, request
import smtplib


app = Flask(__name__)

# SMTP Configuratuion
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email'
EMAIL_PASSWORD = 'google_app_password'

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['email']
        subject = request.form['subject']
        message_body = request.form['message']

        # Send message e-mail
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                message = f"Subject: {subject}\n\n{message_body}"
                server.sendmail(EMAIL_ADDRESS, recipient, message)
            return "Message Send!"
        except Exception as e:
            return f"ERROR: {str(e)}"

    return '''
        <form method="post">
            <label>Adres e-mail:</label><br>
            <input type="email" name="email" required><br>
            <label>topic:</label><br>
            <input type="text" name="subject" required><br>
            <label>contents of the message :</label><br>
            <textarea name="message" required></textarea><br>
            <button type="submit">Send</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)