from aiogram import types, Router, F
group_router = Router()

ban_words = ["шашлык", "кавказы", "шаурма"]



@group_router.message(F.text)
async def cleaner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in ban_words:
            await message.answer(f"{message.from_user.first_name} Щас забаню")
            await message.delete()
