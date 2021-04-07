from pieces.base_piece import Piece


class Knight(Piece):
	def __init__(self, color, pos):
		super().__init__(name="knight", color=color, pos=pos)
	
	def get_moves_list(self, board):
		self.list_of_moves = []
		i = self.grid_index
		sudo_moves = [i + 10, i + 17, i - 6, i - 15, i - 10, i - 17, i + 6, i + 15]
		for move in sudo_moves:
			if 0 > move > 63:
				sudo_moves.remove(move)
		self.list_of_moves.extend(sudo_moves)
