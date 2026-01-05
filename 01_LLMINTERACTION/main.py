from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt = "total 9 employee three of ask for leave how much percentage employee left"

results = model.invoke(prompt)

print("result",results.content)