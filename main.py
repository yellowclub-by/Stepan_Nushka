import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "6731431063:AAGaxAImJGaO3WDY34X1iUoEE_rsDgTE9Lg"
bot = Bot(token=TOKEN)
dp = Dispatcher()

from handless.user_privat import user_router
dp.include_router(user_router)
async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
