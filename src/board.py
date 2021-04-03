from res.constants import *
from src.pieces.base_piece import Piece
from src.pieces.pawn import Pawn
from src.cell import Cell
from res.ultracolors import WHITE, MEDIUM_WOOD
import numpy


class Board:
	def __init__(self, pos=(0, 0), pieces=BASE_PIECES):
		self.w, self.h = pos
		self.pieces = pieces
		self.grid = numpy.empty((BOARD_W, BOARD_H), dtype=Cell)
		self.create()
		self.fill()
		self.update_list_of_moves_for_all_pieces()
	
	def fill(self):
		for pos, piece in self.pieces.items():
			row, col, color = pos
			if self.grid[row][col].piece:
				print("override")
			self.grid[row][col].piece = piece(
				position=(row, col), color=color,
				coordinates=self.grid[row][col].get_center()
			)
	
	def create(self):
		for i, cell in numpy.ndenumerate(self.grid):
			row, col = i
			color = WHITE if (row + col) % 2 == 0 else MEDIUM_WOOD
			self.grid[i] = Cell(pos=(row * CELL_W + self.w, col * CELL_H + self.h), color=color)
	
	def update_list_of_moves_for_all_pieces(self):
		for cell in self.grid.flat:
			if cell.piece:
				cell.piece.get_moves_list(self.grid)
	
	def clear_selection(self):
		for cell in self.grid.flat:
			cell.selected = False
