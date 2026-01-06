import os
import sys

# Fix for PyInstaller face_recognition models
if hasattr(sys, "_MEIPASS"):
    model_path = os.path.join(sys._MEIPASS, "models")
else:
    model_path = os.path.join(os.getcwd(), "models")

os.environ["FACE_RECOGNITION_MODEL_PATH"] = model_path

import cv2
import face_recognition
import numpy as np
from datetime import datetime
import csv
from PIL import Image

DATASET_DIR = "data/faces"
ATTENDANCE_FILE = "attendance.csv"

# Load known faces from dataset
def load_known_faces():
    known_encodings = []
    known_names = []

    for person in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person)
        if not os.path.isdir(person_path):
            continue

        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            try:
                image = face_recognition.load_image_file(img_path)
                # Convert image to RGB if not already
                if image.ndim == 2 or image.shape[2] != 3:
                    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                encoding = face_recognition.face_encodings(image)
                if encoding:
                    known_encodings.append(encoding[0])
                    known_names.append(person)
            except Exception as e:
                print(f"Skipped {img_path}: {e}")
    return known_encodings, known_names

# Mark attendance
def mark_attendance(name):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y,%H:%M:%S")
    
    # Create CSV if not exists
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Date", "Time"])

    # Read existing data to prevent duplicate entries per session
    with open(ATTENDANCE_FILE, "r") as f:
        existing = [line.split(",")[0] for line in f.readlines()]

    if name not in existing:
        with open(ATTENDANCE_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, now.strftime("%d-%m-%Y"), now.strftime("%H:%M:%S")])
        print(f"Attendance marked for {name}")

# Start attendance
def start_attendance():
    known_encodings, known_names = load_known_faces()
    if not known_encodings:
        print("No valid face images found!")
        return

    # Track marked names to avoid multiple entries in one session
    marked_names = set()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding, location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

                if name not in marked_names:  # Only mark once per session
                    mark_attendance(name)
                    marked_names.add(name)

            # Draw rectangle and name
            top, right, bottom, left = location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
