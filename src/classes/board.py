from res.constants import *
from res.ultracolors import WHITE, MEDIUM_WOOD
from classes.cell import Cell
from pieces.base_piece import Piece
from pygame.display import set_caption


class Board:
	def __init__(self, pos=(0, 0), pieces=None):
		self.pos_x, self.pos_y = pos
		self.pieces = pieces
		self.grid = []
		self.create()
		if self.pieces:
			self.fill()
		self.selected_piece = None
		self.white_to_move = True
	
	def create(self):
		for row in range(BOARD_H):
			for col in range(BOARD_W):
				color = WHITE if (row + col) % 2 == 0 else MEDIUM_WOOD
				self.grid.append(
					Cell(
						color=color,
						notation=(row, col),
						position_on_display=(col * CELL_W, row * CELL_H)
					)
				)
	
	def fill(self):
		for pos, piece in self.pieces.items():
			row, col, color = pos
			grid_index = row * 8 + col
			self.grid[grid_index].piece = piece(
				color=color,
				pos=grid_index
			)
		self.__update_all_moves()
	
	def clear_selection(self):
		for cell in self.grid:
			cell.selected = False
	
	def move(self, piece: Piece, end: int):
		if end in piece.list_of_moves:
			self.grid[end].piece, self.grid[piece.grid_index].piece, = piece, None
			self.grid[end].piece.grid_index = end
			self.selected_piece = None
			self.white_to_move = not self.white_to_move
			side = "White" if self.white_to_move else "Black"
			set_caption(f"Now is {side}'s move")
		else:
			print("not in list of moves")
			self.selected_piece = None
		self.clear_selection()
		self.__update_all_moves()
	
	def _add_selection(self, moves: list):
		for move in moves:
			if 0 <= move < 64:
				self.grid[move].selected = True
	
	def __update_all_moves(self):
		for cell in self.grid:
			if cell.piece:
				cell.piece.list_of_moves = cell.piece.get_moves_list(cell.piece.row, cell.piece.col, self.grid)
