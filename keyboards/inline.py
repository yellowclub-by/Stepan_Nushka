from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='ул. Харьковская 3А к4, Минск', callback_data='addresses_1'),
        InlineKeyboardButton(text='ул. Тимирязева 46а, Минск', callback_data='addresses_2'),
        width=1
    )
    return builder.as_markup()


links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ютуб', url='https://www.youtube.com/watch?v=ngd5ugJJYj4'),
            InlineKeyboardButton(text='телеграм', url='tg://resolve?domain=DesantnickSt')
        ]
    ]
)
