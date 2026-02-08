import os
from groq import Groq

class LLMSummarizer:
    def __init__(self, api_key: str):
        """Initialize the Groq client with API key"""
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"  # Fast and accurate model
    
    def summarize_text(self, text: str, style: str = "concise") -> str:
        """
        Summarize the given text using Groq LLM
        
        Args:
            text: The text to summarize
            style: Summary style - 'concise' or 'bullets'
        
        Returns:
            Summarized text
        """
        if style == "bullets":
            prompt = f"Summarize the following text as bullet points:\n\n{text}"
        else:
            prompt = f"Provide a concise summary of the following text:\n\n{text}"
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.3,  # Lower for more focused summaries
                max_tokens=500,
            )
            
            return chat_completion.choices[0].message.content
        
        except Exception as e:
            raise Exception(f"Error calling Groq API: {str(e)}")


# Test function
if __name__ == "__main__":
    # For testing - replace with your actual API key
    api_key = os.getenv("GROQ_API_KEY", "your-api-key-here")
    summarizer = LLMSummarizer(api_key)
    
    test_text = """
    Artificial intelligence has made remarkable progress in recent years. 
    Large language models can now understand and generate human-like text, 
    enabling applications from chatbots to code generation. These models are 
    trained on vast amounts of data and use transformer architectures to 
    process information efficiently.
    """
    
    summary = summarizer.summarize_text(test_text)
    print("Summary:", summary)
