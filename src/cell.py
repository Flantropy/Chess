from typing import Optional

from chess import FILE_NAMES, RANK_NAMES
from pygame import Surface
from pygame.sprite import Sprite

from res.constants import CELL_H, CELL_SIZE, CELL_W
from res.ultracolors import LIGHT_SEA_GREEN, MEDIUM_WOOD, WHITE


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
        self.selected = False
    
    def update(self, *args, **kwargs):
        if self.selected:
            self.image.fill(LIGHT_SEA_GREEN)
        else:
            self.image.fill(self.color)
        if self.piece:
            Surface.blit(self.image, self.piece, dest=(0, 0))
    
    def __str__(self):
        return self.file + self.rank
