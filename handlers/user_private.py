from filters.chat_types import ChatTypeFilter
from aiogram import types, Router,F
from aiogram.filters import CommandStart,Command,or_f
from kdds import reply
from aiogram.utils.formatting import as_list, as_marked_list, Bold, as_marked_section

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))



@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text='Привет я виртуальный помошник',reply_markup=reply.start_kb3.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Че кого?"
    ))

@user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню:',reply_markup=reply.del_kbb,)

@user_private_router.message(F.text.lower() == "о нас")
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('О нас: ')

@user_private_router.message(F.text.lower() == 'варианты оплаты:')
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold("варианты оплаты:"),
            'Картой в боте',
            'При получении карта/кэш',
            'В заведении',
            marker='✅ '
    )
    await message.answer(text.as_html())

@user_private_router.message(F.text.lower() == 'варианты доставки')
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold('Варианты доставки/заказа:'),
            'Курьер',
            'Самовывоз',
            'Покушаю у вас',
            marker='✅ '
        ),
        as_marked_section(
            Bold('Нельзя'),
            'Почта',
            'Голуби',
            marker='❌ '
        ),
        sep = f'\n{"-" * 30}\n'
    )
    await message.answer(text.as_html())




# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f'номер получен')
#     await message.answer(message.contact.first_name)
#
# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f'локация получена')
#     await message.answer(str(message.location))

# @user_private_router.message((F.text.lower().contains('p')) | (F.text.lower().strip() == 'pidr'))
# async def wtf_cmd(message: types.Message):
#     await message.answer('Магия')
