import pygame as pg
from res.constants import (
	FPS,
	DISPLAY_SIZE,
	BOARD_TOP_RIGHT,
	TEST_PIECES
)
from classes.board import Board
from classes.event_handler import EventHandler


class MainScene:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode(DISPLAY_SIZE)
		self.clock = pg.time.Clock()
		self.board = Board(pos=BOARD_TOP_RIGHT)
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
