import chess
import pygame as pg
from chess import Board, Move
from pygame.locals import *

from classes.cell import Cell
from classes.gui_board import GUIBoard


class EventHandler:
    def __init__(self, board: Board, gui_board: GUIBoard):
        self.board = board
        self.gui_board = gui_board
    
    def handle_events(self) -> None:
        for event in pg.event.get():
            self.check_mouse(event)
            self.check_quit(event)
    
    @staticmethod
    def check_quit(event) -> None:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            quit()
    
    def check_mouse(self, event: pg.event.Event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            for cell in self.gui_board.sprites:
                if cell.rect.collidepoint(x, y):
                    if self.gui_board.selected_cell and cell != self.gui_board.selected_cell:
                        self.make_move(to_cell=cell)
                    else:
                        self.gui_board.selected_cell = cell
                        cell.selected = True
    
    def make_move(self, to_cell: Cell):
        promotion = "q" if self.is_promotion(to_cell) else ""
        uci_move = f"{self.gui_board.selected_cell}{to_cell}{promotion}"
        move = Move.from_uci(uci_move)
        if self.board.is_legal(move):
            self.board.push(move)
        self.gui_board.selected_cell.selected = False
        self.gui_board.selected_cell = None
        self.gui_board.update_piece_positions(self.board.board_fen())
    
    def is_promotion(self, to_cell: Cell) -> bool:
        square = self.gui_board.selected_cell.__str__()
        if self.board.piece_type_at(chess.parse_square(square)) == chess.PAWN:
            if to_cell.rank == "8" or to_cell.rank == "1":
                return True
