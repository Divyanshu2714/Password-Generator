import random
import tkinter as tk
from tkinter import messagebox

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "<>,.?/:!@#$%^&*()_+={}[]"

def generate_password():
    upper = upper_var.get()
    lower = lower_var.get()
    nums = num_var.get()
    symbl = symbol_var.get()
    length = int(length_var.get())
    
    all_chars = ""
    if upper:
        all_chars += upper_case
    if lower:
        all_chars += lower_case
    if nums:
        all_chars += digits
    if symbl:
        all_chars += symbols
    
    if all_chars == "":
        messagebox.showerror("Error", "Select at least one character set!")
        return
    
    password = "".join(random.sample(all_chars, length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
root.geometry("480x420")
root.configure(bg="lightblue")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
num_var = tk.BooleanVar(value=False)
symbol_var = tk.BooleanVar(value=False)
length_var = tk.StringVar(value="10")
password_var = tk.StringVar()

tk.Label(root, text="Select Character Sets:" ,bg="lightblue", fg="black", font=("Arial", 16, "bold")).pack(anchor="center", padx=10)
tk.Checkbutton(root, text="Uppercase Letters", variable=upper_var ,bg="lightblue", fg="black" , font=("Arial", 16, "bold")).pack(anchor="center", padx=20)
tk.Checkbutton(root, text="Lowercase Letters", variable=lower_var ,bg="lightblue", fg="black" , font=("Arial", 16, "bold")).pack(anchor="center", padx=20)
tk.Checkbutton(root, text="Numbers", variable=num_var ,bg="lightblue", fg="black" , font=("Arial", 16, "bold")).pack(anchor="center", padx=20)
tk.Checkbutton(root, text="Symbols", variable=symbol_var ,bg="lightblue", fg="black" , font=("Arial", 16, "bold")).pack(anchor="center", padx=20)

tk.Label(root, text="Password Length:" ,bg="lightblue", fg="black", font=("Arial", 16, "bold")).pack(anchor="center", padx=10)
tk.Entry(root, textvariable=length_var, width=5 , fg="black", font=("Arial", 16, "bold")).pack(anchor="center", padx=20)
tk.Button(root, text="Generate Password", command=generate_password ,bg="#5494DA", fg="black", font=("Arial", 16, "bold")).pack(pady=10)
tk.Entry(root, textvariable=password_var, width=30, state='readonly', font=("Arial", 16, "bold")).pack(pady=3)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard ,bg="#5494DA", fg="black", font=("Arial", 16, "bold")).pack(pady=10)

root.mainloop()