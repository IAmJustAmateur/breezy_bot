import json
from typing import Any, Dict, List, NamedTuple
from aiogram.dispatcher.filters.state import State, StatesGroup

#from breezy_bot.keyboards import create_keyboard

from aiogram import types

(
    SUCCESS,
    DIALOGS_JSON_FILE_ERROR,
    
) = range(2)

ERRORS = {
    DIALOGS_JSON_FILE_ERROR: "dialogs JSON file error",
}

class Bot_States(StatesGroup):
    GreetingState = State()
    ReactionState = State()
    NewTopicState = State()
    QuizState = State()
    QuizAnswerState = State()

dialog_states = {
    "greeting": Bot_States.GreetingState,
    "reaction": Bot_States.ReactionState,
    "new topic": Bot_States.NewTopicState,
    "quiz": Bot_States.QuizState,
    "quiz answer": Bot_States.QuizAnswerState,
}

class StatesReading(NamedTuple):
    states: List[Any]
    error: int

def load_dialogs_data(states_file: str) ->StatesReading:
    '''
    load bot dialogs data
    '''
    print ("in load_states")
    try:
        f = open(states_file, encoding = 'utf-8')
        data = json.load(f)
        f.close()
        return StatesReading(data['states'], SUCCESS)
    except IOError:
        pass
    return StatesReading([], DIALOGS_JSON_FILE_ERROR)

class Dialog_State():
    def __init__(self, state_params: dict):
        self.state = dialog_states[state_params["type"]]
        self.params = state_params
        
async def run_dialog(states: Any, state: Dialog_State, message: types.Message):
    pass
    

def load_dialogs(states_file: str) ->List[State]:
    states = []
    sr = load_dialogs_data(states_file)
    if sr.error != SUCCESS:
        return None
    for s in sr.states:
        s = Dialog_State(s)
        states.append(s)
    return states