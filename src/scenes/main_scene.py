import pygame as pg
import chess
from res.constants import (
	FPS,
	DISPLAY_SIZE
)
from classes.event_handler import EventHandler
from classes.gfx import GFX
from classes.gui_board import GUIBoard


class MainScene:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode(DISPLAY_SIZE)
		self.clock = pg.time.Clock()
		self.board = chess.Board()
		self.gfx = GFX()
		self.gui_board = GUIBoard(self.board)
		self.event_handler = EventHandler(board=self.board, gui_board=self.gui_board)
	
	def run(self) -> None:
		self.init_board()
		while True:
			self.event_handler.handle_events()
			self.gfx.update()
			self.gfx.render(self.display)
			pg.display.update()
			self.clock.tick(FPS)
	
	def init_board(self) -> None:
		self.gui_board.sprites = GUIBoard.get_cells()
		self.gui_board.update_piece_positions(self.board.board_fen())
		self.gfx.layer_0.add(self.gui_board.sprites)
