from pieces.base_piece import Piece


class Bishop(Piece):
	def __init__(self, color, pos):
		super().__init__(name="bishop", color=color, pos=pos)
		
	def get_moves_list(self, board):
		self.list_of_moves = []
		for cell in board:
			if self.grid_index % 9 == cell.index % 9 or self.grid_index % 7 == cell.index % 7:
				if cell.row - cell.col == self.grid_index//8 - self.grid_index % 8:
					self.list_of_moves.append(cell.index)
				elif cell.col + cell.row == self.grid_index % 8 + self.grid_index//8:
					self.list_of_moves.append(cell.index)
		self.list_of_moves = set(self.list_of_moves)
		self.list_of_moves.remove(self.grid_index)
