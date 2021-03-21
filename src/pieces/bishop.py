from pieces.base_piece import BasePiece


class Bishop(BasePiece):
	def __init__(self, layer, pos, color):
		super(Bishop, self).__init__(layer=layer, pos=pos, name="bishop", color=color)
