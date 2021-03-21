from pieces.base_piece import BasePiece


class Pawn(BasePiece):
	def __init__(self, layer, pos, color):
		
		super(Pawn, self).__init__(layer=layer, pos=pos, name="pawn", color=color)
