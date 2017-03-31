import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button

class menu(object):
    def __init__(self):
        self.bg_image = setup.GFX['start_bg']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'start button': (0, c.SCREEN_HEIGHT - c.small_button_sz[1])}

        self.start_button = button.button(c.small_button_sz, 'BACK', c.RED,
                                            self.position_list['start button'], "rect_box", "rect_box_yellow")

        self.buttons = (self.start_button,)

        self.surface = pg.display.get_surface()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        result = None
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.highlight = True
                result = button.update(mouse_state, mouse_pos)
            else:
                button.highlight = False
                button.draw()
        self.check_mouse_click(result)

    def check_mouse_click(self,result):
        if result == 'BACK':
            self.next = 'start_menu'
            self.done = True
