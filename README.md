# 🚀 AI Text Summarizer

A full-stack text summarization app powered by Groq LLM, FastAPI, and vanilla JavaScript.

## ✨ Features

- Lightning-fast text summarization using Groq's Llama 3.3 70B model
- Two summary styles: Concise paragraphs or bullet points
- Clean, modern UI with real-time character count
- Compression rate display
- Copy to clipboard functionality
- Fully responsive design

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- FastAPI (REST API framework)
- Groq API (LLM inference)
- Uvicorn (ASGI server)

**Frontend:**
- HTML5
- CSS3 (with gradients and animations)
- Vanilla JavaScript (no frameworks!)

## 📦 Installation

### 1. Clone or download the project files

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your Groq API key

Get your free API key from: https://console.groq.com/keys

Then set it as an environment variable:

**Linux/Mac:**
```bash
export GROQ_API_KEY="your-api-key-here"
```

**Windows (CMD):**
```cmd
set GROQ_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your-api-key-here"
```

Or create a `.env` file in the project root:
```
GROQ_API_KEY=your-api-key-here
```

## 🚀 Running the Application

### 1. Start the Backend (FastAPI)

```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### 2. Start the Frontend

Simply open `index.html` in your browser, or use a local server:

**Python:**
```bash
python -m http.server 3000
```

**Node.js (if you have it):**
```bash
npx serve
```

Then open `http://localhost:3000` in your browser.

## 📝 Usage

1. Paste or type text into the input area (minimum 50 characters)
2. Choose your summary style (Concise or Bullet Points)
3. Click "Summarize" and watch the magic happen! ✨
4. Copy the summary to your clipboard with one click

**Keyboard Shortcut:** `Ctrl + Enter` to summarize

## 🔧 API Endpoints

### `GET /`
Health check and API info

### `GET /health`
Check API and model status

### `POST /summarize`
Summarize text

**Request Body:**
```json
{
  "text": "Your long text here...",
  "style": "concise"  // or "bullets"
}
```

**Response:**
```json
{
  "summary": "Summarized text...",
  "original_length": 500,
  "summary_length": 120
}
```

## 🎨 Customization

**Change the LLM model:**
Edit `llm_summarizer.py` and change the `self.model` value to any Groq-supported model.

**Adjust summary length:**
Modify `max_tokens` in the `summarize_text()` function.

**Change colors:**
Edit the CSS gradients and colors in `style.css`.

## 🐛 Troubleshooting

**"Failed to connect to the API"**
- Make sure the FastAPI backend is running (`python main.py`)
- Check that it's running on port 8000
- Verify CORS is enabled in `main.py`

**"Error calling Groq API"**
- Verify your API key is set correctly
- Check your internet connection
- Ensure you have API credits in your Groq account

**Frontend not loading styles**
- Make sure all files are in the same directory
- Check browser console for errors

## 📄 License

Free to use and modify! Built with ❤️

## 🙌 Credits

- Groq for blazing-fast LLM inference
- FastAPI for the awesome Python framework
- You for building cool stuff!

---

**Happy Summarizing! 🎉**
