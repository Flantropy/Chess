from pygame import sprite, Surface
from constants import LARGE_TILE_SIZE, WHITE, COLS_AS_STR


class Cell(sprite.Sprite):
	def __init__(self, color=WHITE, pos=(0, 0), notation=(0, 0), piece=None):
		super(Cell, self).__init__()
		self.x, self.y = pos
		self.image = Surface(LARGE_TILE_SIZE).convert()
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.color = color
		self.image.fill(self.color)
		self.piece = piece
		self.col_int, self.row_int = notation
		self.col = COLS_AS_STR[self.col_int]
		self.row = abs(self.row_int - 8)  # row for "D2-D4" notation
		self.row_int = abs(self.row_int - 7)  # row for "0:0 - 7:7" notation
		self.is_selected = False
	
	def update(self):
		if self.is_selected:
			self.image.fill((0, 255, 0))
		else:
			self.image.fill(self.color)
			
	def __str__(self):
		"""
		Returns cell position with "A:1" format
		:return: str
		"""
		return f"{self.col}:{self.row}"
