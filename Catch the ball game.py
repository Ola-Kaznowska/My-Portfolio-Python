import tkinter as tk
import random
 
class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball Game")
        self.score = 0
        self.speed = 1000  # Początkowa szybkość ruchu kulki (w milisekundach)
 
        # Ustawienia płótna (Canvas)
        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()
 
        # Tworzenie kulki
        self.ball = self.canvas.create_oval(20, 20, 60, 60, fill="red")
 
        # Wyświetlanie wyniku
        self.score_label = tk.Label(root, text="Wynik: 0", font=('Helvetica', 14))
        self.score_label.pack()
 
        # Obsługa kliknięcia na kulkę
        self.canvas.tag_bind(self.ball, "<Button-1>", self.catch_ball)
 
        # Inicjacja ruchu kulki
        self.move_ball()
 
    def move_ball(self):
        """Losowe przemieszczanie kulki po ekranie."""
        self.canvas.move(self.ball, random.randint(-200, 200), random.randint(-200, 200))
        self.canvas.after(self.speed, self.move_ball)  # Kontrola prędkości
 
    def catch_ball(self, event):
        """Reakcja na kliknięcie w kulkę."""
        self.score += 1
        self.speed = max(100, self.speed - 50)  # Zwiększenie prędkości po każdym trafieniu
        self.score_label.config(text=f"Wynik: {self.score}")
 
# Inicjacja okna tkinter
root = tk.Tk()
game = CatchTheBallGame(root)
root.mainloop()