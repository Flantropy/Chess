from pygame import sprite, Surface
from res.constants import CELL_SIZE
from res.ultracolors import PALE_GREEN_3, PALE_VIOLET_RED_1


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
		self.selection_rect = Surface(CELL_SIZE)
		self.selection_rect.fill(PALE_GREEN_3)
		self.selection_rect.set_alpha(150)
		self.selection_counter = 0
	
	def update(self, *args, **kwargs):
		if self.selected:
			if self.selection_counter == 0:
				Surface.blit(self.image, self.selection_rect, (0, 0))
				self.selection_counter += 1
		else:
			self.selection_counter = 0
			self.image.fill(self.color)
		if self.piece:
			Surface.blit(self.image, self.piece.image, (5, 6))
