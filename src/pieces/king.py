from pieces.base_piece import BasePiece


class King(BasePiece):
	def __init__(self, layer, pos, color):
		super(King, self).__init__(layer=layer, pos=pos, name="king", color=color)
