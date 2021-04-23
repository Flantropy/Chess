from pieces.base_piece import Piece
from typing import List
from classes.cell import Cell


class King(Piece):
	def __init__(self, color, pos):
		super().__init__(name="king", color=color, pos=pos)
	
	def get_moves_list(self, board: List[Cell]) -> List[int]:
		return [cell.row * 8 + cell.col for cell in board if self.move_filter(cell)]
	
	def move_filter(self, cell: Cell) -> bool:
		if cell.piece and cell.piece.color == self.color:
			return False
		if abs(self.row - cell.row) <= 1 and abs(self.col - cell.col) <= 1 and cell.index != self.grid_index:
			return True
