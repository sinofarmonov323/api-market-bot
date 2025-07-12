from aiogram import Bot, Dispatcher, types, F, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from keyboards import apis_button, admin_panel_button
from database import add_api, add_user, get_callback_names, get_api, get_all_apis, delete_api, get_all_users_number
import logging
import asyncio

dp = Dispatcher()

ADMIN_ID = 7077167971

@dp.message(CommandStart())
async def start(message: types.Message):
    add_user(message.from_user.id, message.from_user.username)
    await message.answer(f"Salom {html.bold(message.from_user.full_name)}\nbu botda siz har xil APIlar olshingiz mumkin\nSizga qanday API kerak", reply_markup=apis_button(get_all_apis()))

# @dp.message(Command("admin"))
# async def admin_panel(message: types.Message):
#     if message.from_user.id == ADMIN_ID:
#         await message.answer(f"Admin panel", reply_markup=admin_panel_button())
#     else:
#         await message.answer("/admin")

@dp.message(Command("users"))
async def send_users_number(message: types.Message):
    await message.answer(f"Foydalanuvchilar soni: {len(get_all_users_number())}")

# @dp.callback_query(F.data.in_(["api", "see_users"]))
# async def send_users_number(call: types.CallbackQuery):
#     if call.from_user.id == ADMIN_ID:
#         if call.data == "see_users":
#             await call.message.answer(f"Foydalanuvchilar soni: {len(get_all_users_number())}")
#         elif call.data == "api":
#             await call.message.answer(f"Ishlatish: {html.code("/add_api")} api_name, api_url, callback_name, sarlavha, narx")
#         await call.answer()
#     else:
#         print("NOT EQUAL")
    
@dp.message(Command("delete"))
async def delete_the_api(message: types.Message, command: CommandObject):
    try:
        delete_api(command.args)
        await message.answer("API o'chirildi")
    except Exception as e:
        print("API O'chirilmadi: ", e)
        await message.answer("Bunday API topilmadi")

@dp.message(Command("add_api"))
async def add_new_api(message: types.Message, command: CommandObject):
    if message.from_user.id == ADMIN_ID:
        if command.args != None:
            args = command.args.replace(", ", ",").split(",")
            if len(args) >= 5:
                title, url, callback_name, caption, price = args[0], args[1], args[2], args[3], args[4]
                add_api(title, url, callback_name, caption, price)
                await message.answer("API qo'shildi")
            else:
                await message.answer("nimanidir xato qildingiz")
                await message.answer(f"Ishlatish: {html.code("/add_api")} api_name, api_url, callback_name, sarlavha, narx")
        else:
            await message.answer(f"Ishlatish: {html.code("/add_api")} api_name, api_url, callback_name, sarlavha, narx")

@dp.callback_query()
async def send_info(call: types.CallbackQuery):
    if call.data in get_callback_names():
        data = get_api(call.data)
        await call.message.answer(f"{html.bold(data['name'])}\n\n🔗{data['url']}\n💸Narxi: {data['price']}\n\n{data['caption']}")
        await call.answer(cache_time=1)

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    bot = Bot('8106975001:AAEhrChQRTTo2Z5t96fIRFd23GxNEhHvZjE', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(
        [types.BotCommand(command="start", description="botni ishga tushirish")]
    )
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
