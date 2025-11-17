from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
st.heander("Reaserch Toll")
model = ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)
user_input = st.text_input("Enter your reaserch topic")


