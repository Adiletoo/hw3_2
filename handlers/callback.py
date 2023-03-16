from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message

from config import bot


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
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
        reply_markup=markup
    )


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько лет Леонелю Месси"
    answer = [
        "30",
        "29",
        "37",
        "35",
        "41",
        "33",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Ты не любитель фудбола",
        open_period=7,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    question = "Сколько??"
    answer = [
        '4',
        '9',
        '6',
        '17',
        '8',
    ]

    photo = open("media/7cc9b750009267eb26046b3e1a.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        # open_period=5,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")