import ImageAnalyzer from './components/ImageAnalyzer'
import './App.css'

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Plant Disease Detection</h1>
        <p>Upload an image of a plant to detect diseases</p>
      </header>
      <ImageAnalyzer />
    </div>
  )
}

export default App
