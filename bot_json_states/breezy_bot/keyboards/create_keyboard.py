from breezy_bot.bot_states.bot_states import Bot_State
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

def create_keyboard(state: Bot_State) -> ReplyKeyboardMarkup:
    '''
    create keyboard for Bot State
    '''
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.append(state.params['user_answer_options'])
    return keyboard
