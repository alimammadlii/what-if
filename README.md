# What-If AI

A clean and professional web application that explores alternative histories and possibilities using AI. Built with Streamlit and powered by OpenRouter.ai.

## Features

- Clean and minimalistic UI
- Real-time AI response generation
- Session state management for chat history
- Responsive design
- Secure API key management

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenRouter API key:
   ```
   API_KEY=your_api_key_here
   ```

## Running the Application

To run the application, execute:
```bash
streamlit run ds.py
```

The application will open in your default web browser.

## Usage

1. Enter your "what-if" question in the text area
2. Click the "Generate Response" button
3. View the AI-generated response below
4. Previous responses are retained in the session

## Note

This application uses the OpenRouter.ai API for AI model access. Make sure you have a valid API key and sufficient credits. 