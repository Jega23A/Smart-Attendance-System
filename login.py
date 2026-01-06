import customtkinter as ctk
from tkinter import messagebox
import json
import dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def login():
    username = entry_user.get()
    password = entry_pass.get()

    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        messagebox.showerror("Error", "users.json not found")
        return

    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Login Success", f"Welcome {username}")
        root.destroy()
        dashboard.open_dashboard(users[username]["role"])
    else:
        messagebox.showerror("Error", "Invalid username or password")


root = ctk.CTk()
root.title("Smart Attendance Login")
root.geometry("400x350")

title = ctk.CTkLabel(root, text="Smart Attendance System", font=("Arial", 20, "bold"))
title.pack(pady=20)

entry_user = ctk.CTkEntry(root, placeholder_text="Username")
entry_user.pack(pady=10, padx=40)

entry_pass = ctk.CTkEntry(root, placeholder_text="Password", show="*")
entry_pass.pack(pady=10, padx=40)

login_button = ctk.CTkButton(root, text="Login", command=login, width=150)
login_button.pack(pady=20)

root.mainloop()
