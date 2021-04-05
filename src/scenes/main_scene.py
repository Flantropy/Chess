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
		self.board = Board(pos=BOARD_TOP_RIGHT, pieces=TEST_PIECES)
		self.event_handler = EventHandler()
		self.layer_cells = pg.sprite.Group()
		self.layer_pieces = pg.sprite.Group()
		self.layers = [
			self.layer_cells,
			self.layer_pieces
		]
		self.update_layers()
	
	def update(self):
		for layer in self.layers:
			layer.update()
	
	def render(self):
		for layer in self.layers:
			layer.draw(self.display)
		pg.display.update()
	
	def update_layers(self):
		"""
		Has to be called before using self.layers
		"""
		for cell in self.board.grid:
			self.layer_cells.add(cell)
			if cell.piece:
				self.layer_pieces.add(cell.piece)
	
	def run(self):
		while True:
			#  HANDLE EVENTS
			self.event_handler.handle_events(self.board)
			
			# UPDATE AND RENDER
			self.update()
			self.render()
			
			# TICK
			self.clock.tick(FPS)
