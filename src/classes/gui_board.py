import chess
import pygame
from typing import List, Optional
from classes.cell import Cell
from res.constants import CELL_SIZE, DIR_IMAGES


class GUIBoard:
    def __init__(self, board: chess.Board):
        self.board = board
        self.__sprites = []
        self.selected_cell: Optional[Cell] = None
    
    @property
    def sprites(self):
        return self.__sprites
    
    @sprites.setter
    def sprites(self, value: List[Cell]):
        self.__sprites = value
    
    @classmethod
    def get_cells(cls) -> List[Cell]:
        cells = []
        for rank in chess.RANK_NAMES:
            for file in chess.FILE_NAMES:
                cells.append(Cell(rank=rank, file=file))
        return cells
    
    def update_piece_positions(self, fen: str) -> None:
        for cell in self.sprites:
            cell.piece = None
        pieces = dict(p="pawn", b="bishop", r="rook", n="knight", q="queen", k="king")
        i = 0
        for row in reversed(fen.split("/")):
            for symbol in row:
                if symbol.isdigit():
                    i += int(symbol)
                else:
                    color = "w" if symbol.isupper() else "b"
                    image = pygame.transform.scale(pygame.image.load
                                                   (DIR_IMAGES + f"\\{color}_{pieces[symbol.lower()]}.png"),
                                                   CELL_SIZE)
                    self.sprites[i].piece = image
                    i += 1
