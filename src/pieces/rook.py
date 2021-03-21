from pieces.base_piece import BasePiece


class Rook(BasePiece):
	def __init__(self, layer, pos, color):
		super(Rook, self).__init__(layer=layer, pos=pos, name="rook", color=color)
