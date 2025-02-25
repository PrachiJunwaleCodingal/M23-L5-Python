#password strength checker
import tkinter as tk
from tkinter import messagebox

def check():
    password = entry.get()
    length = len(password)
    if length == 0:
        strength = "Pls enter password"
    elif length < 6:
        strength = "Weak Password"
    elif length < 10:
        strength = "Moderate Password"
    else:
        strength = "Strong Password"  
    messagebox.showinfo("Password Strength", strength)

root = tk.Tk()
root.title("Password Checker")
root.geometry("300x300")
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)
entry = tk.Entry(root, show="*")
entry.pack(pady=10)
button = tk.Button(root, text="Check Strength", command=check)
button.pack(pady=10)
root.mainloop()
