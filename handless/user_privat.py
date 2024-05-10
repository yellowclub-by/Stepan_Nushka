from aiogram.filters import CommandStart, Command
from aiogram import types, Router


user_router = Router()
@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Это бот сделаный Стёпай_Няшкой для заказа пельменей и варенников")


@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Вот наше меню пельменей и варенников:")


@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("О нас: ")


@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("контакты:")


@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Где можно забрать пельмени:")


@user_router.message()
async def echo(message: types.Message):
    # await message.answer("Бот не роботает, а я няшка")
    user_text = message.text
    await message.answer(user_text)