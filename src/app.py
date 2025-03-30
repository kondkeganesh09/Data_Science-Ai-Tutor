import streamlit as st
from src.ai_model import get_gemini_response  # Import the function

st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("🤖 Data Science Tutor")

st.sidebar.header("Instructions")
st.sidebar.write(
    """
    - Ask any question related to Data Science, ML, AI, Python, etc.
    - Click the *Submit* button or press *Enter* to get a response.
    """
)

user_input = st.text_area("Ask a question in Data Science:", "")

if st.button("Submit") and user_input:
    with st.spinner("Thinking... 🤔"):
        response = get_gemini_response(user_input)
    st.success("Response Generated Successfully!")
    st.subheader("AI's Response:")
    st.write(response)

st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit & Google Gemini API")
