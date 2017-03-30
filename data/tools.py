import pygame as pg
from . import constants as c
import os

class Control(object):
	def __init__(self, caption):
		self.screen = pg.display.get_surface()
		self.done = False
		self.clock = pg.time.Clock()
		self.caption = caption
		self.fps = c.FPS
		self.keys = pg.key.get_pressed()
		self.state_dict = {}
		self.state_name = None
		self.state = None

	def setup_states(self, state_dict, start_state):
		self.state_dict = state_dict
		self.state_name = start_state
		self.state = self.state_dict[self.state_name]
		self.state.startup()

	def update(self):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()

	def flip_state(self):
		previous, self.state_name = self.state_name, self.state.next
		self.state = self.state_dict[self.state_name]
		self.state.previous = previous
		self.state.startup()

	def event_loop(self):
		self.events = pg.event.get()

		for event in self.events:
			if event.type == pg.QUIT:
				self.done = True
			elif event.type in (pg.MOUSEMOTION, pg.MOUSEBUTTONUP, pg.MOUSEBUTTONDOWN):
				self.mouse_state = pg.mouse.get_pressed()
				self.mouse_pos = pg.mouse.get_pos()
				self.state.update(self.mouse_state, self.mouse_pos)

	def main(self):
		while not self.done:
			self.event_loop()
			self.update()
			pg.display.update()
			self.clock.tick(self.fps)

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', '.jpg', '.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory,pic))
            graphics[name] = img

    return graphics

def load_all_fonts(directory, accept=('.ttf')):
    fonts = {}
    for font in os.listdir(directory):
        name, ext = os.path.splitext(font)
        if ext.lower() in accept:
            fonts[name] = os.path.join(directory, font)
    return fonts
