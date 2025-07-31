import streamlit as st

# Simple rule-based mock response logic
def get_mock_response(user_input):
    user_input = user_input.lower().strip()

    # Sample keyword-based responses
    if "capital of france" in user_input:
        return "The capital of France is Paris."
    elif "capital of india" in user_input:
        return "The capital of India is New Delhi."
    elif "owl ai" in user_input:
        return "Owl AI is a mock assistant built using Streamlit. You can train me more!"
    elif "python" in user_input:
        return "Python is a powerful programming language used for AI, web development, and automation."
    elif "machine learning" in user_input:
        return "Machine learning is a method where computers learn from data without being explicitly programmed."
    elif "hi" in user_input or "hello" in user_input:
        return "Hello there! I'm Owl AI. How can I help you today?"
    elif "your name" in user_input:
        return "I'm Owl AI, your local assistant."
    elif "who created you" in user_input:
        return "I was created by a developer using Python and Streamlit!"
    elif "help" in user_input:
        return "Sure! Ask me about Python, AI, or general knowledge."
    elif user_input.endswith("?"):
        return "That's a good question! I may not know the answer yet, but I’m learning."
    else:
        return "Sorry, I don't have an answer for that yet. Try asking something else!"

# Streamlit UI
st.set_page_config(page_title="🦉 Owl AI (Mock)", layout="centered")

st.title("🦉 Owl AI - Mock Assistant")
st.write("Ask me anything — offline version with basic intelligence.")

# Input
user_input = st.text_input("Your Question", placeholder="e.g., What is the capital of France?")

if st.button("Ask Owl AI"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Owl AI is thinking..."):
            response = get_mock_response(user_input)
            st.success("Owl AI's Response:")
            st.write(response)
