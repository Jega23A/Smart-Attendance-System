import cv2
import os
from PIL import Image
import numpy as np
from tkinter import simpledialog, messagebox
import tkinter as tk

def register_face():
    root = tk.Tk()
    root.withdraw()

    name = simpledialog.askstring("Register Face", "Enter person name:")
    if not name:
        messagebox.showerror("Error", "Name is required")
        return

    save_dir = os.path.join("data", "faces", name)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Press S to Save | Q to Quit", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img = img.convert("RGB")
            img_np = np.array(img).astype(np.uint8)

            file_path = os.path.join(save_dir, f"{count}.jpg")
            Image.fromarray(img_np).save(file_path)

            messagebox.showinfo("Saved", f"Face saved: {file_path}")
            break

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
