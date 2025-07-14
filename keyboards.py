from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def apis_button(needs: list):
    if needs != []:
        builder = InlineKeyboardBuilder()
        for need in needs:
            builder.add(InlineKeyboardButton(text=need['name'], callback_data=need['callback_name']))
        builder.adjust(2)
        return builder.as_markup()
    else:
        return None

def admin_panel_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="API qo'shish", callback_data="api")],
            [InlineKeyboardButton(text="Foydalanuvchilar sonini ko'rish", callback_data="see_users")]
        ]
    )
