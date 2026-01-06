import customtkinter as ctk
from register_face import register_face
from attendance import start_attendance
from export_excel import export_to_excel
from history import show_history
from reset_attendance import reset_attendance

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def open_dashboard(role):
    app = ctk.CTk()
    app.title("Smart Attendance System")
    app.geometry("500x550")  # Adjusted for all buttons

    # Title
    title = ctk.CTkLabel(app, text="Smart Attendance Dashboard", font=("Arial", 24, "bold"))
    title.pack(pady=20)

    # Logged-in role
    role_label = ctk.CTkLabel(app, text=f"Logged in as: {role}", font=("Arial", 14))
    role_label.pack(pady=10)


    # Common buttons for both admin and staff
    ctk.CTkButton(app, text="Start Attendance", width=220, height=40, command=start_attendance).pack(pady=10)
    ctk.CTkButton(app, text="Export to Excel", width=220, height=40, command=export_to_excel).pack(pady=10)
    ctk.CTkButton(app, text="View Attendance History", width=220, height=40, command=show_history).pack(pady=10)

    # Admin-only buttons
    if role == "admin":
        ctk.CTkButton(app, text="Register Face", width=220, height=40, command=register_face).pack(pady=10)
        ctk.CTkButton(app, text="Reset Attendance", width=220, height=40, fg_color="orange", command=reset_attendance).pack(pady=10)

    # Exit button
    ctk.CTkButton(app, text="Exit", width=220, height=40, fg_color="red", command=app.destroy).pack(pady=20)

    app.mainloop()
