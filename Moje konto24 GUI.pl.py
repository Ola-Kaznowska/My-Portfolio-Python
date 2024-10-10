import tkinter as tk
from tkinter import messagebox
 

saldo = 0.0
 

def wplac_pieniadze():
    global saldo
    try:
        kwota = float(entry_kwota.get())
        if kwota > 0:
            saldo += kwota
            label_saldo.config(text=f"Saldo: {saldo:.2f} zł")
            messagebox.showinfo("Wpłata", f"Pomyślnie wpłacono {kwota:.2f} zł.")
        else:
            messagebox.showerror("Błąd", "Kwota musi być większa od 0.")
    except ValueError:
        messagebox.showerror("Błąd", "Podano nieprawidłową kwotę.")
    entry_kwota.delete(0, tk.END)
 
def wyplac_pieniadze():
    global saldo
    try:
        kwota = float(entry_kwota.get())
        if kwota > 0:
            if kwota <= saldo:
                saldo -= kwota
                label_saldo.config(text=f"Saldo: {saldo:.2f} zł")
                messagebox.showinfo("Wypłata", f"Pomyślnie wypłacono {kwota:.2f} zł.")
            else:
                messagebox.showerror("Błąd", "Niewystarczające środki na koncie.")
        else:
            messagebox.showerror("Błąd", "Kwota musi być większa od 0.")
    except ValueError:
        messagebox.showerror("Błąd", "Podano nieprawidłową kwotę.")
    entry_kwota.delete(0, tk.END)
 
def sprawdz_saldo():
    messagebox.showinfo("Saldo", f"Twoje aktualne saldo wynosi: {saldo:.2f} zł.")
 
def reset():
    global saldo
    saldo = 0.0
    label_saldo.config(text=f"Saldo: {saldo:.2f} zł")
    messagebox.showinfo("Reset", "Konto zostało zresetowane do 0.0 zł.")
 
 

root = tk.Tk()
root.title("Symulator Konta Bankowego")
 

label_saldo = tk.Label(root, text=f"Kasiora: {saldo:.2f} zł", font=("Arial", 16))
label_saldo.pack(pady=10)
 

entry_kwota = tk.Entry(root, font=("Arial", 14))
entry_kwota.pack(pady=10)
 

button_wplata = tk.Button(root, text="Wpłata", font=("Arial", 14), command=wplac_pieniadze)
button_wplata.pack(pady=5)
 
button_wyplata = tk.Button(root, text="Wypłata", font=("Arial", 14), command=wyplac_pieniadze)
button_wyplata.pack(pady=5)
 
button_saldo = tk.Button(root, text="Sprawdź saldo", font=("Arial", 14), command=sprawdz_saldo)
button_saldo.pack(pady=5)
 
 
button_reset = tk.Button(root, text="Reset", font=("Arial", 14), command=reset)
button_reset.pack(pady=5)
 
 

root.mainloop()