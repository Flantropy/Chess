"""
FEN notation is a common way to represent pieces on a chess board
If you not familiar with the way it works, you could visit this link:
https://www.dcode.fr/fen-chess-notation
or
https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
"""
from src import pieces
from typing import List

fen_map = {
	"r": pieces.Rook,
	"n": pieces.Knight,
	"b": pieces.Bishop,
	"q": pieces.Queen,
	"k": pieces.King,
	"p": pieces.Pawn
}


def parse_fen(fen: str) -> List[pieces.Piece]:
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
