from pieces.base_piece import Piece


class Bishop(Piece):
	def __init__(self, color, pos):
		super().__init__(name="bishop", color=color, pos=pos)
	
	@staticmethod
	def get_moves_list(row: int, col: int, board: list) -> list:
		return [cell.index for cell in filter(lambda x: abs(x.row - row) - abs(x.col - col) == 0, board)]
