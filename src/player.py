from constants import PIECES
from pieces.pawn import Pawn
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook


class Player:
	def __init__(self, side, layer, board):
		self.pieces = PIECES
		self.pieces_obj = {
			"Pawn": Pawn,
			"King": King,
			"Queen": Queen,
			"Bishop": Bishop,
			"Knight": Knight,
			"Rook": Rook
		}
		self.side = side
		self.active = False
		self.add_pieces_on_board(layer, board)
	
	def add_pieces_on_board(self, layer, board):
		for pos, piece in self.pieces.items():
			if self.side == "b":
				pos = pos[0], abs(pos[1] - 9)
			piece_obj = self.pieces_obj[piece](
				layer=layer,
				pos=self._find_pos(board, pos),
				color=self.side
			)
			board.add_piece(pos=pos, piece=piece_obj)
			layer.add(piece_obj)
	
	@staticmethod
	def _find_pos(board, pos):
		for grid in board.grid:
			if (grid.col, grid.row) == pos:
				return grid.rect.center
