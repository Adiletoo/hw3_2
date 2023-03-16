from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot



# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


# @dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    photo = open('media/images (1).jpg', 'rb')
    await message.answer_photo(photo=photo,
                               caption="Сам разбирайся!")

# @dp.message_handler(commands=['mem'])
# async def picture(message: types.Message):
#     media = os.listdir("media")
#     image = random.choice(media)
#     with open(f"media/{image}", "rb") as f:
#         await bot.send_photo(chat_id=message.from_user.id, photo=f)

#
# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Как зовут сына Наруто??"
    answer = [
        "Саске",
        "Сай",
        "Ямато",
        "Мицуки",
        "Баруто",
        "Нэджи",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Ты не фанат аниме",
        open_period=7,
        reply_markup=markup)




def register_handlers_client(dp: Dispatcher, mem_command=None, quiz_command=None):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    # dp.register_message_handler(mem_command, commands=['mem'])