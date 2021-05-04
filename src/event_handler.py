import pygame as pg
from pygame.locals import *


class EventHandler:
	def __init__(self, board, gui_board):
		self.board = board
		self.gui_board = gui_board
	
	def handle_events(self) -> None:
		for event in pg.event.get():
			self.check_mouse(event)
			self.check_quit(event)
	
	@staticmethod
	def check_quit(event) -> None:
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pg.quit()
			quit()
	
	def check_mouse(self, event: pg.event.Event) -> None:
		if event.type == MOUSEBUTTONDOWN:
			x, y = pg.mouse.get_pos()
			for cell in self.gui_board.sprites:
				if cell.rect.collidepoint(x, y):
					print(f"file = {cell.file} rank = {cell.rank}")
