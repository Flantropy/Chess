from pieces.base_piece import Piece
from numpy.core.fromnumeric import diagonal
from numpy import fliplr


class Bishop(Piece):
	def __init__(self, position=(0, 0), color="tr_pos", coordinates=(0, 0)):
		super().__init__(name="bishop", position=position, color=color, coordinates=coordinates)
		# self.move_offsets = ((1, 1), (-1, -1), (1, -1), (-1, 1))
	
	def get_moves_list(self, board):
		print(f"col = {self.col} row = {self.row}")
		new_arr = []
		co2 = 7 - (self.row + self.col)
		to_select = diagonal(fliplr(board), offset=co2)
		new_arr.extend(to_select)
		custom_offset = -self.col if self.row < 4 else 7-self.col
		new_arr.extend(diagonal(board, offset=custom_offset))
		for cell in new_arr:
			self.list_of_moves.append((cell.row, cell.col))
