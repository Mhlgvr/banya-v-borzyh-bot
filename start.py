from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

if __name__ == "__main__":
    dp.include_router(router)
    asyncio.run(dp.start_polling(bot))