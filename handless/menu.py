from aiogram import types, Router, F
from aiogram.types import FSInputFile


menu_router = Router()


@menu_router.message(F.text.lower() == 'с говядиной🐮')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\говядина.png')
    await message.answer_photo(photo, caption='пельмени с говядиной')



@menu_router.message(F.text.lower() == 'с сыром🧀')
async def sir(message: types.Message):
    photo = FSInputFile('img\menu\сыр.jpg')
    await message.answer_photo(photo, caption='пельмени с сыром')



@menu_router.message(F.text.lower() == 'с творогом🧈')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\творог.jpg')
    await message.answer_photo(photo, caption='пельмени с творогом')


@menu_router.message(F.text.lower() == 'с картошкой🥔')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\картошка.jpg')
    await message.answer_photo(photo, caption='пельмени с картошкой')


@menu_router.message(F.text.lower() == 'с курятиной🐔')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\курица.png')
    await message.answer_photo(photo, caption='пельмени с курятиной')


@menu_router.message(F.text.lower() == 'с свининой🐷')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\свинина.png')
    await message.answer_photo(photo, caption='пельмени с свининой')