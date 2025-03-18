from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

GROQ_API_KEY = "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"

llm = ChatGroq(api_key=GROQ_API_KEY, temperature=0, model_name="Llama3-8b-8192")

system = "You are a travel agent."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
chain = prompt | llm

response = chain.invoke({"text": "What is the best place to visit in ISLAMABAD?"})
print(response.content)
