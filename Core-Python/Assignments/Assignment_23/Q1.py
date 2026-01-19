import tkinter as tk
from tkinter import messagebox

def login():
    if username.get() == "admin" and password.get() == "1234":
        messagebox.showinfo("Login Success", "Welcome! Login Successful")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Password").grid(row=1, column=0)

username = tk.Entry(root)
password = tk.Entry(root, show="*")

username.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=1)

root.mainloop()
