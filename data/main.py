from data.states import start_menu, welcome_screen, option_menu, creation_menu
from . import setup, tools
from . import constants as c

def main():
    run = tools.Control(c.CAPTION)
    state_dict = {'start_menu' : start_menu.start_menu(),
                    'welcome_screen' : welcome_screen.welcome_screen(),
                    'option_menu' : option_menu.menu(),
                    'creation_menu' : creation_menu.menu()}

    run.setup_states(state_dict, "start_menu")
    run.main()
