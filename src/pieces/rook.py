from typing import List
from classes.cell import Cell
from pieces import Piece


class Rook(Piece):
	def __init__(self, color, pos):
		super().__init__(name="rook", color=color, pos=pos)
	
	def get_moves_list(self, board: List[Cell]) -> List[int]:
		sudo_moves = super().get_rook_moves(board)
		legal_moves = self.clean_up_moves(board, sudo_moves)
		return legal_moves
	
	def clean_up_moves(self, board: List[Cell], moves: List[int]) -> List[int]:
		denied = dict(up=7, down=0, right=7, left=0)
		pieces_colliding_with_moves = [board[move].piece for move in moves if board[move].piece]
		
		for piece in pieces_colliding_with_moves:
			row, col = piece.row, piece.col
			if self.row < row < denied['up']:
				denied['up'] = row if piece.color != self.color else row - 1
			if self.col < col < denied['right']:
				denied['right'] = col if piece.color != self.color else col - 1
			if self.row > row > denied['down']:
				denied['down'] = row if piece.color != self.color else row + 1
			if self.col > col > denied['left']:
				denied['left'] = col if piece.color != self.color else col + 1
		
		return [move for move in moves if
										move // 8 in range(denied["down"], denied["up"] + 1) and
										move % 8 in range(denied["left"], denied["right"] + 1)]
