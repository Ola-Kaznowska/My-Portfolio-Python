from flask import Flask

# Tworzymy aplikację Flask
app = Flask(__name__)

# Definiujemy trasę główną ("/") i jej działanie
@app.route('/')
def hello_world():
    return 'Hello Flask!'

# Uruchamiamy aplikację
if __name__ == '__main__':
    app.run(debug=True)
