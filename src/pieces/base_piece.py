from pygame import sprite, image, transform
from typing import Tuple


class Piece(sprite.Sprite):
	def __init__(self, name, color, pos):
		super().__init__()
		self.name = name
		self.color = color
		self.grid_index = pos
		self.image = image.load("C:\\PycharmProjects\\PyGame\\src\\images/" + self.color + "_" + self.name + ".png")
		self.image = transform.scale(self.image, (32, 32))
		self.rect = self.image.get_rect()
		self.list_of_moves = []
		self.row, self.col = self.from_index_to_notation(self.grid_index)
	
	def __str__(self):
		return f"{self.name}:{self.grid_index} at row={self.row}, col={self.col}"
	
	@staticmethod
	def get_moves_list(row: int, col: int, board: list) -> list:
		pass
			
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
