from breezy_bot.bot_states.bot_states import Bot_State
from aiogram import types
from keyboards import create_keyboard


async def greeting_dialog(state: Bot_State, message: types.message):
    keyboard = create_keyboard(state)
    message_text = state.params["messages"][0]
    keyboard = create_keyboard(state)
    await message.answer (message_text, reply_markup = keyboard)
    await state.set_state(state.params["next_state"])


async def reaction(state: Bot_State, message: types.message):

    pass

