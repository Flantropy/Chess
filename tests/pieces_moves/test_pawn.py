from chess import Move
import chess


def test_forward_move(create_board):
    board = create_board
    assert Move.from_uci('e2e4') in list(board.legal_moves)


def test_board_fen_changes(create_board):
    board = create_board
    my_move = Move.from_uci("e2e4")
    board.push(my_move)
    assert board.fen() == "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"


def test_promotion(create_board):
    board = create_board
    board.set_fen("8/5K1P/8/3k4/8/8/8/8 w - - 0 1")
    board.push(Move.from_uci("h7h8q"))
    assert board.piece_type_at(chess.H8) == chess.QUEEN
