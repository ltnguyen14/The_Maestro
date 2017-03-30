from data.states import menus, option_menu
from . import setup, tools
from . import constants as c

def main():
    run = tools.Control(c.CAPTION)
    state_dict = {'start_menu' : menus.start_menu(),
                    'welcome_screen' : menus.welcome_screen(),
                    'option_menu' : option_menu.menu()}

    run.setup_states(state_dict, "start_menu")
    run.main()
