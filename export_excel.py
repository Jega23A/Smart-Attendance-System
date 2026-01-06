import pandas as pd
from tkinter import messagebox

def export_to_excel():
    try:
        df = pd.read_csv("attendance.csv")
        df.to_excel("attendance.xlsx", index=False)
        messagebox.showinfo("Success", "Exported to attendance.xlsx")
    except Exception as e:
        messagebox.showerror("Error", str(e))
