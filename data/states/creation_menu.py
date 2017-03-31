import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button, text_box

class menu(object):
    def __init__(self):
        self.bg_image = setup.GFX['background_1']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'start button': (50,200),
                                'option button': (50,320),
                                'quit button': (50,440),
                                'title box': (c.SCREEN_WIDTH/2, 100)}

        self.start_button = button.button(c.button_size, 'START', c.YELLOW,
                                            self.position_list['start button'], "rect_box", "rect_box_yellow")
        self.option_button = button.button(c.button_size, 'OPTIONS', c.YELLOW,
                                            self.position_list['option button'], "rect_box", "rect_box_yellow")
        self.quit_button = button.button(c.button_size, 'QUIT', c.OLIVE,
                                            self.position_list['quit button'], "rect_box", "rect_box_yellow")

        self.title_box = text_box.text_box(c.button_size, 'THE MAESTRO', c.TEAL,
                                            self.position_list['title box'], "white_box", True, 45)

        self.buttons = ()

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
        if result == 'QUIT':
            self.quit = True
        elif result == 'START':
            self.next = 'welcome_screen'
            self.done = True
        elif result == 'OPTIONS':
            self.next = 'option_menu'
            self.done = True
