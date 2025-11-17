import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="perplexity/sonar-pro-search",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_new_tokens=100
    
)

response = model.invoke("Who is the current Prime Minister of India as of 2025?")

print(response.content)
