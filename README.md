#EVS PROJECT

This is an AI-Driven Vegetable Disease Recognition and Management Recommendations model.

# Plant Disease Detection

A web application that uses machine learning to detect diseases in plant leaves. Currently supports potato plant disease detection.

## Features

- Upload images through drag & drop or file selection
- Real-time disease detection
- Confidence score for predictions
- Responsive design
- Support for multiple plant types (coming soon)

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