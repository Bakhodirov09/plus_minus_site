from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buy_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="minus"),
            InlineKeyboardButton(text="2/20000", callback_data="show"),
            InlineKeyboardButton(text="➕", callback_data="plus"),
        ],
        [
            InlineKeyboardButton(text="Savatni ko'rish", callback_data="show_basket")
        ]
    ]
)