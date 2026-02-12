import psycopg2
from config import DATABASE_URL

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def find_faq(user_question):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT answer FROM faq
        WHERE question ILIKE %s
        LIMIT 1
    """

    cursor.execute(query, (f"%{user_question}%",))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    return None
