from pieces.base_piece import Piece


class Pawn(Piece):
	def __init__(self, color, pos):
		super().__init__(name="pawn", color=color, pos=pos)
		self.direction = 1 if self.color == "b" else -1
		self.base_row = 1 if self.color == "b" else 6
		
	def get_moves_list(self, board):
		self.list_of_moves = []
		self.look_up_rank(board)
		
	def look_up_rank(self, board):
		"""
		REFACTOR!!!
		"""
		move1 = board[self.grid_index + self.direction * 8 - 1].index
		move2 = board[self.grid_index + self.direction * 8].index
		move3 = board[self.grid_index + self.direction * 8 + 1].index
		moves = [move1, move2, move3]
		
		if self.grid_index // 8 == self.base_row:
			move4 = board[self.grid_index + self.direction * 8 * 2].index
			if not board[move4].piece:
				moves.append(move4)
				
		if not board[move1].piece:
			moves.remove(move1)
		if board[move2].piece:
			moves.remove(move2)
		if not board[move3].piece:
			moves.remove(move3)
		for move in moves:
			self.list_of_moves.append(move)
		
		for move in moves:
			if board[move].piece and board[move].piece.color == self.color:
				self.list_of_moves.remove(move)
