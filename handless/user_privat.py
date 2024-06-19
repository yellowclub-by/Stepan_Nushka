from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F
from keyboards import reply, inline



user_router = Router()



@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("""Добро пожаловать в наш бот-помощник для заказа пельменей и вареников! 
Мы рады предложить вам широкий ассортимент наших вкусных и горячих блюд. Вы можете выбрать различные виды начинки для пельменей,
а также разные соусы и дополнительные ингредиенты для вашего удовольствия.
Ваши заказы будут готовы к доставке в течение короткого времени,
и мы гарантируем высокое качество продукции. Спасибо, что выбираете нас!""",
                         reply_markup=reply.start_kb)



@user_router.message(F.text.lower() == 'меню😋')
@user_router.message(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Вот наше меню пельменей и варенников:", reply_markup=reply.menu_kb)



@user_router.message(F.text.lower() == 'о нас🥵')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("""Мы - это небольшая, но очень дружная команда, которая любит 
свою работу и старается предоставить нашим клиентам только самое лучшее. Наши продукты готовятся из только натуральных 
ингредиентов, а процесс приготовления обеспечивает сохранение всех витаминов и микроэлементов, чтобы вы могли 
наслаждаться вкусом и пользой для здоровья одновременно. 
Мы стремимся к улучшению наших услуг и качества продукции, поэтому ваш отзыв и предложения для нас очень важны. 
Спасибо за выбор нашего заведения!""", reply_markup=inline.links_kb)



@user_router.message(F.text.lower() == 'контакты🤙')
@user_router.message(Command("contacts"))
async def contacts(message: types.Message):
    await message.answer("""Спасибо, что выбрали нашу услугу по заказу пельменей и вареников! 
Если у вас возникли вопросы, предложения или вы хотите оставить отзыв, мы будем рады вам помочь. 
Наши контактные данные:""", reply_markup=reply.contacts_kb)



@user_router.message(F.text.lower() == 'адрес🛖')
@user_router.message(Command("addresses"))
async def addresses(message: types.Message):
    await message.answer("""Спасибо, что выбрали нашу услугу по заказу пельменей и вареников! 
Если вы хотите забрать заказ лично или узнать адреса наших партнеров по доставке, 
мы предоставляем вам следующую информацию:""", reply_markup=inline.addresses_kb())



@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_inline(callback: types.CallbackQuery):
    quopri = callback.data.split('_')[1]
    # await callback.message.delete()
    if quopri == '1':
        await callback.message.answer("первый адрес🏠")
    elif quopri == '2':
        await callback.message.answer("второй адрес🏥")
    elif quopri == '3':
        await  callback.message.answer("третий адрес🏚️")
    elif quopri == '4':
        await callback.message.answer("четвертый адрес🛏️")
    await callback.answer()


@user_router.message(F.text.lower() == 'назад🔙')
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
