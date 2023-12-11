from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import menu_keyboard, contact_keyboard, genre_keyboard
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.utils import database


async def get_start(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!👋🏼 \n'
                                                 f'Наш бот 🤖 анализирует ваши эмоции по видео и голосу, чтобы '
                                                 f'порекомендовать фильм 🎥 , который точно подходит под ваше '
                                                 f'настроение. Забудьте о бесконечных ♾️ поисках — доверьтесь боту🤖,'
                                                 f' и наслаждайтесь кино без лишних хлопот. Погружайтесь в мир фильмов,'
                                                 f' не теряя времени на выбор!❤️🍿', reply_markup=menu_keyboard)


async def get_help(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет! 🎬✨ Добро пожаловать в уютный мир фильмов с эмоциями!'
                                                 f' 🍿🌈 Я здесь, чтобы сделать твой выбор кино ещё более '
                                                 f'захватывающим. Спроси меня о фильмах, поделись своим настроением, '
                                                 f'и я подскажу идеальный фильм для твоей текущей эмоции. '
                                                 f'🤔💖 Вместе мы создадим кинематографическое приключение, '
                                                 f'которое запомнится надолго. 🚀🎥 Готов начать волнующее '
                                                 f'киносафари?', reply_markup=contact_keyboard)


async def get_menu(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Это главное меню нашего бота', reply_markup=menu_keyboard)


async def get_contact(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Мы команда по разработке этого бота. '
                                                 f'Ниже ты увидишь ссылки на наши аккаунты.  '
                                                 f'Обращайся по любым вопросам!\n'
                                                 f'@Omniabene - разработчик тг бота\n'
                                                 f'@Polinn_Ko - нейросеть для определения эмоций по голосу\n'
                                                 f'@SirGeorgy нейросеть для определения эмоций по видео '
                           , reply_markup=contact_keyboard)


async def get_genre(message:Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'В этой вкладке вы можете выбрать любой жанр и я предложу '
                                                 f'вам соотвествующую подборку фильмов'
                           , reply_markup=genre_keyboard)


async def handle_back_to_main_menu(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=menu_keyboard)


async def get_filmToComedy(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("comedy", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToDrama(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("drama", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToFantasy(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("fantasy", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )



async def get_filmToThriller(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("thriller", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToFighters(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("fighters", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToAdventure(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("adventures", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToDetectives(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("detectives", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )


async def get_filmToCartoons(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    for i in range(0, 3):
        film = await database.get_info("cartoons", num[i])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{film[0]}', url=f'{film[2]}')
            ]
        ])
        await bot.send_photo(chat_id=message.chat.id,
                             caption=f'{film[1]}',
                             photo=f'{film[3]}',
                             reply_markup=keyboard
                             )

