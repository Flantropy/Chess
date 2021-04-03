from pieces.base_piece import Piece


class Pawn(Piece):
	def __init__(self, position=(0, 0), color="tr_pos", coordinates=(0, 0)):
		super().__init__(name="pawn", position=position, color=color, coordinates=coordinates)
		self.direction = 1 if self.color == "tr_pos" else -1
		self.base_row = 1 if self.color == "tr_pos" else 6
	#
	# def get_moves_list(self, board):
	# 	if not board[self.row + self.direction][self.col].piece:
	# 		self.list_of_moves.append(self.row + self.direction, self.col)
