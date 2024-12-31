import os
import json
import streamlit as st
from groq import Groq
from io import BytesIO
from fpdf import FPDF

# Streamlit page configuration
st.set_page_config(
    page_title="EV & Charging Stations Info Chatbot",
    page_icon="⚡",
    layout="centered"
)

# Define the working directory and load the data
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

# Retrieve and set API key from config
GROQ_API_KEY = config_data.get("GROQ_API_KEY")

# Validate the API key if it exists
if not GROQ_API_KEY:
    st.error("API key is missing in the config.json file.")
    st.stop()

# Save the API key to the environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the Groq client with API key
try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    st.stop()

# Initialize the chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit page title
st.title("⚡ EV & Charging Stations Info Chatbot")

# Function to validate user prompt
def is_valid_prompt(prompt):
    keywords = ["ev", "vehicle", "charging station", "port", "fast charging", "range", "battery"]
    return any(keyword in prompt.lower() for keyword in keywords)

# Function to create PDF and return bytes
def create_pdf(content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        # Encode content to handle special characters
        encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, encoded_content)
        
        # Return PDF as bytes
        return pdf.output(dest='S').encode('latin-1')
    except Exception as e:
        st.error(f"Error creating PDF: {e}")
        return None

# Display the chat history
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user message
user_prompt = st.chat_input("Ask about EVs and Charging Stations...")

if user_prompt:
    if is_valid_prompt(user_prompt):
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        
        # Send user's message to LLM and get a response
        messages = [
            {"role": "system", "content": "You are a chatbot that provides accurate and concise information about electric vehicles (EVs), their compatibility with charging stations, fast charging support, range, battery life, and related topics."},
            *st.session_state.chat_history
        ]
        
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=messages
            )
            
            assistant_response = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
            
            # Display the LLM response
            with st.chat_message("assistant"):
                st.markdown(assistant_response)
            
            # Create PDF and offer download
            pdf_bytes = create_pdf(assistant_response)
            if pdf_bytes:
                st.download_button(
                    label="Download Response as PDF",
                    data=pdf_bytes,
                    file_name="response_latest.pdf",
                    mime="application/pdf"
                )
            
        except Exception as e:
            st.error(f"Error while fetching the response from GROQ: {e}")
    else:
        # Inform the user about invalid queries
        st.error("Please ask questions related to electric vehicles and charging stations, such as compatibility, fast charging, range, or battery life.")