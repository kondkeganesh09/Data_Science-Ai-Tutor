import streamlit as st
import google.generativeai as genai

# Set API Key securely
GOOGLE_API_KEY = "Enter your Api Key-here"  #API-key
if not GOOGLE_API_KEY:
    st.error("API Key is missing! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to get AI response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model name
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"
