import pygame as pg
from pygame.locals import *


class EventHandler:
	def __init__(self):
		pass
	
	def handle_events(self, board):
		for event in pg.event.get():
			self.check_quit(event)
			self.check_mouse(event, board)
	
	@staticmethod
	def check_quit(event):
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pg.quit()
			quit()
	
	@staticmethod
	def check_mouse(event, board):
		if event.type == MOUSEBUTTONDOWN:
			board.clear_selection()
			x, y = pg.mouse.get_pos()
			for cell in board.grid:
				if cell.rect.collidepoint(x, y):
					if cell.piece:
						board.add_selection(cell.piece.list_of_moves)
