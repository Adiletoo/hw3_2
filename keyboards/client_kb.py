from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=3
)

# =====================================================================================================================
start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz1')
mem_button = KeyboardButton('/mem')

start_markup.add(start_button, info_button, quiz_button, mem_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('да'),
    KeyboardButton('нет')
)
cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)