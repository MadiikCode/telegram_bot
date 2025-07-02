import asyncio
from aiogram import Bot, Dispatcher
from aiobot_project.config import BOT_TOKEN
from aiobot_project.handlers.main_handlers import router  # импортируем Router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
