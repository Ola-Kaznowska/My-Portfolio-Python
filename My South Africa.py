from flask import Flask, render_template_string

app = Flask(__name__)

NAVBAR = """
<nav>
  <a href="/">🏠 Home</a>
  <a href="/attractions">🌟 Attractions</a>
  <a href="/beaches">🏖 Beaches</a>
  <a href="/languages">🗣 Languages</a>
  <a href="/anthem">🎶 Anthem</a>
  <a href="/whyvisit">🌍 Why Visit</a>
  <a href="/mandela">🕊 Nelson Mandela</a>
  <a href="/gallery">📸 Gallery</a>
</nav>
"""

STYLE = """
<style>
body { margin:0; font-family: 'Segoe UI', sans-serif; background:#0d1117; color:#e6edf3; }
nav { background:#111827; padding:1rem; text-align:center; position:sticky; top:0; z-index:1000; }
nav a { color:#facc15; margin:0 1rem; text-decoration:none; font-weight:bold; transition: color 0.3s ease; }
nav a:hover { color:#e11d48; }
header { text-align:center; padding:3rem 1rem; background:linear-gradient(180deg,#1f2937,#0d1117); animation: fadeIn 2s ease-in; }
header h1 { font-size:3rem; margin:0; }
header p { font-size:1.2rem; color:#9ca3af; }
section { padding:2rem; max-width:1000px; margin:auto; animation: fadeIn 1.5s ease-in; }
h2 { color:#facc15; margin-top:2rem; }
.card { background:#161b22; padding:1.5rem; border-radius:12px; margin-bottom:2rem; box-shadow:0 4px 12px rgba(0,0,0,0.5); transition: transform 0.3s ease, box-shadow 0.3s ease; }
.card:hover { transform: translateY(-5px); box-shadow:0 8px 20px rgba(0,0,0,0.7); }
.gallery { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1rem; }
.gallery img { width:100%; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.6); transition: transform 0.3s ease; }
.gallery img:hover { transform:scale(1.05); }
iframe { width:100%; height:400px; border-radius:12px; border:none; margin-bottom:1rem; box-shadow:0 4px 12px rgba(0,0,0,0.5); }
footer { text-align:center; padding:1rem; margin-top:2rem; background:#111827; color:#6b7280; }
blockquote { font-style:italic; border-left:4px solid #facc15; padding-left:1rem; color:#f0f0f0; margin-top:1rem; }
@keyframes fadeIn { from{opacity:0; transform:translateY(20px);} to{opacity:1; transform:translateY(0);} }
</style>
<script>
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({ behavior: "smooth" });
    });
  });
});
</script>
"""

HOME = f"""
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Mossel Bay ❤️ South Africa</title>{STYLE}</head>
<body>
{NAVBAR}
<header>
  <h1>🇿🇦 Welcome to Mossel Bay</h1>
  <p>Discover the historical, cultural, and natural treasures of Mossel Bay and South Africa</p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg" alt="South Africa Flag" width="180">
</header>
<section>
  <div class="card">
    <h2>About Mossel Bay</h2>
    <p>Mossel Bay is a captivating coastal town situated along South Africa’s renowned Garden Route. This town is steeped in history, having been the site of the first European settlement in South Africa. Archaeological evidence indicates that the Khoisan people lived here thousands of years ago, leaving behind a rich cultural heritage.</p>
    <p>Visitors to Mossel Bay can explore its charming streets, historic buildings, and vibrant harbor. The town combines modern tourism facilities with ancient history, offering museums, guided tours, and interactive exhibits. The coastline is famous for whale watching, fishing, and other marine activities. The weather is mild throughout the year, making it ideal for outdoor activities such as hiking along the cliffs, birdwatching, and exploring nature trails.</p>
    
  </div>
  <div class="card">
    <h2>About South Africa</h2>
    <p>South Africa is a country of extraordinary diversity and contrasts. From coastal towns like Mossel Bay to the rugged landscapes of the Drakensberg Mountains, South Africa presents an unforgettable travel experience. It has a rich history marked by colonization, struggle for freedom, and a resilient population that overcame apartheid.</p>
    <p>The country offers breathtaking landscapes, pristine beaches, mountains, and rivers. Its cultural diversity allows visitors to experience various local traditions, music, dance, and cuisine. South Africa’s cities, such as Cape Town and Johannesburg, offer a blend of modern urban life with historical landmarks. Mossel Bay, specifically, is a gateway to understanding South African history, marine biodiversity, and the beauty of the Garden Route.</p>
  </div>
</section>
<footer>🌍 Made with ❤️ in Mossel Bay, South Africa</footer>
</body>
</html>
"""

