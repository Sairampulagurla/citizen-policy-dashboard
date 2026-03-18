import os
from groq import Groq
from retriever import find_relevant_chunk

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_policy_question(policy_text, question):

   relevant_text = find_relevant_chunk(policy_text, question)

   prompt = f"""
You are a helpful assistant that explains government policies to citizens.

Default response language is English.

If the user asks the question in another language OR explicitly requests a specific language,
then respond in that language.

Policy Context:
{policy_text}

User Question:
{question}

Answer clearly and simply.
"""

   response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

   return response.choices[0].message.content
