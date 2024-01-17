from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from inline_keyboards import plus_minus_bttn, buy
from config import token
from default_keyboards import *

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum, welcome back sir"
    await message.answer(text=text, reply_markup=user_main_menu)


# @dp.message_handler(state=RegisterState.full_name)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(full_name=message.text)
#     text = "Yoshingizni kiriting. Biloldinni ukajoni"
#     await message.answer(text=text)
#     await RegisterState.age.set()
#
#
# @dp.message_handler(state=RegisterState.age)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     text = "Iltimos krutoy tushgan rasmingizni yuboring"
#     await message.answer(text=text)
#     await RegisterState.photo.set()
#
#
# @dp.message_handler(state=RegisterState.photo, content_types=types.ContentType.PHOTO)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(photo=message.photo[-1].file_id)
#     text = "Telefon raqamni jo'nating"
#     await message.answer(text=text, reply_markup=phone_share)
#     await RegisterState.phone_number.set()
#
#
# @dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(phone_number=message.contact.phone_number)
#     text = "Iltimos tanlang"
#     await message.answer(text=text, reply_markup=gender_share)
#     await RegisterState.gender.set()
#
#
# @dp.message_handler(state=RegisterState.gender)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(gender=message.text)
#     text = "Iltimos manzilni jo'nating"
#     await message.answer(text=text, reply_markup=location_share)
#     await RegisterState.location.set()
#
#
# @dp.message_handler(state=RegisterState.location, content_types=types.ContentType.LOCATION)
# async def get_user_data_handler(message: types.Message, state: FSMContext):
#     await state.update_data(longitude=message.location.longitude, latitude=message.location.latitude,
#                             chat_id=message.chat.id)
#     data = await state.get_data()
#     if db_manager.add_user(data):
#         text = "Iltimos raxmat deng sizni ro'yxatdan o'tkazib qo'ydim. "
#     else:
#         text = "Uzr aka/honim menda muommo bor."
#     await message.answer(text=text, reply_markup=user_main_menu)
#     await state.finish()


@dp.message_handler(text="🍟 Mahsulotlar")
async def products_handler(message: types.Message):
    text = "Mahsulotlar albatta sizning so'lagingizni oqizib yuboradi."
    await message.answer(text=text, reply_markup=products_menu)


@dp.message_handler(text="Lavash")
async def products_handler(message: types.Message, state: FSMContext):
    await state.update_data(product="Lavash")
    text = "Tanlang."
    await message.answer(text=text, reply_markup=product_inside_menu)


@dp.message_handler(text="Gamburger")
async def products_handler(message: types.Message, state: FSMContext):
    await state.update_data(product="Gamburger")
    text = "Tanlang."
    await message.answer(text=text, reply_markup=product_inside_menu)


@dp.message_handler(text="Katta")
async def products_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(size="big")
    product_name = data.get("product")
    photo = ""
    text = ""
    if product_name == "Lavash":
        photo = "https://cp.ectn.uz/files//web/lavash_kur.png"
        text = "Katta lavash"
        await state.update_data(price=32000)
    elif product_name == "Gamburger":
        await state.update_data(price=39000)
        photo = "https://cp.ectn.uz/files//web/15.jpg"
        text = "Katta burger"

    await message.answer_photo(photo=photo, caption=text, reply_markup=await plus_minus_bttn(0))


@dp.message_handler(text="Kichik")
async def products_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(size="little")
    product_name = data.get("product")
    photo = ""
    text = ""
    if product_name == "Lavash":
        await state.update_data(price=28000, product="Lavash mini")
        photo = "https://cp.ectn.uz/files//web/lavash_kur.png"
        text = "Kichkina lavash"
    elif product_name == "Gamburger":
        await state.update_data(price=32000, product="Burger mini")
        photo = "https://cp.ectn.uz/files//web/15.jpg"
        text = "Kichkina burger"

    await message.answer_photo(photo=photo, caption=text, reply_markup=await plus_minus_bttn(0))


@dp.callback_query_handler(text="plus")
async def plus_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product = data.get('product')
    price = data.get('price')
    size = data.get('size')
    basket = data.get('basket') if data.get('basket') else dict()
    if product in basket.keys():
        basket[product]["quantity"] += 1
    else:
        basket[product] = {
            "name": product,
            "price": price,
            "size": size,
            "quantity": 1
        }
    await state.update_data(basket=basket)
    text = "Mahsulot bittaga oshirildi. ✅"
    await call.answer(text=text)
    await call.message.edit_reply_markup(reply_markup=await plus_minus_bttn(basket[product]['quantity']))

@dp.callback_query_handler(text="minus")
async def plus_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product = data.get('product')
    price = data.get('price')
    size = data.get('size')
    basket = data.get('basket') if data.get('basket') else dict()
    if basket[product]['quantity'] > 0:
        basket[product]['quantity'] -= 1
        basket[product]['price'] -= price
        text = "Mahsulot bittaga kamaytirildi. ✅"
        await state.update_data(basket=basket)
        await call.answer(text=text)
        await call.message.edit_reply_markup(reply_markup=await plus_minus_bttn(basket[product]['quantity']))
    else:
        text = f"Kechirasiz Ayirish Uchun Minimal 1 Ta Bolishi Kerak!"
        await call.answer(text=text)

@dp.callback_query_handler(text="show_basket")
async def buy_product_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get("basket")
    text = ""
    total = 0
    try:
        for product in basket.values():
            total_price = product['quantity'] * product['price']
            total += total_price
            text += f"{product['name']} | {product['size']} | {product['quantity']} | {product['price']} | {total_price}\n"
        text += f"\n\nJami: {total}"
        await call.message.answer(text=text, reply_markup=buy)
    except Exception as e:
        text = f"😕 Sizni Savatingiz Bom Bosh!"
        await call.answer(text=text)

@dp.callback_query_handler(text="buy")
async def buy_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get("basket")
    adminga = "Mahsulotlar:\n"
    total = 0
    try:
        text = f"✅ Buyurtmangiz Qabul Qilindi!"
        for product in basket.values():
            total_price = product['quantity'] * product['price']
            total += total_price
            adminga += f"{product['name']} \t| <b>{product['size']}</b> \t| {product['quantity']} Ta \t"
        adminga += f"\n\n<b>Ja'mi</b>: {total}"
        await dp.bot.send_message(text=adminga, chat_id=5596277119)
        await call.answer(text=text)
    except Exception as e:
        text = f"😕 Sizni Savatingiz Bom Bosh!"
        await call.message.answer(text=text)
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
