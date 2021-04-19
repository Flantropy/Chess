from pieces.base_piece import Piece


class Rook(Piece):
	def __init__(self, color, pos):
		super().__init__(name="rook", color=color, pos=pos)
	
	@staticmethod
	def get_moves_list(row: int, col: int, board: list) -> list:
		return [cell.index for cell in filter(lambda x: x.row == row or x.col == col, board)]
