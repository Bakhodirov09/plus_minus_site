from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍟 Mahsulotlar")
        ]
    ], resize_keyboard=True
)

products_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Gamburger")
        ]
    ], resize_keyboard=True
)

product_inside_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Katta"),
            KeyboardButton(text="Kichik")
        ]
    ], resize_keyboard=True
)