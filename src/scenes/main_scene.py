import pygame as pg
from pygame.locals import *
from res.constants import *
from sys import exit
from src.board import Board
from src.pieces.pawn import Pawn
from src.pieces.rook import Rook
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight


pieces = {
	(6, 5, "w"): Bishop
}


class MainScene:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode(DISPLAY_SIZE)
		self.clock = pg.time.Clock()
		self.board = Board(pos=BOARD_TOP_RIGHT)
	
	def run(self):
		while True:
			# Handle events
			for event in pg.event.get():
				if event.type == QUIT:
					pg.quit()
					exit()
				if event.type == pg.MOUSEBUTTONDOWN:
					self.board.clear_selection()
					x, y = pg.mouse.get_pos()
					for cell in self.board.grid.flat:
						if cell.rect.collidepoint(x, y):
							cell.selected = True
							if cell.piece:
								cell.piece.get_moves_list(self.board.grid)
								for pos in cell.piece.list_of_moves:
									x, y = pos
									self.board.grid[x][y].selected = True
								
			# Update State
			for cell in self.board.grid.flat:
				cell.draw(self.display)
				cell.update()
				if cell.piece:
					cell.piece.draw(self.display)
			
			# Update Display
			pg.display.update()
			
			# Tick
			self.clock.tick(FPS)
