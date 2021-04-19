from pieces.base_piece import Piece
from pieces.rook import Rook
from pieces.bishop import Bishop


class Queen(Piece):
	def __init__(self, color, pos):
		super().__init__(name="queen", color=color, pos=pos)
	
	@staticmethod
	def get_moves_list(row: int, col: int, board: list) -> list:
		moves = Rook.get_moves_list(row, col, board)
		moves.extend(Bishop.get_moves_list(row, col, board))
		return moves
