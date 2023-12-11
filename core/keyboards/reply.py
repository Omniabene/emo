from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Посоветовать фильм по эмоциям 🤪"
        )
    ],
    [
        KeyboardButton(
            text="Контакты 👥"
        ),
        KeyboardButton(
            text="Жанры 🎦"
        )
    ]
], resize_keyboard=True)

contact_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Вернуться в главное меню ◀️",
        )
    ]
], resize_keyboard=True)


question_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Прислать другие 🔃"
        )
    ],
    [
        KeyboardButton(
            text="Жанры 🎦"
        ),
        KeyboardButton(
            text="Вернуться в главное меню ◀️"
        )
    ]
], resize_keyboard=True)


genre_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Комедия 😆"
        ),
        KeyboardButton(
            text="Драма 😭"
        ),
        KeyboardButton(
            text="Фэнтези 🪄"
        ),
        KeyboardButton(
            text="Детектив 🕵️‍♀️"
        ),
        KeyboardButton(
            text="Tриллер 🔪"
        )
    ],
    [
        KeyboardButton(
            text="Приключение 🌋💍"
        ),
        KeyboardButton(
            text="Мультфильмы  🤖"
        ),
        KeyboardButton(
            text="Боевик 🔫 "
        ),
        KeyboardButton(
            text="Вернуться в главное меню ◀️"
        )
    ]
], resize_keyboard=True)
