import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button, text_box

class welcome_screen(object):
    def __init__(self):
        self.pass_arg = None
        self.bg_image = setup.GFX['start_bg_2']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'welcome message': (c.SCREEN_WIDTH/2,c.SCREEN_HEIGHT/2),
                                'next button': (500, 500)}

        self.welcome_message = text_box.text_box(c.welcome_box_size, c.WELCOME_MESS, c.TEAL,
                                            self.position_list['welcome message'], "white_box", True, 28)
        self.next_button = button.button(c.small_button_sz, 'GET STARTED', c.YELLOW,
                                            self.position_list['next button'], "rect_box", "rect_box_yellow", text_size=20)

        self.buttons = (self.welcome_message, self.next_button)

        self.surface = pg.display.get_surface()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        result = None
        #Update buttons
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.highlight = True
                result = button.update(mouse_state, mouse_pos)
            else:
                button.highlight = False
                button.draw()
        self.check_mouse_click(result)

    def check_mouse_click(self, result):
        if result == "GET STARTED":
            self.next = "creation_menu"
            self.done = True
