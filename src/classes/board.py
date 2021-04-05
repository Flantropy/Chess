from res.constants import *
from res.ultracolors import WHITE, MEDIUM_WOOD, PINK_1
from classes.cell import Cell
from pieces.base_piece import Piece


class Board:
	def __init__(self, pos=(0, 0), pieces=BASE_PIECES):
		self.pos_x, self.pos_y = pos
		self.pieces = pieces
		self.grid = []
		self.create()
		self.fill()
		self.update_list_of_moves_for_all_pieces()
		self.selected_piece = None
	
	def create(self):
		for row in range(BOARD_H):
			for col in range(BOARD_W):
				color = WHITE if (row + col) % 2 == 0 else MEDIUM_WOOD
				self.grid.append(
					Cell(
						color=color,
						notation=(row, col),
						position_on_display=(col * CELL_W, row * CELL_H)  # REVIEW
					)
				)
	
	def fill(self):
		for pos, piece in self.pieces.items():
			row, col, color = pos
			grid_index = notation_to_index(row, col)
			self.grid[grid_index].piece = piece(
				color=color,
				position=(row, col),
				coordinates=self.grid[grid_index].rect.center
			)
	
	def update_list_of_moves_for_all_pieces(self):
		for cell in self.grid:
			if cell.piece:
				cell.piece.get_moves_list(self.grid)
	
	def clear_selection(self):
		for cell in self.grid:
			cell.selected = False
	
	def move(self, piece: Piece, end: Cell):
		end_row, end_col = end.row, end.col
		end_pos = (end_row, end_col)
		if end_pos in piece.list_of_moves:
			print("moveee!!!")
	
	def add_selection(self, moves: list):
		for move in moves:
			row, col = move
			grid_index = notation_to_index(row, col)
			self.grid[grid_index].selected = True
			# print(row, col)
