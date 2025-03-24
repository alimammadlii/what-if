# What-If AI

A modern web application that explores alternative histories and possibilities using AI. Built with FastAPI and powered by OpenRouter.ai.

## Features

- Clean and modern chat interface
- Real-time AI response generation
- Historical scenario analysis

## Setup

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your OpenRouter API key:
   ```
   API_KEY=your_api_key_here
   ```

## Running the Application

To run the application, execute:
```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## Usage

1. Open your web browser and navigate to `http://localhost:8000`
2. Enter your "what-if" question in the text area
3. Press Enter or click the Send button to generate a response
4. View the AI-generated response in the chat interface

## Project Structure

```
what-if/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
└── templates/
    └── index.html      # HTML template
```

## Note

This application uses the OpenRouter.ai API for AI model access. Make sure you have a valid API key and sufficient credits. 