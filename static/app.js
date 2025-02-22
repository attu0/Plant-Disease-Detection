const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');
const fileInfo = document.getElementById('fileInfo');
const message = document.getElementById('message');
const loading = document.getElementById('loading');
const resultContainer = document.getElementById('resultContainer');
const predictionResult = document.getElementById('predictionResult');

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
});

function handleFiles(files) {
    if (files.length > 0) {
        const file = files[0];
        
        if (!file.type.startsWith('image/')) {
            showMessage('Please upload an image file', false);
            return;
        }

        fileInfo.textContent = `File: ${file.name} (${formatFileSize(file.size)})`;

        // Preview the image
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);

        // Upload and process the file
        uploadFile(file);
    }
}

function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    loading.style.display = 'block';
    resultContainer.style.display = 'none';
    showMessage('', true);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loading.style.display = 'none';
        
        if (data.error) {
            showMessage(data.error, false);
        } else {
            showMessage('Image processed successfully!', true);
            displayResults(data.result);
        }
    })
    .catch(error => {
        loading.style.display = 'none';
        console.error('Error:', error);
        showMessage('Error processing image: ' + error, false);
    });
}

function displayResults(result) {
    resultContainer.style.display = 'block';
    
    const predictions = result.prediction[0];
    let resultHtml = '<div class="prediction-details">';
    
    if (Array.isArray(predictions)) {
        predictions.forEach((pred, index) => {
            resultHtml += `<p>Class ${index + 1}: ${(pred * 100).toFixed(2)}%</p>`;
        });
    } else {
        resultHtml += `<p>Prediction: ${predictions}</p>`;
    }
    
    resultHtml += '</div>';
    predictionResult.innerHTML = resultHtml;
}

function showMessage(text, isSuccess) {
    message.textContent = text;
    message.style.display = text ? 'block' : 'none';
    message.className = isSuccess ? 'success' : 'error';
}

function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}