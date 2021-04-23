from pieces.base_piece import Piece
from src.classes.cell import Cell


class Pawn(Piece):
	def __init__(self, color, pos):
		super().__init__(name="pawn", color=color, pos=pos)
		self.direction = 1 if self.color == "b" else -1
		self.base_row = 1 if self.color == "b" else 6
	
	def get_moves_list(self, board: list) -> list:
		cells = [cell.index for cell in filter(self.move_filter, board)]
		return cells
	
	def move_filter(self, cell: Cell) -> bool:
		"""
		En-passant moves doesn't available
		"""
		if cell.piece and (cell.piece.color == self.color or self.on_col(cell.col)):
			return False
		if cell.row == self.row + self.direction and self.on_col(cell.col):
			return True  # regular moves
		if self.row == self.base_row and self.on_col(cell.col) and cell.row == self.row + self.direction * 2:
			return True  # 2-x moves from base row
		if abs(cell.col - self.col) == 1 and cell.row == self.row + self.direction and cell.piece and cell.piece.color != self.color:
			return True  # captures
