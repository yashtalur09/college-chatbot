
# import os
# import json
# import streamlit as st
# from groq import Groq
# from io import StringIO
# from fpdf import FPDF

# # Streamlit page configuration
# st.set_page_config(
#     page_title="College Info Chatbot",
#     page_icon="🎓",
#     layout="centered"
# )

# # Define the working directory and load the data
# working_dir = os.path.dirname(os.path.abspath(__file__))
# config_data = json.load(open(f"{working_dir}/config.json"))

# # Retrieve and set API key from config
# GROQ_API_KEY = config_data.get("GROQ_API_KEY")

# # Validate the API key if it exists
# if not GROQ_API_KEY:
#     st.error("API key is missing in the config.json file.")
#     st.stop()

# # Save the API key to the environment variable
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# # Initialize the Groq client with API key
# try:
#     client = Groq(api_key=os.environ["GROQ_API_KEY"])
# except Exception as e:
#     st.error(f"Failed to initialize Groq client: {e}")
#     st.stop()

# # Initialize the chat history in Streamlit session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Streamlit page title
# st.title("🎓 College Info Chatbot")

# # Function to validate user prompt
# def is_valid_prompt(prompt):
#     keywords = ["college", "placement", "fee", "ranking", "infrastructure", "course", "admission"]
#     return any(keyword in prompt.lower() for keyword in keywords)

# # Function to create PDF
# def create_pdf(content):
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_auto_page_break(auto=True, margin=15)
#         pdf.set_font("Arial", size=12)
#         # Encode content to handle special characters
#         encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
#         pdf.multi_cell(0, 10, encoded_content)
#         return pdf.output(dest='S').encode('latin-1')
#     except Exception as e:
#         st.error(f"Error creating PDF: {e}")
#         return None

# # Display the chat history
# for i, message in enumerate(st.session_state.chat_history):
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
#         # Add download buttons for assistant responses
#         if message["role"] == "assistant":
#             response_text = message["content"]
#             col1, col2 = st.columns(2)
            
#             # Text download in column 1
#             with col1:
#                 download_filename = f"response_{i+1}.txt"
#                 st.download_button(
#                     label="Download as Text",
#                     data=response_text,
#                     file_name=download_filename,
#                     mime="text/plain"
#                 )
            
#             # PDF download in column 2
#             with col2:
#                 pdf_bytes = create_pdf(response_text)
#                 if pdf_bytes:
#                     st.download_button(
#                         label="Download as PDF",
#                         data=pdf_bytes,
#                         file_name=f"response_{i+1}.pdf",
#                         mime="application/pdf"
#                     )

# # Input field for user message
# user_prompt = st.chat_input("Ask about colleges in India...")

# if user_prompt:
#     if is_valid_prompt(user_prompt):
#         st.chat_message("user").markdown(user_prompt)
#         st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#         # Send user's message to LLM and get a response
#         messages = [
#             {"role": "system", "content": "You are a chatbot that provides accurate and concise information about colleges in India, including placements, fees, infrastructure, rankings, and related topics. You must not respond to queries unrelated to these topics."},
#             *st.session_state.chat_history
#         ]

#         try:
#             response = client.chat.completions.create(
#                 model="llama3-8b-8192",
#                 messages=messages
#             )

#             assistant_response = response.choices[0].message.content
#             st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

#             # Display the LLM response
#             with st.chat_message("assistant"):
#                 st.markdown(assistant_response)

#                 # Add download buttons in columns
#                 col1, col2 = st.columns(2)
                
#                 # Text download in column 1
#                 with col1:
#                     st.download_button(
#                         label="Download as Text",
#                         data=assistant_response,
#                         file_name="response_latest.txt",
#                         mime="text/plain"
#                     )
                
#                 # PDF download in column 2
#                 with col2:
#                     pdf_bytes = create_pdf(assistant_response)
#                     if pdf_bytes:
#                         st.download_button(
#                             label="Download as PDF",
#                             data=pdf_bytes,
#                             file_name="response_latest.pdf",
#                             mime="application/pdf"
#                         )

#         except Exception as e:
#             st.error(f"Error while fetching the response from GROQ: {e}")
#     else:
#         # Inform the user about invalid queries
#         st.error("Please ask questions related to colleges, such as placements, fees, infrastructure, or rankings.")



# import os
# import json
# import streamlit as st
# from groq import Groq
# from io import StringIO
# from fpdf import FPDF

# # Streamlit page configuration MUST come first
# st.set_page_config(
#     page_title="College Info Chatbot",
#     page_icon="🎓",
#     layout="centered"
# )

