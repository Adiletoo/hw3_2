from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")

@dp.message_handler(commands=["meme"])
async def picture(message: types.Message):
    images = os.listdir("images")
    image = random.choice(images)
    with open(f"images/{image}", "rb") as f:
        await bot.send_photo(chat_id=message.from_user.id, photo=f)


@dp.message_handler(commands=['quiz'])
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
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
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
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit:
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)