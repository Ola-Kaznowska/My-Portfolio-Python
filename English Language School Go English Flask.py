from flask import Flask, request, render_template_string, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'YOUR_E-MAIL' #Open-Source
EMAIL_PASSWORD = 'YOUR_CODE_APPLICATION' #Open-Source


courses = {
     'A1': {
        'title': 'Kurs Angielskiego A1 z Native Speakers',
        'description': 'Opis kursu A1: Kurs języka angielskiego na poziomie A1 w Go English Online to doskonały wybór dla osób, które dopiero rozpoczynają swoją przygodę z tym językiem lub chcą usystematyzować podstawową wiedzę. W Go English Online wierzymy, że nauka języka angielskiego od Native Speaker’ów to najskuteczniejsza metoda przyswajania języka. Ucząc się od osób, dla których angielski jest językiem ojczystym, kursanci zyskują nie tylko dostęp do autentycznej wymowy i akcentu, ale również uczą się myślenia w języku angielskim. Native Speakerzy pomagają w naturalny sposób przełamywać bariery językowe i budować pewność siebie w komunikacji. Ponadto, dzięki nauce z osobą, która zna język od urodzenia, uczestnicy kursu uczą się realnych, używanych na co dzień zwrotów i konstrukcji, a także poznają elementy kulturowe, które są nieodłączną częścią języka. Język angielski to obecnie najważniejszy język międzynarodowej komunikacji. Jest oficjalnym językiem w ponad 50 krajach i używanym przez ponad miliard osób na całym świecie. Jego znajomość otwiera drzwi do globalnych możliwości edukacyjnych, zawodowych i podróżniczych. Angielski jest także dominującym językiem w biznesie, technologii i internecie – większość treści w sieci, badań naukowych oraz międzynarodowych konferencji odbywa się właśnie w tym języku.',
        'image': 'https://m.media-amazon.com/images/I/91z+YYO7vlL._AC_UF350,350_QL80_.jpg'
    },
    'A2': {
        'title': 'Kurs Angielskiego A2 z Native Speakers',
        'description': 'Opis kursu A2: Kurs angielskiego na poziomie A2 to kolejny etap nauki dla osób, które opanowały już podstawy i chcą rozwijać swoje umiejętności językowe. Uczestnicy kursu uczą się bardziej zaawansowanego słownictwa, gramatyki oraz praktycznych zwrotów, które pozwalają na swobodniejszą komunikację w codziennych sytuacjach. Kurs koncentruje się na rozumieniu ze słuchu, budowaniu pełniejszych wypowiedzi oraz pewniejszym posługiwaniu się językiem angielskim w mowie i piśmie. Kurs A2 w Go English Online prowadzony jest przez Native Speaker’ów, co pozwala kursantom na osłuchanie się z naturalnym akcentem i autentycznym językiem. Zajęcia odbywają się w dynamicznej i przyjaznej atmosferze, co sprzyja szybkiemu przyswajaniu nowej wiedzy.',
        'image': 'https://st4.depositphotos.com/12592726/20141/i/450/depositphotos_201418792-stock-photo-sunrise-usa-flag-summer-day.jpg'
    },
    'B1': {
        'title': 'Kurs Angielskiego B1 z Native Speakers (IT Career/PCEP)',
        'description': 'Opis kursu B1 dla programistów i branży IT: Kurs języka angielskiego dla programistów w Go English Online to idealne rozwiązanie dla osób pracujących lub planujących karierę w branży IT. Język angielski jest absolutnie niezbędny dla programistów, ponieważ większość dokumentacji technicznej, kursów, tutoriali oraz forów programistycznych jest napisana w tym języku. Ponadto, firmy technologiczne na całym świecie prowadzą rekrutację w języku angielskim, a umiejętność skutecznej komunikacji w tym języku otwiera drzwi do międzynarodowych projektów i lepszych ofert pracy. Program kursu obejmuje: Słownictwo branżowe – nauka najważniejszych terminów używanych w programowaniu, DevOps, analizie danych i innych specjalizacjach IT, Pisanie i czytanie dokumentacji technicznej – zrozumienie i tworzenie specyfikacji technicznych, komentarzy do kodu oraz raportów, Komunikacja w środowisku pracy – udział w spotkaniach zespołowych, rozmowach rekrutacyjnych i prezentacjach projektów, Rozumienie nagrań i wykładów technicznych – ćwiczenie słuchania i analizowania treści z międzynarodowych konferencji IT, Przygotowanie do rozmów kwalifikacyjnych – rozwijanie umiejętności odpowiadania na pytania techniczne i opisania własnych projektów w języku angielskim. Język angielski jest standardem w świecie technologii. Oto kilka powodów, dla których jego znajomość jest kluczowa dla programistów: Globalna dokumentacja – większość języków programowania, frameworków i narzędzi posiada dokumentację wyłącznie w języku angielskim, Społeczność IT – popularne fora i społeczności, takie jak Stack Overflow, GitHub czy Dev.to, operują głównie w języku angielskim, Międzynarodowe zespoły – wiele firm IT pracuje w globalnym środowisku, gdzie angielski jest podstawowym językiem komunikacji, Dostęp do najlepszych kursów i zasobów – większość nowoczesnych kursów online i konferencji technologicznych odbywa się w języku angielskim, Możliwość pracy zdalnej – znajomość angielskiego pozwala na podjęcie pracy w międzynarodowych firmach bez konieczności przeprowadzki. Kurs na poziomie B1 dla programistów obejmuje także przygotowanie do prestiżowego certyfikatu PCEP (Certified Entry-Level Python Programmer). Jest to międzynarodowy certyfikat potwierdzający podstawowe umiejętności w języku Python, który stanowi doskonały punkt wyjścia do dalszej kariery w IT. Zdobycie certyfikatu PCEP zwiększa szanse na zatrudnienie na stanowiskach juniorskich w Pythonie, otwierając drzwi do pierwszej pracy w branży IT. Egzamin PCEP wymaga znajomości języka angielskiego, ponieważ cały egzamin odbywa się w tym języku – zarówno pytania, dokumentacja, jak i materiały szkoleniowe. Uczestnicy muszą także wykazać się umiejętnością rozumienia poleceń oraz technicznej terminologii w języku angielskim.',
        'image': 'https://www.citylit.ac.uk/media/catalog/product/cache/7c1110bc2aba24b121586d9ef95eca3c/i/n/introduction-to-python-cppy01_10.jpg'
    },
    'B2': {
        'title': 'Kurs Angielskiego B2 z Native Speakers',
        'description': 'Opis kursu B2: Kurs angielskiego na poziomie B2 skierowany jest do osób, które chcą osiągnąć zaawansowany poziom znajomości języka i swobodnie komunikować się w różnych sytuacjach. Uczestnicy kursu rozwijają umiejętność płynnej konwersacji, uczą się skomplikowanych struktur gramatycznych oraz doskonalą swoje umiejętności czytania i pisania na wyższym poziomie.',
        'image': 'https://dreamgo.pl/wp-content/uploads/2020/03/Santa-Monica-Los-Angeles-Kalifornia.jpg'
    },
    'C1': {
        'title': 'Kurs Angielskiego C1 z Native Speakers',
        'description': 'Opis kursu C1: Kurs angielskiego na poziomie C1 w Go English Online to propozycja dla osób, które posługują się językiem angielskim na poziomie zaawansowanym i chcą doskonalić swoje umiejętności w sposób profesjonalny. Skierowany jest do studentów, specjalistów oraz wszystkich, którzy pragną osiągnąć wysoki poziom płynności językowej.',
        'image': 'https://tv-english.club/wp-content/uploads/2014/12/advanced.jpg'
    },
    'C2': {
        'title': 'Kurs Angielskiego C2 z Native Speakers',
        'description': 'Opis kursu C2: Kurs angielskiego na poziomie C2 w Go English Online to najwyższy poziom zaawansowania, przeznaczony dla osób, które chcą osiągnąć pełną biegłość językową. Jest skierowany do profesjonalistów, akademików, tłumaczy oraz wszystkich, którzy pragną swobodnie komunikować się w języku angielskim w każdej sytuacji. Kurs C2 pozwala na swobodne funkcjonowanie w środowisku akademickim i zawodowym na poziomie native speakera. Jest doskonałym przygotowaniem do egzaminów takich jak CPE (Certificate of Proficiency in English) oraz do pracy wymagającej najwyższej precyzji językowej.',
        'image': 'https://i.pinimg.com/736x/6c/c4/b2/6cc4b295b491f9811bf25e9171e1e66f.jpg'
    }
}


