import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "6731431063:AAGaxAImJGaO3WDY34X1iUoEE_rsDgTE9Lg"
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Это бот сделаный Стёпай_Няшкой для заказа пельменей и варенников")


@dp.message()
async def echo(message: types.Message):
    # await message.answer("Бот не работает, а я няшка")
    user_text = message.text
    await message.answer(user_text)


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