ATTRACTIONS = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Attractions</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>Attractions in Mossel Bay</h2>
<div class="card">
  <p>🏖 <b>Santos Beach</b> – This tranquil beach is perfect for families and offers safe swimming. The golden sands and calm waves provide an ideal location for sunbathing, picnicking, and beach games.</p>
  <p>🌊 <b>The Point</b> – Famous for its waves, The Point is a hotspot for surfing enthusiasts. It also offers stunning coastal views and dramatic sunsets, making it a favorite among photographers.</p>
  <p>🐳 <b>Whale Watching</b> – From June to November, southern right whales come close to the shore. Visitors can take guided boat tours to observe these magnificent creatures up close in their natural habitat.</p>
  <p>🏛 <b>Diaz Museum</b> – This museum commemorates Bartolomeu Dias, the Portuguese explorer, and showcases the history of European settlement in Mossel Bay. Exhibits include historical artifacts, maritime equipment, and interactive displays.</p>
  <p>⛴ <b>Mossel Bay Harbor</b> – A lively area with seafood restaurants, boat trips, and historical exhibits about the local fishing industry. A perfect place to enjoy fresh seafood while watching boats arrive and depart.</p>
  <p>🐢 <b>St. Blaize Trail</b> – Scenic trail along cliffs offering panoramic views of the Indian Ocean. Ideal for hiking, photography, and observing local flora and fauna.</p>
</div>
<div class="gallery">
 
</div>
</section>
<footer>❤️ Mossel Bay Tourism</footer>
</body></html>
"""

BEACHES = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Beaches</title>{STYLE}</head><body>
{NAVBAR}
<section>
  <h2>Beaches of Mossel Bay</h2>
  <div class="card">
    <p>Mossel Bay is home to numerous beautiful beaches suitable for families, surfers, and nature lovers:</p>
    <ul>
      <li>Santos Beach – Calm and safe, ideal for swimming</li>
      <li>Diaz Beach – Golden sands and picturesque shoreline</li>
      <li>The Point – Popular with surfers for strong waves</li>
      <li>Monkey Valley – Secluded, peaceful, and less crowded</li>
      <li>Victoria Bay – Small, charming cove perfect for surfing and relaxation</li>
    </ul>
    <p>Each beach has unique characteristics, from calm family-friendly waters to challenging surf spots. Visitors can enjoy walking, photography, and water activities.</p>
  </div>
  <div class="gallery">
    
  </div>
</section>
<footer>❤️ Mossel Bay Beaches</footer>
</body></html>
"""

LANGUAGES = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Languages</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>Languages of South Africa</h2>
<div class="card">
  <p>South Africa is a multilingual country with 11 official languages. Mossel Bay, located in the Western Cape, primarily uses:</p>
  <ul>
    <li><b>Afrikaans</b> – Widely spoken among locals, useful for greetings and basic conversations.</li>
    <li><b>English</b> – The primary language for tourism, business, and official communication.</li>
    <li><b>isiXhosa</b> – Rich cultural heritage, spoken by many communities in the region.</li>
  </ul>
  <p>Visitors are encouraged to learn a few phrases in Afrikaans or isiXhosa, which enhances the cultural experience and fosters positive interactions with locals.</p>
</div>
<div class="gallery">
 
