from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
from PIL import Image
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MODEL_PATH = './saved_models/50.h5'

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Load the TensorFlow model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error(f"Error loading model: {str(e)}")
    raise

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    try:
        img = Image.open(image_path)
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        logging.info(f"Image preprocessed successfully. Shape: {img_array.shape}")
        return img_array
    except Exception as e:
        logging.error(f"Error in preprocessing: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file and allowed_file(file.filename):
            # Save the file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            logging.info(f"File saved successfully: {filepath}")
            
            try:
                # Preprocess the image
                processed_image = preprocess_image(filepath)
                logging.info("Image preprocessing completed")
                
                # Make prediction
                prediction = model.predict(processed_image)
                logging.info(f"Prediction made successfully. Shape: {prediction.shape}")
                
                # Convert numpy types to Python native types
                prediction_list = prediction.tolist()
                
                result = {
                    'prediction': prediction_list,
                    'filepath': f'/static/uploads/{filename}'
                }
                
                response = {
                    'success': True,
                    'result': result,
                    'message': 'Image processed successfully'
                }
                
                logging.info("Sending successful response")
                return jsonify(response)
                
            except Exception as e:
                error_msg = f"Error processing image: {str(e)}"
                logging.error(error_msg)
                return jsonify({'error': error_msg}), 500
                
        return jsonify({'error': 'File type not allowed'}), 400
        
    except Exception as e:
        error_msg = f"Server error: {str(e)}"
        logging.error(error_msg)
        return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    app.run(debug=True)