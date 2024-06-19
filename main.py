import asyncio
from aiogram import Bot, Dispatcher



TOKEN = "6731431063:AAGaxAImJGaO3WDY34X1iUoEE_rsDgTE9Lg"
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()



from handless.user_privat import user_router
from handless.menu import menu_router
from handless.user_group import group_router

dp.include_router(user_router)
dp.include_router(menu_router)
dp.include_router(group_router)



async def main():
    print("Бот запущен")
    await dp.start_polling(bot)



asyncio.run(main())
