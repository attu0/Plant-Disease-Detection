# Plant Disease Detection

A web application that uses machine learning to detect diseases in plant leaves. The system can identify various plant diseases and provide recommendations for treatment.

## Features

- Upload plant leaf images through drag & drop or file selection
- Real-time disease detection using deep learning models
- Detailed disease analysis with confidence scores
- Treatment recommendations for identified diseases
- Responsive web interface for both desktop and mobile
- Support for multiple plant types and diseases
- User-friendly dashboard for viewing results

## Tech Stack

### Frontend
- React 18.x
- Vite 4.x
- Axios for API calls
- TailwindCSS for styling
- React Router for navigation
- React Dropzone for file uploads

### Backend
- FastAPI
- TensorFlow 2.x
- Python 3.10+
- Uvicorn
- OpenCV for image processing
- NumPy for numerical operations
- Pandas for data handling

## Setup

### Backend Setup
1. Navigate to the api directory:
```bash
cd api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
python main.py
```

The backend will be running on http://localhost:8000

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be running on http://localhost:5173

## Usage

1. Open the application in your browser
2. Upload an image of a plant leaf
3. The system will automatically analyze the image
4. View the results showing:
   - Plant type
   - Disease status
   - Confidence level
   - Treatment recommendations
5. Save or share the results as needed

## Project Structure

```
├── api/                    # Backend directory
│   ├── main.py            # FastAPI application
│   ├── models/            # ML model files
│   ├── utils/             # Utility functions
│   └── requirements.txt   # Python dependencies
├── frontend/              # Frontend directory
│   ├── src/              # Source files
│   │   ├── components/   # React components
│   │   ├── pages/       # Page components
│   │   ├── assets/      # Static assets
│   │   └── App.jsx      # Main application component
│   └── package.json     # Node.js dependencies
└── training/             # Training scripts and data
    ├── data/            # Training datasets
    └── notebooks/       # Jupyter notebooks
```

## Datasets

The model was trained using the following dataset:
- [Plant Disease Classification Merged Dataset](https://www.kaggle.com/datasets/alinedobrovsky/plant-disease-classification-merged-dataset?resource=download) - A comprehensive dataset containing images of various plant diseases and healthy plants.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Project Overview

This is an AI-Driven Plant Disease Recognition and Management System. The application uses deep learning to identify plant diseases from leaf images with high accuracy. It provides farmers and agricultural experts with an efficient solution for crop monitoring and disease management.

### Problem Statement

Plant diseases significantly impact agricultural productivity and farmers' livelihoods. Traditional methods of disease detection are time-consuming, require expertise, and often result in late diagnosis. Our solution addresses this gap by providing real-time, reliable disease diagnostics through an automated system that classifies leaf images into different disease categories.

### Relevance

This project is highly relevant for several reasons:

#### Agricultural Impact
- **Early Detection**: Enables timely intervention to prevent disease spread
- **Yield Protection**: Helps maintain crop yields by identifying issues early
- **Resource Optimization**: Reduces unnecessary pesticide use through accurate diagnosis

#### Technological Innovation
- **AI-Powered**: Uses state-of-the-art deep learning models for accurate classification
- **Accessible**: Provides easy-to-use interface for farmers and experts
- **Scalable**: Can be extended to support more plant types and diseases

#### Environmental Benefits
- **Sustainable Farming**: Promotes targeted treatment instead of blanket pesticide use
- **Resource Conservation**: Helps optimize water and fertilizer usage
- **Biodiversity Protection**: Reduces environmental impact of farming practices

#### Future Applications
- Mobile app integration for field use
- Integration with agricultural IoT systems
- Expansion to more plant species and diseases
