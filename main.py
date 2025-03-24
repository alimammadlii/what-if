from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List, Dict
import json

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# System prompt for historical expertise
SYSTEM_PROMPT = """You are an expert historical analyst. You must ONLY answer questions about historical 'what-if' scenarios.
If the user asks anything not related to historical events (like personal questions, future scenarios, or fictional situations), 
politely explain that you can only analyze historical scenarios and ask them to rephrase their question as a historical what-if.
Example valid questions: 'What if Rome never fell?', 'What if the Industrial Revolution started earlier?'
Example invalid questions: 'What if I won the lottery?', 'What if aliens visit tomorrow?'"""

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="templates/static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Store messages in memory (in a real app, you'd use a database)
messages: List[Dict] = []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "messages": messages}
    )

@app.post("/chat")
async def chat(question: str = Form(...)):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/alimammadlii/what-if",
                "X-Title": "What-If AI",
            },
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        
        # Add messages to history
        messages.append({
            "role": "user",
            "content": question
        })
        messages.append({
            "role": "assistant",
            "content": completion.choices[0].message.content
        })
        
        return {"status": "success", "messages": messages}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)