</div>
</section>
<footer>🌍 Languages in South Africa ❤️</footer>
</body></html>
"""

ANTHEM = f"""
<!doctype html><html><head><meta charset="utf-8"><title>National Anthem</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>National Anthem of South Africa</h2>
<div class="card">
<p>The South African national anthem is unique because it combines five languages: Xhosa, Zulu, Sesotho, Afrikaans, and English. It reflects the country's history, unity, and diversity.</p>
<p>The lyrics speak of freedom, hope, and the aspiration for peace. Singing the anthem is a sign of respect and celebration of South Africa's journey through struggle to democracy.</p>
</div>
<iframe src="https://www.youtube.com/embed/MCSq3_aM-hY" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/NBKjWRjwMkY" allowfullscreen></iframe>
</section>
<footer>❤️ Nkosi Sikelel’ iAfrika</footer>
</body></html>
"""

WHYVISIT = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Why Visit</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>Why Visit Mossel Bay and South Africa?</h2>
<div class="card">
<p>South Africa offers travelers a rich and diverse experience, from coastal towns to mountains and historical landmarks. Mossel Bay is a perfect example of South Africa's charm, history, and natural beauty.</p>
<ul>
<li>❤️ Warm and friendly local communities</li>
<li>🏖 Pristine beaches and coastal views</li>
<li>🐘 Opportunities to explore wildlife and natural reserves</li>
<li>🏛 Rich historical and cultural sites</li>
<li>🌄 Stunning landscapes for hiking and photography</li>
<li>🕊 A place to reflect on history and celebrate resilience</li>
</ul>
<p>Visiting Mossel Bay allows tourists to immerse themselves in both South African history and the scenic beauty of the Garden Route.</p>
</div>
</section>
<footer>🌍 Visit Mossel Bay</footer>
</body></html>
"""

MANDELA = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Nelson Mandela</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>🕊 Nelson Mandela</h2>
<div class="card">
<p>Nelson Mandela (1918–2013) was a South African revolutionary, political leader, and philanthropist. He spent 27 years in prison fighting racial segregation and injustice, becoming a symbol of resilience and forgiveness worldwide.</p>
<p>Mandela served as South Africa’s first black president from 1994 to 1999, leading the nation through reconciliation and building democratic institutions. His dedication to equality, justice, and human rights changed the course of history in South Africa and inspired millions around the globe.</p>
<p>Mandela strongly believed in the transformative power of education. He once said:</p>
<blockquote>“Education is the most powerful weapon which you can use to change the world.”</blockquote>
<p>His life story encourages learning, perseverance, and working towards positive change. Visitors to South Africa often pay homage to Mandela’s legacy through museums, monuments, and cultural programs.</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/85/Nelson_Mandela.jpg" alt="Nelson Mandela" width="40%">
</div>
</section>
<footer>❤️ Remembering Nelson Mandela</footer>
</body></html>
"""

GALLERY = f"""
<!doctype html><html><head><meta charset="utf-8"><title>Gallery</title>{STYLE}</head><body>
{NAVBAR}
<section>
<h2>Gallery of Mossel Bay and South Africa</h2>
<div class="gallery">
<img src="https://www.mosselbayontheline.co.za/media/xt-adaptive-images/480/images/Photos/Mosselbaai_Peninsula.jpg" alt="Mossel Bay">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5YE2SeRusOwwIPjxwABOi8LoJll6BfP4hvw&s" alt="Beach">
<img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg" alt="Flag">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Tsitsikamma_Park.JPG/500px-Tsitsikamma_Park.JPG" alt="Garden Route">
<img src="https://www.shutterstock.com/image-photo/cape-town-western-south-africa-600nw-2485314389.jpg" alt="Cape Town">
<img src="https://mosselbay.net/wp-content/uploads/2024/07/beach-Mossel-Bay.jpg" alt="Beach">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Parking_Lot_Sunset.jpg/500px-Parking_Lot_Sunset.jpg" alt="Sunset">
</div>
</section>
<footer>📸 Memories of Mossel Bay</footer>
</body></html>
"""

@app.route("/") 
def home(): return render_template_string(HOME)

@app.route("/attractions") 
def attractions(): return render_template_string(ATTRACTIONS)

@app.route("/beaches") 
def beaches(): return render_template_string(BEACHES)

@app.route("/languages") 
def languages(): return render_template_string(LANGUAGES)

@app.route("/anthem") 
def anthem(): return render_template_string(ANTHEM)

@app.route("/whyvisit") 
def whyvisit(): return render_template_string(WHYVISIT)

@app.route("/mandela")
def mandela(): return render_template_string(MANDELA)

@app.route("/gallery") 
def gallery(): return render_template_string(GALLERY)

if __name__ == "__main__":
    app.run(debug=True)