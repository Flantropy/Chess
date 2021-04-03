from pieces.base_piece import Piece


class King(Piece):
	def __init__(self, position=(0, 0), color="tr_pos", coordinates=(0, 0)):
		super().__init__(name="king", position=position, color=color, coordinates=coordinates)
