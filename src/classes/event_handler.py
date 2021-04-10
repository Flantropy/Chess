import pygame as pg
from pygame.locals import *
from pygame.display import set_caption


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
		color_to_move = "w" if board.white_to_move else "b"
		if event.type == MOUSEBUTTONDOWN:
			x, y = pg.mouse.get_pos()
			for cell in board.grid:
				if cell.rect.collidepoint(x, y):
					if board.selected_piece:
						board.move(board.selected_piece, cell.index)
					elif cell.piece and cell.piece.color == color_to_move:
						board.selected_piece = cell.piece
						cell.piece.get_moves_list(board.grid)
						board.add_selection(cell.piece.list_of_moves)
						set_caption(f"{board.selected_piece}")
						print(cell.piece)
