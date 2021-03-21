from pieces.base_piece import BasePiece


class Knight(BasePiece):
	def __init__(self, layer, pos, color):
		super(Knight, self).__init__(layer=layer, pos=pos, name="knight", color=color)
