from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import os
model=ChatOpenAI(
    model="gryphe/mythomax-l2-13b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)
#chat history not getting saved in this example
"""while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(user_input)
    print("Ai: ",result.content)
"""

chat_history=[]
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("Ai: ",result.content)
    print("Chat History: ",chat_history)
