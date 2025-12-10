// app/static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('file-input');
    const dropZone = document.getElementById('drop-zone');
    const previewImg = document.getElementById('preview-img');
    const uploadPrompt = document.getElementById('upload-prompt');
    const generateBtn = document.getElementById('generate-btn');
    const resultContainer = document.getElementById('result-container');
    const resultPlaceholder = document.getElementById('result-placeholder');
    const loader = document.getElementById('loader');
    const resultImg = document.getElementById('result-img');
    const errorMsg = document.getElementById('error-msg');
    const downloadLink = document.getElementById('download-link');
    
    // State variables
    let selectedStyle = 'watercolor';
    let currentFile = null; // Store the file object here

    // Style Selection
    document.querySelectorAll('.style-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.style-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            selectedStyle = e.target.dataset.value;
        });
    });

    // File Handling
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('border-indigo-400', 'bg-indigo-50');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('border-indigo-400', 'bg-indigo-50');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('border-indigo-400', 'bg-indigo-50');
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert("Please upload an image file.");
            return;
        }

        // Store the file in our state variable
        currentFile = file;

        const reader = new FileReader();
        reader.onload = (e) => {
            previewImg.src = e.target.result;
            previewImg.classList.remove('hidden');
            uploadPrompt.classList.add('hidden');
            generateBtn.disabled = false;
        };
        reader.readAsDataURL(file);
    }

    // Generation Logic
    generateBtn.addEventListener('click', async () => {
        if (!currentFile) return;

        // UI State: Loading
        generateBtn.disabled = true;
        resultPlaceholder.classList.add('hidden');
        resultContainer.classList.add('hidden');
        errorMsg.classList.add('hidden');
        loader.classList.remove('hidden');

        const formData = new FormData();
        // Use the stored currentFile, which handles both drop and click-upload
        formData.append('file', currentFile);
        formData.append('style', selectedStyle);

        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok || data.error) {
                throw new Error(data.error || 'Generation failed');
            }

            // Success
            resultImg.src = data.image_url;
            downloadLink.href = data.image_url;
            resultContainer.classList.remove('hidden');

        } catch (error) {
            console.error(error);
            document.getElementById('error-text').textContent = error.message;
            errorMsg.classList.remove('hidden');
        } finally {
            loader.classList.add('hidden');
            generateBtn.disabled = false;
        }
    });
});