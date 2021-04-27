"""
FEN notation is a common way to represent pieces on a chess board
If you not familiar with the way it works, you could visit this link:
https://www.dcode.fr/fen-chess-notation
or
https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
"""
from typing import List
from pieces import Piece, King, Queen, Rook, Bishop, Knight, Pawn

fen_map = dict(p=Pawn, n=Knight, b=Bishop, r=Rook, q=Queen, k=King)


def parse_fen(fen: str) -> List[Piece]:
	all_pieces = []
	index = 0
	fen = fen.split("/")
	for row in fen:
		for symbol in row:
			if symbol in "12345678":
				index += int(symbol)
			else:
				color = "w" if symbol.isupper() else "b"
				piece_class = fen_map[symbol.lower()]
				piece_instance = piece_class(color=color, pos=index)
				index += 1
				all_pieces.append(piece_instance)
	return all_pieces
