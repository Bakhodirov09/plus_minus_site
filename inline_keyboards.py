from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def plus_minus_bttn(now):
    buy_product = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="minus"),
                InlineKeyboardButton(text=f"{now}", callback_data="show"),
                InlineKeyboardButton(text="➕", callback_data="plus"),
            ],
            [
                InlineKeyboardButton(text="Savatni ko'rish", callback_data="show_basket")
            ]
        ]
    )
    return buy_product

buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒 Sotib Olish", callback_data="buy")
        ]
    ]
)