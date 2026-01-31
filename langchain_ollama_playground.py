from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2", base_url="http://127.0.0.1:11434")
resp = llm.invoke("Hi from LangChain + Ollama!")
print(resp.content)