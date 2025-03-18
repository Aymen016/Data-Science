import os
from groq import Groq

GROQ_API_KEY="----------------------------------------"

client = Groq(api_key=GROQ_API_KEY)
chat_completion = client.chat.completions.create(
  messages=[
              {"role": "user", "content": "Explain the importance of fast language models"}
  ],
    model="llama-3.3-70b-versatile",
  )

print(chat_completion.choices[0].message.content)
