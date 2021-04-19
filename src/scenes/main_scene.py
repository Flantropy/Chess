import pygame as pg
from res.constants import (
	FPS,
	DISPLAY_SIZE,
	BOARD_TOP_RIGHT
)
from classes.board import Board
from classes.event_handler import EventHandler
from src.pieces.pawn import Pawn
from src.pieces.rook import Rook
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight

BASE_PIECES = {
	(6, 0, "w"): Pawn, (7, 0, "w"): Rook,
	(6, 1, "w"): Pawn, (7, 1, "w"): Knight,
	(6, 2, "w"): Pawn, (7, 2, "w"): Bishop,
	(6, 3, "w"): Pawn, (7, 3, "w"): Queen,
	(6, 4, "w"): Pawn, (7, 4, "w"): King,
	(6, 5, "w"): Pawn, (7, 5, "w"): Bishop,
	(6, 6, "w"): Pawn, (7, 6, "w"): Knight,
	(6, 7, "w"): Pawn, (7, 7, "w"): Rook,
	
	(1, 0, "b"): Pawn, (0, 0, "b"): Rook,
	(1, 1, "b"): Pawn, (0, 1, "b"): Knight,
	(1, 2, "b"): Pawn, (0, 2, "b"): Bishop,
	(1, 3, "b"): Pawn, (0, 3, "b"): Queen,
	(1, 4, "b"): Pawn, (0, 4, "b"): King,
	(1, 5, "b"): Pawn, (0, 5, "b"): Bishop,
	(1, 6, "b"): Pawn, (0, 6, "b"): Knight,
	(1, 7, "b"): Pawn, (0, 7, "b"): Rook
}

TEST_PIECES = {
	(3, 5, "w"): Rook,
	(0, 3, "b"): Rook,
	
	(1, 1, "b"): Bishop,
	(6, 6, "w"): Bishop,
	
	(2, 2, "w"): Queen
}


class MainScene:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode(DISPLAY_SIZE)
		self.clock = pg.time.Clock()
		self.board = Board(pos=BOARD_TOP_RIGHT, pieces=TEST_PIECES)
		self.event_handler = EventHandler()
		self.board_layer = pg.sprite.Group()
		for cell in self.board.grid:
			self.board_layer.add(cell)
		
	def run(self):
		while True:
			#  HANDLE EVENTS
			self.event_handler.handle_events(self.board)
			
			# UPDATE AND RENDER
			self.board_layer.update()
			self.board_layer.draw(self.display)
			pg.display.update()
			
			# TICK
			self.clock.tick(FPS)
