from data.states import menus
from . import setup, tools
from . import constants as c

def main():
    run = tools.Control(c.CAPTION)
    state_dict = {'main_menu' : menus.Menu()}

    run.setup_states(state_dict, "main_menu")
    run.main()
