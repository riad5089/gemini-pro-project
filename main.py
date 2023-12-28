from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get respose
model =genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    respose=model.generate_content(question)
    return respose.text

# initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input=st.text_input("Input:",key="input")
submit =st.button("Ask the question")

#when submit is clicked
if submit:
    response=get_gemini_response(input)
    st.write(response)









