import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

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

# Set page config
st.set_page_config(
    page_title="What-If AI",
    page_icon="🤔",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        padding: 10px;
        text-align: center;
        font-size: 0.8em;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title(" What-If...?")
st.markdown("""
    Explore alternative histories and possibilities with AI. 
    Enter your 'what-if' question below and let the AI generate a response.
""")

# Input section
user_input = st.text_area(
    "Enter your what-if question:",
    placeholder="What if...",
    height=100
)

# Generate button
if st.button("Generate Response", type="primary"):
    if user_input:
        with st.spinner("Generating response..."):
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
                            "content": user_input
                        }
                    ]
                )
                
                # Add the new message to chat history
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_input
                })
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": completion.choices[0].message.content
                })
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question first.")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**AI:** {message['content']}")
        st.markdown("---")