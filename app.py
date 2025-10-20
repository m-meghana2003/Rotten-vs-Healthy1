import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from werkzeug.utils import secure_filename
from PIL import Image
from time import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
MODEL_PATH = 'models/healthy_vs_rotten.h5'
model = load_model(MODEL_PATH)

# Get class labelstr
try:
    DATASET_PATH = 'datasets'
    class_labels = sorted([d for d in os.listdir(DATASET_PATH) if os.path.isdir(os.path.join(DATASET_PATH, d))])
except FileNotFoundError:
    class_labels = ["Apple__Healthy", "Apple__Rotten", "Banana__Healthy", "Banana__Rotten", "Bellpepper__Healthy", "Bellpepper__Rotten", "Carrot__Healthy", "Carrot__Rotten", "Cucumber__Healthy", "Cucumber__Rotten", "Grape__Healthy", "Grape__Rotten", "Guava__Healthy", "Guava__Rotten", "Jujube__Healthy", "Jujube__Rotten", "Mango__Healthy", "Mango__Rotten", "Orange__Healthy", "Orange__Rotten", "Pomegranate__Healthy", "Pomegranate__Rotten", "Potato__Healthy", "Potato__Rotten", "Strawberry__Healthy", "Strawberry__Rotten", "Tomato__Healthy", "Tomato__Rotten"]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    timestamp = int(time())

    if request.method == 'POST':
        # Delete previous uploads
        for f in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, f)
            if os.path.isfile(file_path):
                os.remove(file_path)

        files = request.files.getlist('file')
        if not files or files[0].filename == '':
            return render_template('index.html', error="No files selected.")

        for file in files:
            filename = secure_filename(file.filename)
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(img_path)

            # Preprocess for prediction
            img = Image.open(img_path).convert('RGB')
            img_resized = img.resize((224,224))
            img_array = image.img_to_array(img_resized)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            preds = model.predict(img_array)[0]
            pred_idx = np.argmax(preds)
            prediction = class_labels[pred_idx]
            confidence = round(float(preds[pred_idx])*100, 2)

            results.append({
                'filename': filename,
                'prediction': prediction,
                'confidence': confidence
            })

    return render_template('index.html', results=results, timestamp=timestamp)
    
if __name__ == "__main__":
    ort = int(os.environ.get("PORT", 8080))  # use PORT from Railway
    app.run(host='0.0.0.0', port=port)
