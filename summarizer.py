from groq import Groq
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_summary(text):

    prompt = f"""
    Simplify this government policy for citizens.

    Provide:
    1. Short Summary
    2. Key Points
    3. Citizen Impact

    Policy:
    {text[:4000]}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content

    return summary
