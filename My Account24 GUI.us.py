import tkinter as tk
from tkinter import messagebox

balance = 0.0

def deposit_money():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount > 0:
            balance += amount
            label_balance.config(text=f"Balance: ${balance:.2f}")
            messagebox.showinfo("Deposit", f"Successfully deposited ${amount:.2f}.")
        else:
            messagebox.showerror("Error", "Amount must be greater than 0.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")
    entry_amount.delete(0, tk.END)

def withdraw_money():
    global balance
    try:
        amount = float(entry_amount.get())
        if amount > 0:
            if amount <= balance:
                balance -= amount
                label_balance.config(text=f"Balance: ${balance:.2f}")
                messagebox.showinfo("Withdrawal", f"Successfully withdrew ${amount:.2f}.")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", "Amount must be greater than 0.")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")
    entry_amount.delete(0, tk.END)

def check_balance():
    messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")

def reset_account():
    global balance
    balance = 0.0
    label_balance.config(text=f"Balance: ${balance:.2f}")
    messagebox.showinfo("Reset", "The account has been reset to $0.0.")

root = tk.Tk()
root.title("Bank Account Simulator")

label_balance = tk.Label(root, text=f"Balance: ${balance:.2f}", font=("Arial", 16))
label_balance.pack(pady=10)

entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.pack(pady=10)

button_deposit = tk.Button(root, text="Deposit", font=("Arial", 14), command=deposit_money)
button_deposit.pack(pady=5)

button_withdraw = tk.Button(root, text="Withdraw", font=("Arial", 14), command=withdraw_money)
button_withdraw.pack(pady=5)

button_check_balance = tk.Button(root, text="Check Balance", font=("Arial", 14), command=check_balance)
button_check_balance.pack(pady=5)

button_reset = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_account)
button_reset.pack(pady=5)

root.mainloop()
