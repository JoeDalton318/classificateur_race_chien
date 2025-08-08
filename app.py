from flask import Flask, render_template, request, send_from_directory, session
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.xception import preprocess_input
from PIL import Image
import numpy as np
import json
import os

# === Config ===
MODEL_PATH = "mon_modele(2).h5"
LABELS_PATH = "labels.json"
IMG_SIZE = (299, 299)

app = Flask(__name__)
app.secret_key = "votre_cle_secrete"  # À personnaliser pour la sécurité

# Charger le modèle
model = load_model(MODEL_PATH, compile=False)

# Charger les labels
with open(LABELS_PATH, "r", encoding="utf-8") as f:
    labels = json.load(f)

def prepare_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    img = np.array(img, dtype=np.float32)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def format_label(label):
    """Extrait le nom de la race après le tiret et le met en forme lisible."""
    return label.split('-')[-1].replace('_', ' ').capitalize()

@app.route("/", methods=["GET", "POST"])
def index():
    predictions = None
    image_filename = None

    # Initialiser l'historique et le compteur si besoin
    if "history" not in session:
        session["history"] = []
    if "count" not in session:
        session["count"] = 0

    if request.method == "POST":
        file = request.files["image"]
        if file:
            os.makedirs("uploads", exist_ok=True)
            path = os.path.join("uploads", file.filename)
            file.save(path)
            image_filename = file.filename

            # Préparer l’image et prédire
            img = prepare_image(path)
            preds = model.predict(img)[0]

            # Top-3 indices triés par proba
            top_indices = np.argsort(preds)[-3:][::-1]
            predictions = [
                {
                    "race": format_label(labels[str(i)]),
                    "confidence": float(preds[i]) * 100
                }
                for i in top_indices
            ]

            # Ajouter à l'historique
            session["history"].insert(0, {
                "image": image_filename,
                "predictions": predictions
            })
            session["history"] = session["history"][:5]  # Limite à 5 dernières analyses
            session["count"] += 1

    return render_template(
        "index.html",
        predictions=predictions,
        image_filename=image_filename,
        history=session.get("history", []),
        count=session.get("count", 0)
    )

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == "__main__":
    app.run(debug=True)