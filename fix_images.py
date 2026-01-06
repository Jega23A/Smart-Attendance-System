from PIL import Image
import os

DATASET = "dataset"

for file in os.listdir(DATASET):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        try:
            path = os.path.join(DATASET, file)
            img = Image.open(path).convert("RGB")  # Force RGB
            img.save(path)  # Overwrite original
            print(f"✔ Converted: {file}")
        except Exception as e:
            print(f"❌ Skipped {file}: {e}")

print("✅ All images converted to RGB")
