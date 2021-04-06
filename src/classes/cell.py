from pygame import sprite, Surface
from res.constants import CELL_SIZE
from res.ultracolors import LIGHT_BLUE_1, LAVENDER_BLUSH_3


class Cell(sprite.Sprite):
	"""
	This class is item of Board.grid
	"""
	def __init__(self, color, notation, position_on_display):
		super(Cell, self).__init__()
		self.row, self.col = notation
		self.color = color
		self.image = Surface(CELL_SIZE)
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.topleft = position_on_display
		self.piece = None
		self.selected = False
		self.index = self.row * 8 + self.col

	def update(self, *args, **kwargs):
		if self.selected:
			self.image.fill(LIGHT_BLUE_1)
		else:
			self.image.fill(self.color)
