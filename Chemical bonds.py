from flask import Flask, render_template_string

app = Flask(__name__)

shared_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chemistry Test 2025</title>
    <style>
        body { background-color: black; color: white; text-align: center; font-family: Arial, sans-serif; margin: 0; padding: 0; overflow: hidden; }
        .buttons { margin-top: 20px; z-index: 10; position: relative; }
        .btn {
            background-color: blue;
            color: white;
            padding: 15px 30px;
            margin: 10px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            transition: transform 0.3s;
            z-index: 10;
            position: relative;
        }
        .btn:hover {
            transform: scale(1.1);
        }

        @keyframes wave {
            0% { transform: translateY(100%); }
            100% { transform: translateY(0); }
        }
        .wave {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(0,123,255,0.5) 10%, rgba(0,0,0,0) 70%);
            animation: wave 1.5s ease-out;
            z-index: 0; /* Background animation has a lower z-index */
        }

        /* Animations for pages */
        @keyframes ionAnimation {
            0% { opacity: 0; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1); }
        }
        .ion { font-size: 50px; animation: ionAnimation 1.5s ease-out; }

        @keyframes waterWave {
            0% { opacity: 0; transform: translateY(50px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .h2o { font-size: 50px; animation: waterWave 1.5s ease-out; }

        @keyframes complexAnimation {
            0% { opacity: 0; transform: rotate(0deg); }
            100% { opacity: 1; transform: rotate(360deg); }
        }
        .complex { font-size: 50px; animation: complexAnimation 1.5s ease-out; }

        /* Back button styles */
        .back-btn {
            background-color: green;
            color: white;
            padding: 15px 30px;
            margin-top: 20px;
            border: none;
            cursor: pointer;
            font-size: 18px;
            z-index: 10;
            position: relative;
        }
        .back-btn:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body>
    <div class="wave"></div>
"""

@app.route('/')
def home():
    return shared_html + """
        <h1>Chemical Bonds</h1>
        <div class="buttons">
            <button class="btn" onclick="location.href='/ionic'">Ionic Bond</button>
            <button class="btn" onclick="location.href='/covalent'">Covalent Bond</button>
            <button class="btn" onclick="location.href='/coordinate'">Coordinate Bond</button>
        </div>
    </body>
    </html>
    """

@app.route('/ionic')
def ionic():
    return shared_html + """
        <div class="ion">Na⁺ + Cl⁻ → NaCl</div>
        <h1>Ionic Bond</h1>
        <p>An ionic bond is a type of chemical bond that occurs when one atom transfers an electron to another. This results in the formation of ions with opposite charges, which are electrostatically attracted to each other. Ionic bonds are commonly found in compounds like table salt (NaCl), where sodium (Na⁺) transfers its electron to chlorine (Cl⁻), forming a stable compound.</p>
        <p>Ionic bonds are typical in salts, oxides, and other compounds where the electronegativity difference between atoms is significant. The resulting electrostatic attraction between the charged ions leads to the formation of a stable chemical compound.</p>
        <p>An everyday example of an ionic bond is table salt, whose crystal structure is formed by the interaction between sodium and chlorine ions. Ionic bonds are also present in many minerals and are responsible for their physical properties.</p>
        <button class="back-btn" onclick="location.href='/'">Back</button>
    </body>
    </html>
    """

@app.route('/covalent')
def covalent():
    return shared_html + """
        <div class="h2o">H₂ + O → H₂O</div>
        <h1>Covalent Bond</h1>
        <p>A covalent bond involves the sharing of electrons between two atoms. This is the most common type of bond in organic chemistry, especially between atoms such as oxygen (O) and hydrogen (H). In this type of bond, atoms do not transfer electrons but instead share them to achieve a full electron shell.</p>
        <p>Water (H₂O) is one of the most well-known examples of a covalent bond. Two hydrogen (H₂) atoms share electrons with an oxygen (O) atom, creating a strong covalent bond that results in a H₂O molecule. These bonds give water its unique properties, such as high boiling and melting points, which are crucial in biology and chemistry.</p>
        <p>Covalent bonds can occur in single, double, and triple forms, depending on the number of electrons shared by the atoms. They are found in many important organic substances like proteins, nucleic acids, and other macromolecules.</p>
        <button class="back-btn" onclick="location.href='/'">Back</button>
    </body>
    </html>
    """

@app.route('/coordinate')
def coordinate():
    return shared_html + """
        <div class="complex">[Cu(NH₃)₄]²⁺</div>
        <h1>Coordinate Bond</h1>
        <p>A coordinate bond is a special type of chemical bond where the electron pair comes from only one atom. This bond is unique because one atom provides both the electron and the orbital in which the electron resides. Coordinate bonds are primarily found in transition metal complexes.</p>
        <p>An example of a coordinate bond is the complex [Cu(NH₃)₄]²⁺, where copper (Cu²⁺) combines with four ammonia (NH₃) molecules to form a stable complex. Ammonia donates a lone pair of electrons to bond with copper, creating a coordinate bond. This type of bond is common in coordination chemistry and contributes to the chemical properties of complexes.</p>
        <p>Coordinate bonds are essential in various fields of chemistry, including biochemistry and catalysis. Modern research into catalysts based on transition metals often uses coordinate compounds to facilitate chemical reactions more efficiently.</p>
        <button class="back-btn" onclick="location.href='/'">Back</button>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
