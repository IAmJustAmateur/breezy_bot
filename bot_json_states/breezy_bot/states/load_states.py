import json
from typing import Any, Dict, List, NamedTuple
from aiogram.dispatcher.filters.state import State, StatesGroup
from breezy_bot import SUCCESS, ERRORS, DIALOGS_JSON_FILE_ERROR

from aiogram import types

class StatesReading(NamedTuple):
    states: List[Any]
    error: int

def load_states_data(states_file: str) ->StatesReading:
    print ("in load_states")
    try:
        f = open(states_file, encoding = 'utf-8')
        data = json.load(f)
        f.close()
        return StatesReading(data['states'], SUCCESS)
    except IOError:
        pass
    return StatesReading([], DIALOGS_JSON_FILE_ERROR)

class Bot_State(State):
    def __init__(self, state_params: dict, *args, **kwargs):
        super().__init__(state_params["name"])
        self.params = state_params
        #self.handler = handlers[self.params.type]

def run_dialog(state: State, message: types.Message):
    pass

def load_states(states_file: str) ->List[State]:
    states = []
    sr = load_states_data(states_file)
    if sr.error != SUCCESS:
        return None
    for s in sr.states:
        s = Bot_State(s)
        states.append(s)
    return states
    


