import tkinter as tk
from tkinter import messagebox
 
class SuperheroQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Superhero Quiz for Kids")
 
        # Wynik i numer pytania
        self.score = 0
        self.question_number = 0
 
        # Lista pytań o superbohaterach
        self.questions = [
            {"question": "Który superbohater nosi pelerynę?", "options": ["Iron Man", "Superman", "Spider-Man", "Hulk"], "answer": "Superman"},
            {"question": "Który bohater jest miliarderem?", "options": ["Batman", "Thor", "Flash", "Wonder Woman"], "answer": "Batman"},
            {"question": "Który superbohater posiada tarczę?", "options": ["Spider-Man", "Captain America", "Wolverine", "Aquaman"], "answer": "Captain America"},
            {"question": "Który bohater został ukąszony przez radioaktywnego pająka?", "options": ["Iron Man", "Spider-Man", "Hulk", "Batman"], "answer": "Spider-Man"},
            {"question": "Który bohater zamienia się w ogromnego zielonego stwora?", "options": ["Thor", "Flash", "Hulk", "Doctor Strange"], "answer": "Hulk"},
        ]
 
        # Interfejs użytkownika
        self.question_label = tk.Label(root, text="", font=('Helvetica', 14), wraplength=400)
        self.question_label.pack(pady=20)
 
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=('Helvetica', 12), width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)
 
        # Start gry
        self.next_question()
 
    def next_question(self):
        """Załaduj następne pytanie do interfejsu."""
        if self.question_number < len(self.questions):
            current_question = self.questions[self.question_number]
            self.question_label.config(text=current_question["question"])
            for i, option in enumerate(current_question["options"]):
                self.option_buttons[i].config(text=option)
        else:
            self.show_score()
 
    def check_answer(self, chosen_option_index):
        """Sprawdź poprawność odpowiedzi i przejdź do kolejnego pytania."""
        correct_answer = self.questions[self.question_number]["answer"]
        chosen_answer = self.option_buttons[chosen_option_index].cget("text")
 
        if chosen_answer == correct_answer:
            self.score += 1
 
        self.question_number += 1
        self.next_question()
 
    def show_score(self):
        """Wyświetl końcowy wynik i zapytaj, czy gracz chce zagrać ponownie."""
        messagebox.showinfo("Koniec gry", f"Twój wynik: {self.score}/{len(self.questions)}")
        self.question_number = 0
        self.score = 0
        self.next_question()
 
# Inicjacja aplikacji tkinter
root = tk.Tk()
quiz_app = SuperheroQuizApp(root)
root.mainloop()