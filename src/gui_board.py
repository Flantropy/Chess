import chess
from typing import List
from cell import Cell
import pygame
from res.constants import DIR_IMAGES, CELL_SIZE


class GUIBoard:
	pawn_img = pygame.transform.scale(pygame.image.load(DIR_IMAGES + r"\w_pawn.png"), CELL_SIZE)
	
	def __init__(self, board: chess.Board):
		self.board = board
		self.__sprites = []
	
	@property
	def sprites(self):
		return self.__sprites
	
	@sprites.setter
	def sprites(self, value: List[Cell]):
		self.__sprites = value
	
	@classmethod
	def get_cells(cls, fen: str) -> List[Cell]:
		cells = []
		for rank in chess.RANK_NAMES:
			for file in chess.FILE_NAMES:
				cells.append(Cell(rank=rank, file=file, piece=cls.pawn_img))
		
		return cells
