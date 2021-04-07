from pieces.base_piece import Piece


class Queen(Piece):
	def __init__(self, color, pos):
		super().__init__(name="queen", color=color, pos=pos)
