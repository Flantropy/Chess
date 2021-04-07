from pieces.base_piece import Piece


class King(Piece):
	def __init__(self, color, pos):
		super().__init__(name="king", color=color, pos=pos)
