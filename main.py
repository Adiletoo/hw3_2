from aiogram.utils import executor
from config import dp, bot, ADMINS
from handlers import client, callback, extra, admin, fsmAdminMentor
import logging
import asyncio
from database.bot_dp import sql_create

async def on_startup(_):
    await bot.send_message(chat_id=ADMINS[0], text='Бот запущен')
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsmAdminMentor.register_handlers_fsm_anketa(dp)
# extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
