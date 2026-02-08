from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_summarizer import LLMSummarizer
import os

# Initialize FastAPI app
app = FastAPI(title="Text Summarizer API", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize summarizer (load API key from environment)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY not set in environment variables")

summarizer = LLMSummarizer(GROQ_API_KEY)

# Request model
class SummarizeRequest(BaseModel):
    text: str
    style: str = "concise"  # 'concise' or 'bullets'

# Response model
class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Text Summarizer API is running!",
        "endpoints": {
            "/summarize": "POST - Summarize text",
            "/health": "GET - Health check"
        }
    }

@app.get("/health")
async def health_check():
    """Check if API and LLM are working"""
    return {"status": "healthy", "model": "groq-llama-3.3-70b"}

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    """
    Summarize the provided text using Groq LLM
    
    Args:
        request: SummarizeRequest with text and optional style
    
    Returns:
        SummarizeResponse with summary and length stats
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if len(request.text) < 50:
        raise HTTPException(
            status_code=400, 
            detail="Text is too short to summarize (minimum 50 characters)"
        )
    
    try:
        summary = summarizer.summarize_text(request.text, request.style)
        
        return SummarizeResponse(
            summary=summary,
            original_length=len(request.text),
            summary_length=len(summary)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
