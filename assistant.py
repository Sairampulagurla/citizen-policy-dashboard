import os
from groq import Groq
from retriever import find_relevant_chunk

client = Groq(api_key="*************")

def ask_policy_question(policy_text, question):

   relevant_text = find_relevant_chunk(policy_text, question)

   prompt = f"""
You are a helpful assistant that explains government policies to citizens.
       
The user may ask questions in different languages.
Always respond in the SAME language as the user's question.
       
Policy Context:
{policy_text}
       
User Question:
{question}
       
Answer clearly and simply in the same language as the question.
"""

   response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

   return response.choices[0].message.content