# # Custom CSS for animations and styling (moved after set_page_config)
# # Custom CSS for improved background and font styles
# # Custom CSS for improved background and font styles
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f6d365; /* Fallback for browsers that do not support gradients */
#         background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
#         color: #333333;
#         font-family: 'Arial', sans-serif;
#     }
#     .stApp {
#         background-image: url('https://path_to_your_image.jpg'); /* Update this to a public URL or local path */
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: inset 0 0 100px rgba(255, 255, 255, 0.2);
#     }
#     .stButton>button {
#         background-color: #007BFF;
#         color: white;
#         border-radius: 8px;
#         font-size: 16px;
#         padding: 10px 20px;
#         box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
#     }
#     .stSelectbox {
#         font-size: 16px;
#         border-radius: 5px;
#         padding: 5px;
#     }
#     .tabs-container {
#         background-color: rgba(255, 255, 255, 0.9);
#         padding: 15px;
#         border-radius: 10px;
#     }
#     h1, h2, h3, h4, h5, h6 {
#         text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


# # Define the working directory and load the data
# working_dir = os.path.dirname(os.path.abspath(__file__))
# config_data = json.load(open(f"{working_dir}/config.json"))

# # Retrieve and set API key from config
# GROQ_API_KEY = config_data.get("GROQ_API_KEY")

# # Validate the API key if it exists
# if not GROQ_API_KEY:
#     st.error("🔑 API key is missing in the config.json file.")
#     st.stop()

# # Save the API key to the environment variable
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# # Initialize the Groq client with API key
# try:
#     client = Groq(api_key=os.environ["GROQ_API_KEY"])
# except Exception as e:
#     st.error(f"⚠️ Failed to initialize Groq client: {e}")
#     st.stop()

# # Initialize chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Enhanced page header with animations
# st.markdown("""
#     <div style='text-align: center; padding: 20px;'>
#         <h1 class='stTitle'>🎓 College Info Chatbot</h1>
#         <p style='font-size: 1.2rem; color: #666; margin-top: 10px;'>
#             Your AI guide to colleges in India
#         </p>
#     </div>
# """, unsafe_allow_html=True)

# # Display welcome message for new users
# if not st.session_state.chat_history:
#     st.markdown("""
#         <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 10px; margin: 20px 0;'>
#             <h3 style='color: #1e3a8a;'>👋 Welcome to College Info Chatbot!</h3>
#             <p>Ask me about:</p>
#             <div style='display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 10px;'>
#                 <span style='background: #e5e7eb; padding: 5px 10px; border-radius: 15px;'>📚 Courses</span>
#                 <span style='background: #e5e7eb; padding: 5px 10px; border-radius: 15px;'>💰 Fees</span>
#                 <span style='background: #e5e7eb; padding: 5px 10px; border-radius: 15px;'>🏢 Infrastructure</span>
#                 <span style='background: #e5e7eb; padding: 5px 10px; border-radius: 15px;'>🎯 Placements</span>
#                 <span style='background: #e5e7eb; padding: 5px 10px; border-radius: 15px;'>🏆 Rankings</span>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

# # Function definitions
# def is_valid_prompt(prompt):
#     keywords = ["college", "placement", "fee", "ranking", "infrastructure", "course", "admission"]
#     return any(keyword in prompt.lower() for keyword in keywords)

# def create_pdf(content):
#     try:
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_auto_page_break(auto=True, margin=15)
#         pdf.set_font("Arial", size=12)
#         encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
#         pdf.multi_cell(0, 10, encoded_content)
#         return pdf.output(dest='S').encode('latin-1')
#     except Exception as e:
#         st.error(f"Error creating PDF: {e}")
#         return None

