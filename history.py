import pandas as pd
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def show_history():
    window = ctk.CTk()
    window.title("Attendance History")
    window.geometry("700x450")

    # Title
    title = ctk.CTkLabel(window, text="Attendance History", font=("Arial", 22, "bold"))
    title.pack(pady=10)

    # Scrollable textbox
    textbox = ctk.CTkTextbox(window, width=660, height=350)
    textbox.pack(padx=10, pady=10)

    # Enable vertical scrollbar
    textbox.configure(state="normal")

    try:
        df = pd.read_csv("attendance.csv")
        if df.empty:
            textbox.insert("end", "No attendance records found.")
        else:
            textbox.insert("end", df.to_string(index=False))
    except Exception:
        textbox.insert("end", "No attendance data found.")

    textbox.configure(state="disabled")  # make readonly
    window.mainloop()
