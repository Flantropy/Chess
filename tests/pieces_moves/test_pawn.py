from chess import Move
import chess


def test_forward_move(create_board):
    b = create_board
    assert Move.from_uci('e2e4') in list(b.legal_moves)


def test_board_fen_changes(create_board):
    board = chess.Board()
    my_move = Move.from_uci("e2e4")
    board.push(my_move)
    assert board.fen() == "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
