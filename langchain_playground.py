from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.environ["OPENAI_API_KEY"],
)

result = chat_model.invoke("Hi!")
print(result.content)