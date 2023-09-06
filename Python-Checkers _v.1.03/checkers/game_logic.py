import pygame

#
from tkinter import *
from tkinter import ttk
from constants.colors import BROWN, YELLOW, BLUE, BLACK
from constants.constants import SQUARE_SIZE, RADIUS_PIECE
from checkers.board import Board

#
from winner_windows import winner_black, winner_yellow
from winner_windows.winner_black import winner_window_black
from winner_windows.winner_yellow import winner_window_yellow


class Game_Logic:
    def __init__(self, win):
        self._init()
        self.win = win

    # initializing the game and its private
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    # updates the window
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def winner(self):
        #
        #
        if self.board.winner() == YELLOW:
            winner_window_yellow()
        elif self.board.winner() == BLACK:
            winner_window_black()

    # if some piece is selected move it
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            # if select was not completed call select again on something else
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        # if selection by use is valid return true
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        # if piece that we selected and gonna move in position that is not in another piece position move it
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            # if we have a enemy piece in our valid moves
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                self.win,
                BLUE,
                (
                    col * SQUARE_SIZE + SQUARE_SIZE // 2,
                    row * SQUARE_SIZE + SQUARE_SIZE // 2,
                ),
                RADIUS_PIECE,
            )

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = YELLOW
        else:
            self.turn = BLACK

    # for passing the turn to ai
    def ai_move(self, board):
        self.board = board
        self.change_turn()

    # return board
    def get_board(self):
        return self.board
