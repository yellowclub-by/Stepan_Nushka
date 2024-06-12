from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='адрес 1',callback_data='addresses_1'),
        InlineKeyboardButton(text='адрес 2', callback_data='addresses_2'),
        InlineKeyboardButton(text='адрес 3', callback_data='addresses_3'),
        InlineKeyboardButton(text='адрес 4', callback_data='addresses_4'),
        width=2
    )
    return builder.as_markup()