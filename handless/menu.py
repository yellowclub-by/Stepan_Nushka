from aiogram import types, Router, F
from aiogram.types import FSInputFile


menu_router = Router()


@menu_router.message(F.text.lower() == 'с говядиной🐮')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\говядина.png')
    await message.answer_photo(photo, caption='''<b>Пельмени с говядиной</b>
    
Пельмени с говядиной - небольшие кармашки из тонкого теста.
Начинка состоит из сочного говяжьего фарша, лука и специй.
Пельмени варятся в подсоленной воде до готовности.
Подаются горячими со сметаной, маслом или другими соусами.
    
<b>Цена за пачку:</b> 5р''')



@menu_router.message(F.text.lower() == 'с сыром🧀')
async def sir(message: types.Message):
    photo = FSInputFile('img\menu\сыр.jpg')
    await message.answer_photo(photo, caption='''<b>Вареники с сыром</b>
    
Вареники с сыром - популярное блюдо украинской кухни.
Начинка состоит из мягкого сыра, например, творога или сулугуни.
Тесто для вареников готовится из муки, яиц и воды.
Вареники варятся в кипящей воде и подаются со сметаной или маслом.
    
<b>Цена за пачку:</b> 5р''')



@menu_router.message(F.text.lower() == 'с творогом🧈')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\творог.jpg')
    await message.answer_photo(photo, caption='''<b>Вареники с творогом</b>
    
Вареники с творогом - традиционное украинское блюдо.
Начинка состоит из нежного домашнего творога и сахара.
Тесто для вареников делается из муки, яиц и воды.
Вареники варятся в воде и подаются со сметаной или маслом.
    
<b>Цена за пачку:</b> 5р''')


@menu_router.message(F.text.lower() == 'с картошкой🥔')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\картошка.jpg')
    await message.answer_photo(photo, caption='''<b>Вареники с картошкой</b>
    
Вареники с картошкой - традиционное украинское блюдо.
Начинка состоит из мягкого картофельного пюре, иногда с луком.
Тонкое пресное тесто изготавливается из муки, яиц и воды.
Вареники варятся до готовности и подаются со сметаной или растопленным маслом.
    
<b>Цена за пачку:</b> 5р''')


@menu_router.message(F.text.lower() == 'с курятиной🐔')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\курица.png')
    await message.answer_photo(photo, caption='''<b>Пельмени с курятиной</b>
    
Пельмени с курятиной - аппетитные русские пельмени.
Начинка состоит из нежного куриного фарша и ароматных специй.
Тесто для пельменей приготавливается из муки, яиц и воды.
Пельмени варятся до готовности и подаются со сметаной или маслом.
    
<b>Цена за пачку:</b> 5р''')


@menu_router.message(F.text.lower() == 'с свининой🐷')
async def govydina(message: types.Message):
    photo = FSInputFile('img\menu\свинина.png')
    await message.answer_photo(photo, caption=''''<b>Пельмени с свининой</b>
    
Пельмени с свининой - классическое блюдо русской кухни.
Начинка состоит из сочного фарша из свинины и специй.
Тесто для пельменей изготавливается из муки, яиц и воды.
Пельмени варятся в кипящей воде и подаются со сметаной или маслом.
    
<b>Цена за пачку:</b> 5р''')