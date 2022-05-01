from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import Dispatcher, filters

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import logging

from states.load_states import load_states, run_dialog

class Breezy_Bot(Bot):
    def __init__(self):
        self.states = load_states()
        # logging

        @self.dp.message_handler(state='*' )
        async def process(message: types.Message):
            state = self.dp.current_state(user=message.from_user.id)
            self.log_info(state, message)
            run_dialog(state, message)

    def log_info(self, state, message):
        state_name = state.storage.data[str(message.from_user.id)][str(message.from_user.id)]['state']
        logging.info(state_name)


