import handlers
from aiogram import types
from aiogram.dispatcher import Dispatcher as dp
from states.load_states import Bot_State
from keyboards.create_keyboard import create_keyboard

async def greeting(state: Bot_State, message: types.Message):
    keyboard = create_keyboard(state.params)

    



