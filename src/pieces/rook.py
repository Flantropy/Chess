from pieces.base_piece import Piece


class Rook(Piece):
	def __init__(self, position=(0, 0), color="w", coordinates=(0, 0)):
		super().__init__(name="rook", position=position, color=color, coordinates=coordinates)
	
	def get_moves_list(self, board):
		super().get_moves_list(board)
		
		for cell in board[self.grid_index-8::-8]:
			if not super().add_move(cell.index, board):
				break
	
		# for i in range(self.grid_index, 64, 8):
		# 	self.list_of_moves.append(i)
		# for i in range(self.grid_index, self.row * 8 + 8, 1):
		# 	self.list_of_moves.append(i)
		# for i in range(self.grid_index, self.row * 8 - 1, -1):
		# 	self.list_of_moves.append(i)
