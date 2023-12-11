import asyncio
from aiogram import Bot, Dispatcher
from core.handlers.basic import (get_start, get_menu, handle_back_to_main_menu, get_contact, get_genre, get_help,
                                 get_filmToDrama, get_filmToComedy, get_filmToAdventure, get_filmToFantasy,
                                 get_filmToCartoons, get_filmToThriller, get_filmToDetectives, get_filmToFighters)
from core.settings import settings
from core.utils.commands import set_commands
from aiogram.filters import Command
from core.handlers import request
from core.utils.statesrequest import StepsForm
from core.utils import database


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')


async def start():
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()
    await database.db_start()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(request.get_request, lambda message: message.text == "Посоветовать фильм по эмоциям 🤪")
    dp.message.register(request.get_video, StepsForm.GET_VIDEO)

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(get_menu, Command(commands='menu'))
    dp.message.register(get_contact, lambda message: message.text == "Контакты 👥")
    dp.message.register(get_genre, lambda message: message.text == "Жанры 🎦")
    dp.message.register(handle_back_to_main_menu, lambda message: message.text == "Вернуться в главное меню ◀️")
    dp.message.register(get_filmToComedy, lambda message: message.text == "Комедия 😆")
    dp.message.register(get_filmToDrama, lambda message: message.text == "Драма 😭")
    dp.message.register(get_filmToFantasy, lambda message: message.text == "Фэнтези 🪄")
    dp.message.register(get_filmToThriller, lambda message: message.text == "Tриллер 🔪")
    dp.message.register(get_filmToFighters, lambda message: message.text == "Боевик 🔫 ")
    dp.message.register(get_filmToAdventure, lambda message: message.text == "Приключение 🌋💍")
    dp.message.register(get_filmToDetectives, lambda message: message.text == "Детектив 🕵️‍♀️")
    dp.message.register(get_filmToCartoons, lambda message: message.text == "Мультфильмы  🤖")
    dp.message.register(request.get_films, lambda message: message.text == "Прислать другие 🔃")


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
