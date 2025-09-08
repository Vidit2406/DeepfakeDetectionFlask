from flask import Flask, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the trained model once at startup
model = tf.keras.models.load_model("deepfake_xception_model.keras")  # Updated path

@app.route('/')
def home():
    return "Deepfake Detection API is running. Use /upload to upload images."

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return "No file uploaded", 400

        # Preprocess the uploaded image
        img = Image.open(file.stream).convert("RGB").resize((299, 299))
        img_array = np.array(img).astype(np.float32)
        img_array = tf.keras.applications.xception.preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make prediction
        pred_prob = model.predict(img_array)[0][0]
        label = "Fake" if pred_prob >= 0.5 else "Real"
        confidence = pred_prob if label == "Fake" else 1 - pred_prob

        # Show prediction result with confidence
        return f'''
            <html>
                <body>
                    <h2>Prediction: {label}</h2>
                    <p>Confidence: {confidence*100:.2f}%</p>
                    <a href="/upload">Try another image</a>
                </body>
            </html>
        '''

    # GET request: show upload form
    return '''
        <html>
            <body>
                <h2>Upload Image for Deepfake Detection</h2>
                <form action="/upload" method="post" enctype="multipart/form-data">
                  <input type="file" name="file" required>
                  <input type="submit" value="Upload">
                </form>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)