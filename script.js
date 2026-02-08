// Configuration
const API_URL = 'http://localhost:8000';

// DOM elements
const inputText = document.getElementById('inputText');
const charCount = document.getElementById('charCount');
const summaryStyle = document.getElementById('summaryStyle');
const summarizeBtn = document.getElementById('summarizeBtn');
const btnText = summarizeBtn.querySelector('.btn-text');
const loader = summarizeBtn.querySelector('.loader');
const outputSection = document.getElementById('outputSection');
const summaryOutput = document.getElementById('summaryOutput');
const compressionRate = document.getElementById('compressionRate');
const copyBtn = document.getElementById('copyBtn');
const errorMessage = document.getElementById('errorMessage');

// Update character count
inputText.addEventListener('input', () => {
    const length = inputText.value.length;
    charCount.textContent = `${length} characters`;
    
    // Hide error when user starts typing
    if (errorMessage.style.display !== 'none') {
        errorMessage.style.display = 'none';
    }
});

// Summarize button click
summarizeBtn.addEventListener('click', async () => {
    const text = inputText.value.trim();
    
    // Validation
    if (!text) {
        showError('Please enter some text to summarize');
        return;
    }
    
    if (text.length < 50) {
        showError('Text must be at least 50 characters long');
        return;
    }
    
    // Show loading state
    summarizeBtn.disabled = true;
    btnText.style.display = 'none';
    loader.style.display = 'block';
    outputSection.style.display = 'none';
    errorMessage.style.display = 'none';
    
    try {
        // Call API
        const response = await fetch(`${API_URL}/summarize`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                style: summaryStyle.value
            })
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to summarize text');
        }
        
        const data = await response.json();
        
        // Display results
        displaySummary(data);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'Failed to connect to the API. Make sure the backend is running!');
    } finally {
        // Reset button state
        summarizeBtn.disabled = false;
        btnText.style.display = 'inline';
        loader.style.display = 'none';
    }
});

// Display summary
function displaySummary(data) {
    summaryOutput.textContent = data.summary;
    
    // Calculate compression rate
    const reduction = ((1 - data.summary_length / data.original_length) * 100).toFixed(1);
    compressionRate.textContent = `${reduction}% shorter`;
    
    // Show output section with animation
    outputSection.style.display = 'block';
    outputSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Copy summary to clipboard
copyBtn.addEventListener('click', async () => {
    try {
        await navigator.clipboard.writeText(summaryOutput.textContent);
        
        // Visual feedback
        const originalText = copyBtn.textContent;
        copyBtn.textContent = '✅ Copied!';
        copyBtn.style.background = '#28a745';
        copyBtn.style.color = 'white';
        
        setTimeout(() => {
            copyBtn.textContent = originalText;
            copyBtn.style.background = '';
            copyBtn.style.color = '';
        }, 2000);
        
    } catch (error) {
        showError('Failed to copy to clipboard');
    }
});

// Allow Enter+Ctrl to summarize
inputText.addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.key === 'Enter') {
        summarizeBtn.click();
    }
});

// Check API health on load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (response.ok) {
            console.log('✅ Backend is running!');
        }
    } catch (error) {
        console.warn('⚠️ Backend not detected. Make sure to start the FastAPI server!');
    }
});
