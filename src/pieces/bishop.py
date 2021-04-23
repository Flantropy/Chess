from pieces.base_piece import Piece
from typing import List
from classes.cell import Cell


class Bishop(Piece):
	def __init__(self, color, pos):
		super().__init__(name="bishop", color=color, pos=pos)
	
	def get_moves_list(self, board: List[Cell]) -> List[int]:
		return super().get_bishop_moves(board)

