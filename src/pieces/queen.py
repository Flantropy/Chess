from pieces.base_piece import Piece
from typing import List
from classes.cell import Cell


class Queen(Piece):
	def __init__(self, color, pos):
		super().__init__(name="queen", color=color, pos=pos)
	
	def get_moves_list(self, board: List[Cell]) -> List[int]:
		bishop_moves = super().get_bishop_moves(board)
		rook_moves = super().get_rook_moves(board)
		return bishop_moves + rook_moves
