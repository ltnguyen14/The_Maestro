from data.states import menus
from . import setup, tools
from . import constants as c

def main():
    run = tools.Control(c.CAPTION)
    state_dict = {'start_menu' : menus.main_menu(),
                    'main_menu' : menus.main_menu_test()}

    run.setup_states(state_dict, "main_menu")
    run.main()
