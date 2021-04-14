from pieces.base_piece import Piece


class Rook(Piece):
	def __init__(self, color, pos):
		super().__init__(name="rook", color=color, pos=pos)
	
	def get_moves_list(self, board):
		self.list_of_moves = []
		for cell in board:
			if cell.row == self.grid_index // 8 or cell.col == self.grid_index % 8:
				self.list_of_moves.append(cell.index)
		self.list_of_moves = set(self.list_of_moves)
		self.list_of_moves.remove(self.grid_index)
		
		for move in self.list_of_moves.copy():
			if board[move].piece and board[move].piece.color == self.color:
				self.list_of_moves.remove(move)
