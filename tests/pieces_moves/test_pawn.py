from tests.pieces_moves.base import *
from src.pieces.pawn import Pawn


@fixture
def board():
	pieces = {
		(1, 0, "tr_pos"): Pawn
	}
	new_board = Board(pieces=pieces)
	return new_board


def test_pawn_move_up(board):
	result = board.grid[1][0].move((2, 0))  # (row, col)
	assert result == True


def test_pawn_move_from_base_row(board):
	result = board.grid[1][0].move((3, 0))  # (row, col)
	assert result == True


def test_pawn_move_backwards(board):
	result = board.grid[1][0].move((0, 0))  # (row, col)
	assert result == False


def test_pawn_move_too_long(board):
	result = board.grid[1][0].move((4, 0))  # (row, col)
	assert result == False


def test_pawn_move_from_base_over_piece():
	pieces = {
		(1, 0, "tr_pos"): Pawn,
		(2, 0, "b"): Pawn
	}
	new_board = Board(pieces=pieces)
	result = new_board.grid[1][0].move((3, 0))  # (row, col)
	assert result == False


def test_pawn_move_left(board):
	result = board.grid[1][0].move((0, 0))  # (row, col)
	assert result == False


def test_pawn_capture():
	pieces = {
		(1, 1, "tr_pos"): Pawn,
		(2, 2, "b"): Pawn
	}
	new_board = Board(pieces=pieces)
	result = new_board.grid[1][1].move((2, 2))  # (row, col)
	assert result == True


def test_pawn_capture_backwards():
	pieces = {
		(1, 1, "tr_pos"): Pawn,
		(0, 0, "b"): Pawn
	}
	new_board = Board(pieces=pieces)
	result = new_board.grid[1][1].move((2, 2))  # (row, col)
	assert result == False

