import os
from tkinter import messagebox

def reset_attendance():
    try:
        if os.path.exists("attendance.csv"):
            os.remove("attendance.csv")
        if os.path.exists("attendance.xlsx"):
            os.remove("attendance.xlsx")
        messagebox.showinfo("Success", "Attendance reset successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reset attendance:\n{e}")
