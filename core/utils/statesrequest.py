from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_VIDEO = State()
    GET_CONSENT = State()
