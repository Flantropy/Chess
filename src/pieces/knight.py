from pieces.base_piece import Piece
from itertools import product
from typing import List


class Knight(Piece):
	def __init__(self, color, pos):
		super().__init__(name="knight", color=color, pos=pos)
	
	def get_moves_list(self, board: list) -> List[int]:
		x, y = self.row, self.col
		moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
		moves = [x*8 + y for x, y in moves if 8 > x >= 0 and 8 > y >= 0]
		return moves
