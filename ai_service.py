from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
Ты официальный AI-ассистент ALT University.

Отвечай только в контексте ALT University.
Не приводи примеры из других стран или организаций.
Если точной информации нет, честно скажи:
"Информация по данному вопросу отсутствует в базе университета."

Не выдумывай данные.
Отвечай кратко и по делу.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content

