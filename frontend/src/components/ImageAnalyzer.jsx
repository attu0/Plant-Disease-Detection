import { useState } from 'react'
import axios from 'axios'
import Button from './Button'
import './ImageAnalyzer.css'

function ImageAnalyzer() {
  const [selectedImage, setSelectedImage] = useState(null)
  const [result, setResult] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [file, setFile] = useState(null)

  const handleImageSelect = (event) => {
    const selectedFile = event.target.files[0]
    if (selectedFile) {
      setFile(selectedFile)
      setSelectedImage(URL.createObjectURL(selectedFile))
      setResult(null)
      setError(null)
    }
  }

  const handleSubmit = async () => {
    if (!file) {
      setError('Please select an image first')
      return
    }
    await analyzeImage(file)
  }

  const handleNext = () => {
    setSelectedImage(null)
    setResult(null)
    setError(null)
    setFile(null)
  }

  const analyzeImage = async (file) => {
    setIsLoading(true)
    setError(null)
    
    try {
      const formData = new FormData()
      formData.append('file', file)

      console.log('Sending request to backend...')
      const response = await axios.post('http://localhost:8000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      console.log('Response from backend:', response.data)

      if (response.data) {
        setResult({
          plantType: response.data.plant_type,
          disease: response.data.class,
          confidence: (response.data.confidence * 100).toFixed(2)
        })
      } else {
        setError('Invalid response from server')
      }
    } catch (err) {
      console.error('Error details:', err)
      setError(err.response?.data?.detail || 'Error analyzing image. Please try again.')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="main-content">
      <div className="upload-section">
        <div className="upload-box">
          {selectedImage ? (
            <img src={selectedImage} alt="Selected plant" className="preview-image" />
          ) : (
            <div className="upload-placeholder">
              <p>Drag and drop an image here or</p>
              <label className="upload-button">
                Choose File
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleImageSelect}
                  style={{ display: 'none' }}
                />
              </label>
            </div>
          )}
        </div>
        
        <div className="button-group">
          {selectedImage && !result && (
            <Button 
              text="Submit Image" 
              onClick={handleSubmit} 
              disabled={isLoading}
              type="primary"
            />
          )}
          {result && (
            <Button 
              text="Next Image" 
              onClick={handleNext}
              type="secondary"
            />
          )}
        </div>
      </div>

      {selectedImage && (
        <div className="result-section">
          <h2>Analysis Results</h2>
          {isLoading ? (
            <div className="loading">
              <div className="spinner"></div>
              <p>Analyzing image...</p>
            </div>
          ) : error ? (
            <div className="error">
              <p>{error}</p>
            </div>
          ) : result ? (
            <div className="result-content">
              <p className="plant-type">{result.plantType} Plant</p>
              <p className="disease-name">{result.disease}</p>
              <p className="confidence">Confidence: {result.confidence}%</p>
            </div>
          ) : (
            <p>Click "Submit Image" to analyze</p>
          )}
        </div>
      )}
    </main>
  )
}

export default ImageAnalyzer 