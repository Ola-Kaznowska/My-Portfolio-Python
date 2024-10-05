import tkinter as tk
 
# Lista superbohaterów i ich opisy
superheroes = [
    {"name": "Superman", "description": "Superman ma nadludzką siłę, potrafi latać i ma wzrok laserowy."},
    {"name": "Batman", "description": "Batman to genialny detektyw, korzysta z technologii i gadżetów do walki ze złem."},
    {"name": "Wonder Woman", "description": "Wonder Woman jest niesamowicie silna, posiada magiczny lasso i jest amazonką."},
    {"name": "Spider-Man", "description": "Spider-Man posiada zdolność wspinania się po ścianach i wystrzeliwania pajęczyny."},
    {"name": "Iron Man", "description": "Iron Man to miliarder, który stworzył zaawansowany technologicznie pancerz bojowy."},
    {"name": "Hulk", "description": "Hulk to olbrzymia, zielona postać, która posiada niesamowitą siłę, szczególnie gdy się złości."},
]
 
class SuperheroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Superheroes Info")
 
        # Etykieta powitalna
        self.label = tk.Label(root, text="Wybierz swojego ulubionego superbohatera:", font=('Helvetica', 14))
        self.label.pack(pady=10)
 
        # Tworzenie przycisków dla każdego bohatera przy pomocy pętli
        for hero in superheroes:
            button = tk.Button(root, text=hero["name"], command=lambda h=hero: self.show_hero_info(h))
            button.pack(pady=5)
 
        # Pole do wyświetlania opisu bohatera
        self.info_label = tk.Label(root, text="", wraplength=300, font=('Helvetica', 12))
        self.info_label.pack(pady=20)
 
    def show_hero_info(self, hero):
        """Funkcja do wyświetlania informacji o wybranym bohaterze."""
        self.info_label.config(text=hero["description"])
 
# Inicjacja okna tkinter
root = tk.Tk()
app = SuperheroApp(root)
root.mainloop()