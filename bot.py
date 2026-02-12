import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import BOT_TOKEN
from database import find_faq
from ai_service import ask_ai

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я AI-ассистент ALT University. Задай вопрос.")

@dp.message()
async def handle_message(message: Message):
    question = message.text

    faq_answer = find_faq(question)

    if faq_answer:
        await message.answer(faq_answer)
    else:
        ai_response = ask_ai(question)
        await message.answer(ai_response)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
