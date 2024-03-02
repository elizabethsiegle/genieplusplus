import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Set the page title and initial layout
st.set_page_config(page_title="Impossibly Difficult Question", layout="centered")

# Display the app header
st.header("Ask Your Impossibly Difficult Question")

# Create a text input box with a label
user_question = st.text_input("What is the impossibly difficult question you want me to answer (within reason)?")

api_key = os.environ.get('OPENAI_API_KEY')

# Create a submit button
if st.button("Submit"):
    if user_question:
        # You can process the question here and display an answer
        st.success("Your question was submitted successfully!")
        st.write("Question:", user_question)
        # Implement logic to handle or respond to the question
        GOOGLE_API_KEY= os.environ.get('GOOGLE_API_KEY')
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        # get phone numbers and restaurants to call
        response = model.generate_content(f"You are a helpful assistant. Return 5 relevant places and their phone numbers to help answer the following question: {user_question}")
        st.write("output: ", response.text)

        # parse phone numbers from initial Gemini output
        parse_phone_numbers = model.generate_content(f"If the following contains phone numbers, parse them out from the following and return them separated by commas as an array: {response} ")
        st.write(f'parse_phone_numbers {parse_phone_numbers.text}')

        # Twilio 
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        # loop through phone numbers to print out number to call
        for num in parse_phone_numbers.text:
            print(num)
            # call = client.calls.create( 
            #     twiml = twiml,
            #     to=num, #user input
            #     from_='+18553021845' #twilio num
            # )



    else:
        st.error("Please enter a question before submitting.")

st.write('Made w/ ❤️ by Abel Regalado, Daniel Kim, && Lizzie Siegle in SF 🌁')
st.write("check out this [GitHub repo](https://github.com/elizabethsiegle/genieplusplus)")