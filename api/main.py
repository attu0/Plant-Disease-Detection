from fastapi import FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Load both models
MODEL1 = tf.keras.models.load_model("saved_models/50_40.h5", compile=False)
MODEL1.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

MODEL2 = tf.keras.models.load_model("saved_models/50_20.h5", compile=False)
MODEL2.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "https://plant-disease-frontend.vercel.app",
    "https://plant-disease-frontend.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Class names for Model 1
CLASS_NAMES_MODEL1 = ['Corn__common_rust',
 'Corn__gray_leaf_spot',
 'Corn__healthy',
 'Corn__northern_leaf_blight',
 'Mango__diseased',
 'Mango__healthy',
 'Sugarcane__bacterial_blight',
 'Sugarcane__healthy',
 'Sugarcane__red_rot',
 'Sugarcane__red_stripe',
 'Sugarcane__rust',
 'Wheat__brown_rust',
 'Wheat__healthy',
 'Wheat__septoria',
 'Wheat__yellow_rust']

# Add class names for Model 2 - update with your second model's classes
CLASS_NAMES_MODEL2 = ['Pepper__bell___bacterial_spot','Pepper__bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Tomato_Bacterial_spot','Tomato_Early_blight','Tomato_Late_blight','Tomato_Leaf_Mold','Tomato_Septoria_leaf_spot','Tomato_Spider_mites_Two_spotted_spider_mite','Tomato__Target_Spot','Tomato__Tomato_YellowLeaf__Curl_Virus','Tomato__Tomato_mosaic_virus','Tomato_healthy']


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    # Resize image to 256x256
    image = image.resize((256, 256))
    # Convert to numpy array
    image = np.array(image)
    return image

@app.get("/")
async def root():
    return {"message": "Welcome to Plant Disease Detection API"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # Get predictions from Model 1
    predictions1 = MODEL1.predict(img_batch)
    confidence1 = float(np.max(predictions1[0]))
    predicted_class1 = CLASS_NAMES_MODEL1[np.argmax(predictions1[0])]
    
    # If confidence is below 95%, try Model 2
    if confidence1 < 0.97:
        predictions2 = MODEL2.predict(img_batch)
        confidence2 = float(np.max(predictions2[0]))
        predicted_class2 = CLASS_NAMES_MODEL2[np.argmax(predictions2[0])]
        
        # Return the prediction with higher confidence
        if confidence2 > confidence1:
            return {
                'class': predicted_class2,
                'confidence': confidence2,
                'model_used': 'model2'
            }
    
    # Return Model 1 predictions if confidence is >= 95% or if it's better than Model 2
    return {
        'class': predicted_class1,
        'confidence': confidence1,
        'model_used': 'model1'
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)



