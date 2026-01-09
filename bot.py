import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = os.getenv("8531925061:AAFSKazco3DM_3L6HBZMpIjdI6jPVOxvIAQ")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def handler(message: Message):
    await message.reply("Бот запущен и работает 24/7 🚀")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