@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Go English - Kursy Angielskiego Online</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .h1{
            font-size: 3em; 
            font-weight: bold; 
            text-transform: uppercase;
            text-align: center;
            margin: 20px 0; 
            color: #333;
            font-family: Arial, sans-serif;
        }
         h2 {
    color:rgb(30, 45, 255); 
    font-size: 1.5em; 
    text-align: left; 
    margin: 20px 0; 
    font-family: Arial, sans-serif; 
}
            .course { border: 1px solid #ccc; padding: 20px; margin: 20px; }
            .course img { max-width: 100%; height: auto; }
            .course button { background-color: green; color: white; padding: 10px; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Angielski Online <br>z Native<br>Speakers</h1>
        <h2>Jesteśmy internetową szkołą<br>językową w której zaczniesz dużo<br>lepiej mówić po angielsku!</h2>
        <p>Wybierz kurs odpowiedni dla siebie:</p>
        {% for key, course in courses.items() %}
            <div class="course">
                <h2>{{ course.title }}</h2>
                <img src="{{ course.image }}" alt="{{ course.title }}">
                <p>{{ course.description }}</p>
                <form action="{{ url_for('course_detail', level=key) }}" method="get">
                    <button type="submit">Zarezerwuj kurs</button>
                </form>
            </div>
        {% endfor %}

         <h3>Kursy Języka Angielskiego przez platformę <h2 style="color:#1805ed;">Zoom</h2>
            
          
    </body>
    </html>
    ''', courses=courses)


@app.route('/course/<level>', methods=['GET', 'POST'])
def course_detail(level):
    course = courses.get(level)
    if not course:
        return "Nie znaleziono takiego kursu.", 404

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        card_number = request.form['card_number']

        subject = 'Potwierdzenie rezerwacji kursu'
        payment_link = 'https://card867655mycourse=6446346464'
        message_body = f'''
        Dzień dobry {name},

Dziękujemy za zapisanie się na {course['title']} w Go English!

Prowadzący: John Connor
Link do zajęć online (Zoom): https://us05web.zoom.us/j/1234567890?pwd=example
Meeting ID: 123 456 7890
Passcode: 125

Oto link do miesięcznej płatności: {payment_link}

Uproszczona treść Regulaminu Szkoły Angielskiego Go English dotycząca najważniejszych zasad współpracy.
Aby skorzystać z kursów, klient musi zaakceptować regulamin i dokonać opłaty.
Szczegóły dotyczące płatności i organizacji zajęć są ustalane indywidualnie lub zawarte w opisie kursu.
W przypadku zajęć online, uczestnik musi posiadać odpowiedni sprzęt i dostęp do Internetu.
W przypadku problemów technicznych związanych z dostępem do kursu, odpowiedzialność spoczywa na uczestniku, chyba że problem wynika z działania organizatora.
Materiały kursowe są chronione prawem autorskim i przeznaczone wyłącznie do użytku osobistego uczestnika.
Szkoła może rejestrować zajęcia dla celów edukacyjnych, ale wykorzystanie wizerunku uczestnika do celów marketingowych wymaga dodatkowej zgody.
(pełna treść regulaminu)
        
Pozdrawiamy,
Aleksandra Kaznowska
Go English
Telefon: 598 235 659
        '''

        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            return f"E-mail potwierdzający został wysłany na adres {email}."
        except Exception as e:
            return f"Wystąpił błąd podczas wysyłania e-maila: {str(e)}"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>{{ course.title }} - Go English</title>
    </head>
    <body>
        <h1>{{ course.title }}</h1>
        <img src="{{ course.image }}" alt="{{ course.title }}">
        <p>{{ course.description }}</p>
        <h2>Formularz rezerwacji</h2>
        <form method="post">
            <label for="name">Imię i nazwisko:</label><br>
            <input type="text" id="name" name="name" required><br>
            <label for="email">Adres e-mail:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="card_number">Numer karty:</label><br>
            <input type="text" id="card_number" name="card_number" required><br>
            <button type="submit">Zarezerwuj</button>
        </form>
    </body>
    </html>
    ''', course=course)

if __name__ == '__main__':
    app.run(debug=True)