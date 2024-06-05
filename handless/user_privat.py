from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from keyboards import reply


user_router = Router()



@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Это бот сделаный Стёпай_Няшкой для заказа пельменей и варенников",
                         reply_markup=reply.start_kb)



@user_router.message(F.text.lower() == 'меню')
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Вот наше меню пельменей и варенников:", reply_markup=reply.menu_kb)



@user_router.message(F.text.lower() == 'о нас')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("О нас: ")



@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("контакты:", reply_markup=reply.contacts_kb)



@user_router.message(F.text.lower() == 'адрес')
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("Где можно забрать пельмени:")



@user_router.message(F.text.lower() == 'назад')
async def back_home(message: types.Message):
    await message.answer("главное меню", reply_markup=reply.start_kb)

# @user_router.message(F.text)
# @user_router.message(F.photo)
# @user_router.message(F.text.lower() == 'доставка')
# @user_router.message(F.text.lower().contains('достав'))
# @user_router.message(F.text.lower().startswith('как'))
# @user_router.message(F.text.lower().endswith('?'))
# @user_router.message(F.text.lower().startswith('как'), F.text.endswith('?'))
@user_router.message((F.text.lower().contains('стоимост')) | (F.text.lower().contains('цен')))
async def echo(message: types.Message):
    await message.answer("Сработал магический фильтр")
    # user_text = message.text
    # await message.answer(user_text)
