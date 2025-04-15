# EVS PROJECT

# Plant Disease Detection

A web application that uses machine learning to detect diseases in plant leaves. Currently supports potato plant disease detection.

## Features

- Upload images through drag & drop or file selection
- Real-time disease detection
- Confidence score for predictions
- Responsive design
- Support for multiple plant types 

## Tech Stack

### Frontend
- React
- Vite
- Axios
- CSS3

### Backend
- FastAPI
- TensorFlow
- Python 3.x
- Uvicorn

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
3. Click "Submit Image" to analyze
4. View the results showing plant type, disease status, and confidence level

## Project Structure

```
├── api/                    # Backend directory
│   ├── main.py            # FastAPI application
│   └── requirements.txt    # Python dependencies
├── frontend/              # Frontend directory
│   ├── src/              # Source files
│   │   ├── components/   # React components
│   │   └── App.jsx       # Main application component
│   └── package.json      # Node.js dependencies
└── saved_models/         # ML model directory
    └── 50.h5            # Trained model
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Project Overview

This is an AI-Driven Vegetable Disease Recognition and Management Recommendations model. Discover the future of farming with our AI-powered website designed to recognize vegetable diseases with unprecedented accuracy. By identifying early signs of pest infestation to diagnosing nutrient deficiencies, the tool is an ultimate farming companion. By automated systems can effectively identify diseases and recommend solutions based on leaf images, providing farmers and agricultural experts with an efficient solution for crop monitoring and disease management.

### Problem Statement

Vegetable crops are highly susceptible to a variety of diseases, significantly impacting yield and farmers' livelihoods. Traditional methods of disease detection are time-consuming, require expertise, and often result in late diagnosis. Leveraging AI technology can address this gap by providing real-time, reliable disease diagnostics. This project aims to develop an automated system to classify leaf images into different categories, including healthy and diseased conditions. The objective is to build a robust, efficient, and scalable solution to assist farmers and agricultural experts in detecting diseases accurately and early.

### Relevance

This project is highly relevant for several reasons, particularly within the domains of agriculture, technology, and machine learning. Here are some key points highlighting its significance:

#### Agricultural Importance
- **Crop Yield**: Early detection and treatment of diseases can significantly improve yields of vegetables. Timely and accurate classification of diseases enables better disease management and prevention measures.

#### Technological Advancement in Agriculture (Smart Farming)
- **Automation**: Automating disease detection can reduce the dependency on human experts.
- **Cost Efficiency**: Machine learning models offer a cost-effective solution compared to traditional lab tests or extensive manual inspections.

#### Deep Learning (CNN) for Image Classification
- **High Accuracy**: By image classification tasks, making them suitable for identifying visual patterns in infected leaves.

#### Environmental and Economic Impact
- **Pesticide Reduction**: Accurate disease identification helps minimize the indiscriminate use of pesticides. Reducing crop losses due to diseases contributes to sustainable farming practices.

#### Potential Use Cases
- **Mobile Applications**: Apps that allow farmers to capture leaf images and get instant disease classifications.
