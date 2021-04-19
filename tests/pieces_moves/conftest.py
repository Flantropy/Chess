import pytest
from src.pieces.knight import Knight
from src.classes.board import Board


@pytest.fixture
def create_board() -> Board:
	new_board = Board()
	return new_board


@pytest.fixture
def bar():
	pass


@pytest.fixture
def setup():
	pieces = {
		(2, 2, "w"): Knight
	}
	new_board = Board(pieces=pieces)
	knight = new_board.grid[18].piece
	knight.list_of_moves = knight.get_moves_list(knight.row, knight.col, new_board.grid)
	return {"piece": knight}
