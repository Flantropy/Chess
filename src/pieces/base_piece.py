from pygame import sprite, image, transform
from typing import Tuple, List
from src.classes.cell import Cell


class Piece(sprite.Sprite):
	def __init__(self, name, color, pos):
		super().__init__()
		self.name = name
		self.color = color
		self.grid_index = pos
		self.image = image.load("images/" + self.color + "_" + self.name + ".png")
		self.image = transform.scale(self.image, (32, 32))
		self.rect = self.image.get_rect()
		self.list_of_moves = []
		self.row, self.col = self.from_index_to_notation(self.grid_index)
	
	def __str__(self):
		return f"{self.name}:{self.grid_index} at row={self.row}, col={self.col}"
	
	def get_moves_list(self, board: List[Cell]) -> List[int]:
		...
	
	@staticmethod
	def from_index_to_notation(index: int) -> Tuple[int, int]:
		row = index // 8
		col = index % 8
		return row, col
	
	@property
	def grid_index(self) -> int:
		return self.__grid_index
	
	@grid_index.setter
	def grid_index(self, value: int):
		self.__grid_index = value
		self.row, self.col = self.from_index_to_notation(value)
	
	def on_row(self, row: int) -> bool:
		return True if self.row == row else False
	
	def on_col(self, col: int) -> bool:
		return True if self.col == col else False
	
	def get_bishop_moves(self, board) -> List[int]:
		sudo_moves: List[int] = [cell.index for cell in filter(lambda x: abs(x.row - self.row) - abs(x.col - self.col) == 0, board)]
		return sudo_moves
	
	def get_rook_moves(self, board) -> List[int]:
		sudo_moves: List[int] = [cell.index for cell in filter(self.rook_filter, board)]
		return sudo_moves
	
	def rook_filter(self, cell: Cell) -> bool:
		if self.on_col(cell.col) or self.on_row(cell.row):
			return True
		
		
		
	# def awesome_filter(self, sudo_moves: List[Cell]) -> List[int]:
	# 	# TODO add captures support
	# 	denied = []
	# 	for move in sudo_moves:
	# 		if move.piece:
	# 			if move.row > self.row:
	# 				for row in range(move.row, 8):
	# 					denied.append(row * 8 + self.col)
	# 			elif move.row < self.row:
	# 				for row in range(move.row):
	# 					denied.append(row * 8 + self.col)
	# 			if move.col > self.col:
	# 				for col in range(move.col, 8):
	# 					denied.append(col + self.row * 8)
	# 			elif move.col < self.col:
	# 				for col in range(move.col):
	# 					denied.append(col + self.row * 8)
	# 	return [cell.index for cell in sudo_moves if cell.index not in denied]
