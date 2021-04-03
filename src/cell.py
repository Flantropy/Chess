from pygame import sprite, Surface
from res.constants import CELL_SIZE
from res.ultracolors import LIGHT_BLUE_1


class Cell(sprite.Sprite):
	"""
	This class is item of Board.grid
	"""
	def __init__(self, color, notation, pos=(0, 0)):
		super(Cell, self).__init__()
		self.row, self.col = notation
		self.color = color
		self.image = Surface(CELL_SIZE)
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.piece = None
		self.selected = False
		
	def draw(self, display):
		display.blit(self.image, self.rect)
		
	def get_center(self):
		return self.rect.center

	def update(self, *args, **kwargs):
		if self.selected:
			self.image.fill(LIGHT_BLUE_1)
			
		else:
			self.image.fill(self.color)
