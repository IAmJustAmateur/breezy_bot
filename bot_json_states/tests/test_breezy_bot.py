#from states import load_states_data, load_states

from breezy_bot import DIALOGS_JSON_FILE_ERROR, SUCCESS
#from breezy_bot.states.load_states import load_states_data, load_states
from   breezy_bot.states import  load_states
import  pprint

def test_load_states():
    import os
    dialogs_path = os.path.join (os.getcwd(), ".env", "dialogs.json")
    states = load_states.load_states(dialogs_path)
    pprint.pprint (states)
    