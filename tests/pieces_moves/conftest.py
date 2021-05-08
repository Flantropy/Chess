import pytest
import chess


@pytest.fixture
def create_board():
    board = chess.Board()
    yield board
    board.reset()
