from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Меню'),
                KeyboardButton(text='О нас')
            ],
            [
                KeyboardButton(text='Контакты'),
                KeyboardButton(text='Адрес')
            ]


    ],
    resize_keyboard=True,
    input_field_placeholder='че надо'

)
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='с говядиной'),
                KeyboardButton(text='с сыром')
            ],
            [
                KeyboardButton(text='с творогом'),
                KeyboardButton(text='с свининой')
            ],
            [
                KeyboardButton(text='с курятиной'),
                KeyboardButton(text='с картошкой')

            ]


    ],
    resize_keyboard=True,
    input_field_placeholder='лол'

)
contacts_kb = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='доставка'),
                KeyboardButton(text='владелец')
            ],
            [
                KeyboardButton(text='повар'),
                KeyboardButton(text='админ')
            ]
    ],
    resize_keyboard=True,
    input_field_placeholder='позвони мне'

)
