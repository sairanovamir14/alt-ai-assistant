from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(question, context=None):
    prompt = f"""
You are an AI assistant for ALT University.
Answer briefly and clearly.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
