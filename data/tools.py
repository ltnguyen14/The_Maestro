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
		self.pass_arg = None

	def setup_states(self, state_dict, start_state):
		self.state_dict = state_dict
		self.state_name = start_state
		self.state = self.state_dict[self.state_name]
		self.state = self.state()
		self.state.startup()

	def update(self):
		if self.state.quit:
			self.done = True
		elif self.state.done:
			self.flip_state()

	def flip_state(self):
		self.pass_arg = self.state.pass_arg
		previous, self.state_name = self.state_name, self.state.next
		self.state = self.state_dict[self.state_name]
		if self.pass_arg != None:
			self.state = self.state(self.pass_arg)
		else:
			self.state = self.state()
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

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pg.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left + c.text_box_offset, y + c.text_box_offset))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

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
