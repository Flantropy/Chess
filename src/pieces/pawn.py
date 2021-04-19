from pieces.base_piece import Piece


class Pawn(Piece):
	def __init__(self, color, pos):
		super().__init__(name="pawn", color=color, pos=pos)
		self.direction = 1 if self.color == "b" else -1
		self.base_row = 1 if self.color == "b" else 6
	
	def pawn_get_moves(self, board: list) -> list:
		cells = [
			cell for cell in
			filter(
				lambda x: x.row == self.row * self.direction and abs(x.col - self.col) < 2,
				board
			)
		]
		return cells
