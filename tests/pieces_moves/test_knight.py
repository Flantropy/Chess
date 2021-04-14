from pytest import fixture
from src.pieces.knight import Knight
from src.classes.board import Board


@fixture
def setup():
	pieces = {
		(2, 2, "w"): Knight
	}
	new_board = Board(pieces=pieces)
	knight = new_board.grid[18].piece
	knight.get_moves_list(new_board.grid)
	return {"piece": knight}


def test_knight_moves(setup):
	piece = setup["piece"]
	valid_moves = {1, 3, 8, 12, 24, 28, 33, 35}
	wrong_moves = set(range(64)).difference(valid_moves)
	for move in valid_moves:
		assert move in piece.list_of_moves
	for i in wrong_moves:
		assert i not in piece.list_of_moves
