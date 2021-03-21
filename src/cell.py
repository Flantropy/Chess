from pygame import sprite, Surface
from constants import LARGE_TILE_SIZE, WHITE, COLS_AS_STR


class Cell(sprite.Sprite):
	def __init__(self, color=WHITE, pos=(0, 0), notation=(0, 0)):
		super(Cell, self).__init__()
		self.x, self.y = pos
		self.image = Surface(LARGE_TILE_SIZE).convert()
		self.rect = self.image.get_rect()
		self.rect.topleft = pos
		self.color = color
		self.image.fill(self.color)
		self.piece = None
		self.col, self.row = notation
		self.col = COLS_AS_STR[self.col]
		self.row = abs(self.row - 8)
		self.is_selected = False
	
	def add_piece(self, piece=None):
		self.piece = piece
	
	def update(self):
		if self.is_selected:
			self.image.fill((0, 255, 0))
		else:
			self.image.fill(self.color)
