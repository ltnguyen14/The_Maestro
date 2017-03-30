import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import menu_option

class main_menu(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

        self.bg_image = setup.GFX['start_bg']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'start button': (50,100),
                                'option button': (50,220),
                                'quit button': (50,340)}

        self.start_button = menu_option.menu_option(c.menu_button_size, 'START', c.RED,
                                            self.position_list['start button'], "rect_box", "white_box", True)
        self.option_button = menu_option.menu_option(c.menu_button_size, 'OPTIONS', c.RED,
                                            self.position_list['option button'], "rect_box", "white_box",True)
        self.quit_button = menu_option.menu_option(c.menu_button_size, 'QUIT', c.OLIVE,
                                            self.position_list['quit button'], "rect_box", "white_box", True)

        self.buttons = (self.start_button, self.option_button, self.quit_button)

        self.surface = pg.display.get_surface()
        self.initialize()

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
            self.next = 'main_menu'
            self.done = True

class main_menu_test(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

        self.bg_image = setup.GFX['start_bg']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'start button': (0,100),
                                'quit button': (0,340)}

        self.start_button = menu_option.menu_option(c.menu_button_size, 'START', c.RED,
                                            self.position_list['start button'], "rect_box", "white_box", True)
        self.quit_button = menu_option.menu_option(c.menu_button_size, 'QUIT', c.OLIVE,
                                            self.position_list['quit button'], "rect_box", "white_box", True)

        self.buttons = (self.start_button, self.quit_button)

        self.surface = pg.display.get_surface()
        self.initialize()

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
            self.next = 'start_menu'
            self.done = True
