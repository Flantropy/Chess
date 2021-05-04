from pygame.sprite import Sprite
from pygame import Surface
from typing import Optional
from chess import Piece, RANK_NAMES, FILE_NAMES
from res.ultracolors import WHITE, MEDIUM_WOOD
from res.constants import CELL_SIZE, CELL_W, CELL_H


class Cell(Sprite):
	def __init__(self, rank, file, piece: Optional[Surface] = None):
		super(Cell, self).__init__()
		self.rank = rank
		self.file = file
		self.piece = piece
		self.color = MEDIUM_WOOD if (RANK_NAMES.index(self.rank) + FILE_NAMES.index(self.file)) % 2 == 0 else WHITE
		self.image = Surface(CELL_SIZE)
		self.image.fill(self.color)
		self.rect = self.image.get_rect()
		self.rect.x = FILE_NAMES.index(self.file) * CELL_W
		self.rect.y = list(reversed(RANK_NAMES)).index(self.rank) * CELL_H
	
	def update(self, *args, **kwargs):
		if self.piece:
			Surface.blit(self.image, self.piece, dest=(0, 0))
