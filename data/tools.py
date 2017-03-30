import pygame as pg
import os

class Control(object):
	def __init__(self, caption):
		self.screen = pg.display.get_surface()
		self.done = False
		self.clock = pg.time.Clock()
		self.caption = caption
		self.fps = 60
		self.keys = pg.key.get_pressed()
		self.state_dict = {}
		self.state_name = None
		self.state = None

	def setup_states(self, state_dict, start_state):
		self.state_dict = state_dict
		self.state_name = start_state
		self.state = self.state_dict[self.state_name]

	def update(self):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()
		self.state.update(self.screen, self.keys)

	def flip_state(self):
		previous, self.state_name = self.state_name, self.state.next
		persist = self.state.cleanup()
		self.state = self.state_dict[self.state_name]
		self.state.previous = previous
		self.state.startup(persist)

	def event_loop(self):
		self.events = pg.event.get()

		for event in self.events:
			if event.type == pg.QUIT:
				self.done = True
			elif event.type == pg.KEYDOWN:
				self.keys = pg.key.get_pressed()
				self.toggle_show_fps(event.key)
				self.state.get_event(event)
			elif event.type == pg.KEYUP:
				self.keys = pg.key.get_pressed()
				self.state.get_event(event)

	def main(self):
		while not self.done:
			self.event_loop()
			self.update()
			pg.display.update()
			self.clock.tick(self.fps)

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory,pic))
            graphics[name] = img

    return graphics
