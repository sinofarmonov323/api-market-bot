from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def apis_button(needs: list):
    if needs != []:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=need['name'], callback_data=need['callback_name'])] for need in needs
            ]
        )
    else:
        return None

def admin_panel_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="API qo'shish", callback_data="add_api")],
            [InlineKeyboardButton(text="Foydalanuvchilar sonini ko'rish", callback_data="see_users")]
        ]
    )
