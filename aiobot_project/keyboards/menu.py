from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Спросить ChatGPT")],
        [KeyboardButton(text="Отправь фото")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери действие 👇"
)
