from tests.pieces_moves.base import *
from src.pieces.rook import Rook


def test_rook_speak():
	assert str(Rook()) == "rook"
