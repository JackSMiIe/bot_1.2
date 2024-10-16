import asyncio
import os

from aiogram import Bot,Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from dotenv import find_dotenv,load_dotenv

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_command_list import private
from handlers.admin_private import admin_router

ALLOWED_UPDATES = ['message','edited_message']

bot = Bot(
    token=os.getenv('TOKEN'),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
bot.my_admins_list = []
dp = Dispatcher()

dp.include_routers(user_private_router)
dp.include_routers(user_group_router)
dp.include_router(admin_router)




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot,allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())



