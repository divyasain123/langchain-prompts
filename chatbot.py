from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
model=ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(user_input)
    print("Ai: ",result.content)