# # Display chat history
# for i, message in enumerate(st.session_state.chat_history):
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
#         if message["role"] == "assistant":
#             response_text = message["content"]
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 st.download_button(
#                     label="📄 Download as Text",
#                     data=response_text,
#                     file_name=f"response_{i+1}.txt",
#                     mime="text/plain"
#                 )
            
#             with col2:
#                 pdf_bytes = create_pdf(response_text)
#                 if pdf_bytes:
#                     st.download_button(
#                         label="📑 Download as PDF",
#                         data=pdf_bytes,
#                         file_name=f"response_{i+1}.pdf",
#                         mime="application/pdf"
#                     )

# # Chat input and processing
# user_prompt = st.chat_input("💭 Ask about colleges in India...")

# if user_prompt:
#     if is_valid_prompt(user_prompt):
#         st.chat_message("user").markdown(user_prompt)
#         st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#         with st.spinner('🤔 Thinking...'):
#             messages = [
#                 {"role": "system", "content": "You are a chatbot that provides accurate and concise information about colleges in India, including placements, fees, infrastructure, rankings, and related topics. You must not respond to queries unrelated to these topics."},
#                 *st.session_state.chat_history
#             ]

#             try:
#                 response = client.chat.completions.create(
#                     model="llama3-8b-8192",
#                     messages=messages
#                 )

#                 assistant_response = response.choices[0].message.content
#                 st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

#                 with st.chat_message("assistant"):
#                     st.markdown(assistant_response)

#                     col1, col2 = st.columns(2)
                    
#                     with col1:
#                         st.download_button(
#                             label="📄 Download as Text",
#                             data=assistant_response,
#                             file_name="response_latest.txt",
#                             mime="text/plain"
#                         )
                    
#                     with col2:
#                         pdf_bytes = create_pdf(assistant_response)
#                         if pdf_bytes:
#                             st.download_button(
#                                 label="📑 Download as PDF",
#                                 data=pdf_bytes,
#                                 file_name="response_latest.pdf",
#                                 mime="application/pdf"
#                             )

#             except Exception as e:
#                 st.error(f"⚠️ Error while fetching the response: {e}")
#     else:
#         st.error("❌ Please ask questions related to colleges, such as placements, fees, infrastructure, or rankings.")

import os
import json
import streamlit as st
from groq import Groq
from io import StringIO
from fpdf import FPDF
from streamlit_lottie import st_lottie

# Streamlit page configuration
st.set_page_config(
    page_title="College Info Chatbot",
    page_icon="🎓",
    layout="centered"
)

# Initialize chat history if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load animations
def load_lottie_file(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Animation file not found: {filepath}")
        return None

# Define the working directory and load the data
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")

try:
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
except FileNotFoundError:
    st.error(f"Config file not found: {config_path}")
    st.stop()

# Retrieve and set API key from config
GROQ_API_KEY = config_data.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("🔑 API key is missing in the config.json file.")
    st.stop()

# Save the API key to the environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize the Groq client with API key
try:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
except Exception as e:
    st.error(f"⚠️ Failed to initialize Groq client: {e}")
    st.stop()

# Load welcome animation once
welcome_animation = load_lottie_file("animate.json")

# Enhanced page header with animations
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 class='stTitle'>🎓 College Info Chatbot</h1>
        <p style='font-size: 1.2rem; color: #666; margin-top: 10px;'>
            Your AI guide to colleges in India
        </p>
    </div>
""", unsafe_allow_html=True)

# Display welcome animation and message
if not st.session_state.chat_history and welcome_animation:
    st_lottie(welcome_animation, height=300, key="welcome_anim")
    st.markdown("""
        
    """, unsafe_allow_html=True)

# Function to validate user prompts
def is_valid_prompt(prompt):
    keywords = ["college", "placement", "fee", "ranking", "infrastructure", "course", "admission"]
    return any(keyword in prompt.lower() for keyword in keywords)

# Function to create PDF
def create_pdf(content):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        encoded_content = content.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, encoded_content)
        return pdf.output(dest='S').encode('latin-1')
    except Exception as e:
        st.error(f"Error creating PDF: {e}")
        return None

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        if message["role"] == "assistant":
            response_text = message["content"]
            col1, col2 = st.columns(2)
            
            with col1:
                st.download_button(
                    label="📄 Download as Text",
                    data=response_text,
                    file_name=f"response_{i+1}.txt",
                    mime="text/plain"
                )
            
            with col2:
                pdf_bytes = create_pdf(response_text)
                if pdf_bytes:
                    st.download_button(
                        label="📑 Download as PDF",
                        data=pdf_bytes,
                        file_name=f"response_{i+1}.pdf",
                        mime="application/pdf"
                    )

# Chat input and processing
user_prompt = st.chat_input("💭 Ask about colleges in India...")

if user_prompt:
    if is_valid_prompt(user_prompt):
        st.chat_message("user").markdown(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        with st.spinner('🤔 Thinking...'):
            messages = [
                {"role": "system", "content": "You are a chatbot that provides accurate and concise information about colleges in India, including placements, fees, infrastructure, rankings, and related topics. You must not respond to queries unrelated to these topics."},
                *st.session_state.chat_history
            ]

            try:
                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=messages
                )

                assistant_response = response.choices[0].message.content
                st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

                with st.chat_message("assistant"):
                    st.markdown(assistant_response)

                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.download_button(
                            label="📄 Download as Text",
                            data=assistant_response,
                            file_name="response_latest.txt",
                            mime="text/plain"
                        )
                    
                    with col2:
                        pdf_bytes = create_pdf(assistant_response)
                        if pdf_bytes:
                            st.download_button(
                                label="📑 Download as PDF",
                                data=pdf_bytes,
                                file_name="response_latest.pdf",
                                mime="application/pdf"
                            )

            except Exception as e:
                st.error(f"⚠️ Error while fetching the response: {e}")
    else:
        st.error("❌ Please ask questions related to colleges, such as placements, fees, infrastructure, or rankings.")
