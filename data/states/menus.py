import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button

class start_menu(object):
    def __init__(self):
        self.bg_image = setup.GFX['start_bg']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'start button': (50,200),
                                'option button': (50,320),
                                'quit button': (50,440)}

        self.start_button = button.button(c.button_size, 'START', c.RED,
                                            self.position_list['start button'], "rect_box", "rect_box_yellow", True)
        self.option_button = button.button(c.button_size, 'OPTIONS', c.RED,
                                            self.position_list['option button'], "rect_box", "rect_box_yellow",True)
        self.quit_button = button.button(c.button_size, 'QUIT', c.OLIVE,
                                            self.position_list['quit button'], "rect_box", "rect_box_yellow", True)

        self.buttons = (self.start_button, self.option_button, self.quit_button)

        self.surface = pg.display.get_surface()
        self.initialize()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def initialize(self):
        for button in self.buttons:
            button.draw()

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        result = None
        for button in self.buttons:
            if button.hl_able == True:
                if button.rect.collidepoint(mouse_pos):
                    button.highlight = True
                    result = button.update(mouse_state, mouse_pos)
                else:
                    button.highlight = False
                    button.draw()
            else:
                button.draw()
        if result == 'QUIT':
            self.quit = True
        elif result == 'START':
            self.next = 'welcome_screen'
            self.done = True
        elif result == 'OPTIONS':
            self.next = 'option_menu'
            self.done = True

class welcome_screen(object):
    def __init__(self):
        self.bg_image = setup.GFX['start_bg']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'welcome message': (c.SCREEN_WIDTH/2,c.SCREEN_HEIGHT/2),
                                'next button': (500, 500)}

        self.welcome_message = button.button(c.button_size, 'WELCOME GUYS', c.RED,
                                            self.position_list['welcome message'], "rect_box", "white_box", True, True)
        self.next_button = button.button(c.button_size, 'NEXT', c.GREEN,
                                            self.position_list['next button'], "rect_box", "rect_box_yellow", True)

        self.buttons = (self.welcome_message, self.next_button)

        self.surface = pg.display.get_surface()
        self.initialize()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def initialize(self):
        for button in self.buttons:
            button.draw()

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        result = None
        for button in self.buttons:
            if button.hl_able == True:
                if button.rect.collidepoint(mouse_pos):
                    button.highlight = True
                    result = button.update(mouse_state, mouse_pos)
                else:
                    button.highlight = False
                    button.draw()
            else:
                button.draw()
