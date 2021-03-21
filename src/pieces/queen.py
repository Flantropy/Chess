from pieces.base_piece import BasePiece


class Queen(BasePiece):
	def __init__(self, layer, pos, color):
		super(Queen, self).__init__(layer=layer, pos=pos, name="queen", color=color)
