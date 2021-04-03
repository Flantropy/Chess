from pieces.base_piece import Piece


class Rook(Piece):
	def __init__(self, position=(0, 0), color="w", coordinates=(0, 0)):
		super().__init__(name="rook", position=position, color=color, coordinates=coordinates)
		self.move_offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
