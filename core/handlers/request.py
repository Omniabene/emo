from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesrequest import StepsForm
from func import  handle_video_note
from core.settings import settings
from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import random
from core.utils import database
from core.keyboards.reply import question_keyboard
from core.handlers.basic import handle_back_to_main_menu

bot = Bot(token=settings.bots.bot_token)




async def get_request(message: Message, state: FSMContext):
    await message.answer(f'Здравствуйте, {message.from_user.first_name}!\n'
                         f'Отправь мне кружочек, и я отправлю тебе подборку фильмов по эмоциям '
                         f'которые ты сейчас испытываетшь', reply_markup=ReplyKeyboardRemove())
    await state.set_state(StepsForm.GET_VIDEO)


async def get_video(message: Message, state: FSMContext):

    if message.video_note:
        await message.answer(f'Мы приняли ваш кружочек, теперь чуть-чуть подождите.')
        num = random.sample(range(1, 11), 3)
        emo = await handle_video_note(message, bot)
        with open('file.txt', 'w', encoding='utf-8') as file:
            file.write(emo)
        if emo == "Happy":
            await message.answer("Я определил, что вы счастливы, поэтому предлагаю Вам на выбор три комедии.")
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
        elif emo == "Surprised":
            await message.answer("Я определил, что вы удивлены, поэтому предлагаю Вам на выбор фэнтези.")
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
        elif emo == "Neutral":
            num = random.sample(range(1, 11), 5)
            list = ["comedy", "drama", "fantasy", "thriller", "fighters", "adventures", "detectives", "cartoons"]
            random_selection = random.sample(list, 5)
            await message.answer("Я определил, что у вас нейтральное настроение, поэтому предлагаю "
                                 "Вам на выбор пять фильмов из каждой категории.")
            for i in range(0, 5):
                film = await database.get_info(random_selection[i], num[i])
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
        elif emo == "Angry":
            await message.answer("Я определил, что вы злитесь, поэтому предлагаю Вам на выбор три боевика.")
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
        elif emo == "Sad":
            await message.answer("Я определил, что вам грустно, поэтому предлагаю Вам на выбор три драмы.")
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
        await message.answer("Не понравились предложенные фильмы? Ничего страшного!😉Ты можешь попробовать "
                             "ещё раз, вернувшись назад в главное меню или выбрать жанр фильмов самостоятельно.🚀",
                             reply_markup=question_keyboard)
        await state.clear()
    else:
        await message.answer("Ты отправил не кружок.\n"
                             "Отправь кружок чтобы я мог предложить тебе вильмы")
        await state.set_state(StepsForm.GET_VIDEO)


async def get_films(message: Message, bot: Bot):
    num = random.sample(range(1, 11), 3)
    with open('file.txt', 'r', encoding='utf-8') as file:
        posled = file.read()

    if posled == "Happy":
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
    elif posled == "Surprised":
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
    elif posled == "Neutral":
        num = random.sample(range(1, 11), 5)
        list = ["comedy", "drama", "fantasy", "thriller", "fighters", "adventures", "detectives", "cartoons"]
        random_selection = random.sample(list, 5)
        for i in range(0, 5):
            film = await database.get_info(random_selection[i], num[i])
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
    elif posled == "Angry":
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
    elif posled == "Sad":
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
    await handle_back_to_main_menu(message, bot)

