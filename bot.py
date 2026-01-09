import os
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # /start
    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer("✅ Бот запущен и работает!")

    # запуск polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
