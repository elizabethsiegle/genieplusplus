import streamlit as st

# Set the page title and initial layout
st.set_page_config(page_title="Impossibly Difficult Question", layout="centered")

# Display the app header
st.header("Ask Your Impossibly Difficult Question")

# Create a text input box with a label
user_question = st.text_input("What is the impossibly difficult question you want me to answer (within reason)?")

# Create a submit button
if st.button("Submit"):
    if user_question:
        # You can process the question here and display an answer
        st.success("Your question was submitted successfully!")
        st.write("Question:", user_question)
        # Implement logic to handle or respond to the question
    else:
        st.error("Please enter a question before submitting.")
