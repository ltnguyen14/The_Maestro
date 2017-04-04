import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button, text_box, selection_box
from data.players import initialize

class menu(object):
    def __init__(self):
        initialize.run()
        self.pass_arg = None
        self.bg_image = setup.GFX['background_1']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'height_input': (c.SCREEN_WIDTH/2,150),
                                'weight_input': (c.SCREEN_WIDTH/2,250),
                                'type_input': (c.SCREEN_WIDTH/2,350),

                                'height_label': (c.SCREEN_WIDTH/2,200),
                                'weight_label': (c.SCREEN_WIDTH/2,300),
                                'type_label': (c.SCREEN_WIDTH/2,400),

                                'next_button': (c.SCREEN_WIDTH - 80, c.SCREEN_HEIGHT - 30),
                                'back': (80, c.SCREEN_HEIGHT - 30),
                                'title' : (c.SCREEN_WIDTH/2, 50)}

        self.title = button.button(c.button_size, "YOUR BODY TYPE", c.BLUE,
                                        self.position_list['title'], "blank", "blank", center=True)

        self.back_button = button.button(c.small_button_sz, "BACK", c.YELLOW,
                                        self.position_list['back'], "rect_box", "rect_box_yellow", center=True, text_size = 20)
        self.next_button = button.button(c.small_button_sz, "NEXT", c.YELLOW,
                                        self.position_list['next_button'], "rect_box", "rect_box_yellow", center=True, text_size = 20)

        self.height_input = selection_box.menu(c.selection_sz, ['Short','Medium','Tall'], c.YELLOW,
                                            self.position_list['height_input'], "selection_blue", "selection_yellow", center=True, text_size = 20)
        self.height_label = button.button(c.button_size, "HEIGHT", c.RED,
                                        self.position_list['height_label'], "blank", "blank", center=True, text_size = 20)

        self.weight_input = selection_box.menu(c.selection_sz, ['Lean','Medium','Stocky'], c.YELLOW,
                                            self.position_list['weight_input'], "selection_blue", "selection_yellow", center=True, text_size = 20)
        self.weight_label = button.button(c.button_size, "WEIGHT", c.RED,
                                        self.position_list['weight_label'], "blank", "blank", center=True, text_size = 20)

        self.type_input = selection_box.menu(c.selection_sz, ['Agile','Mixed','Powerful'], c.YELLOW,
                                            self.position_list['type_input'], "selection_blue", "selection_yellow", center=True, text_size = 20)
        self.type_label = button.button(c.button_size, "PLAY TYPE", c.RED,
                                        self.position_list['type_label'], "blank", "blank", center=True, text_size = 20)

        self.buttons = (self.height_input, self.weight_input, self.type_input,
                            self.height_label, self.weight_label, self.type_label,
                            self.title, self.back_button, self.next_button)

        self.surface = pg.display.get_surface()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        #Update buttons
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.highlight = True
                result = button.update(mouse_state, mouse_pos)
                self.check_mouse_click(result)
            else:
                button.highlight = False
                button.draw()

    def check_mouse_click(self, result):
        if result == 'BACK':
            self.next = 'welcome_screen'
            self.done = True
        elif result == 'NEXT':
            self.next = 'player_info'
            self.pass_arg = 'player'
            self.done = True
