Deepfake Detection Flask API

This project is a Flask web application for detecting deepfake images using an Xception-based deep learning model.  

> Note: The trained model is not included yet. Once trained, it should be placed in the `artifacts/` folder.

---

Project Structure

DeepfakeDetectionFlask/
│
├─ app.py                  # Flask application
├─ requirements.txt        # Python dependencies
├─ README.md               # This file
└─ artifacts/              # Folder to store the trained model later

---

Setup and Run

1. Clone the repository

	```bash
	git clone https://github.com/Vidit2406/DeepfakeDetectionFlask.git
	cd DeepfakeDetectionFlask
	```
2. Install dependencies

	```bash
	pip install -r requirements.txt
	```
3. Run the Flask app

	```bash
	python app.py
	```
4. Open the web interface
	Go to http://127.0.0.1:5000/upload in your browser.

	Upload an image to check if it is Real or Fake.

Key Features – 
	1. Highlights the capabilities of your app. Example:

	2. Detects deepfake images using a pre-trained Xception model.

	3. Shows prediction confidence along with the label.

	4. Simple web interface for uploading images.

	5. Easy to replace or add new models in the artifacts/ folder.

Notes / Recommendations – 
	Important information for users:

		1. Make sure your Python environment matches requirements.txt.

		2. Add the trained model to artifacts/ before running predictions.

		3. Designed for research/testing; not for production use.