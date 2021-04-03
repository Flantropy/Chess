from pieces.base_piece import Piece


class Knight(Piece):
	def __init__(self, position=(0, 0), color="w", coordinates=(0, 0)):
		super().__init__(name="knight", position=position, color=color, coordinates=coordinates)
