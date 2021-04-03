# item of Board.grid[]
from pygame import sprite, Surface
from res.constants import CELL_SIZE
from res.ultracolors import WHITE


class Cell(sprite.Sprite):
	def __init__(self, pos=(0, 0), color=WHITE):
		super(Cell, self).__init__()
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
			self.image.fill((0, 255, 0))
		else:
			self.image.fill(self.color)
