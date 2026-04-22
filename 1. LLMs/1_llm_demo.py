from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(model = 'gpt-3.5-turbo-instruct', temperature=0.7)

result = llm.invoke("What is the capital of United States?")

print(result)