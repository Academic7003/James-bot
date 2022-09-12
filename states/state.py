from aiogram.dispatcher.filters.state import State, StatesGroup

class TruthAdd(StatesGroup):
    text = State()

class DareAdd(StatesGroup):
    text = State()