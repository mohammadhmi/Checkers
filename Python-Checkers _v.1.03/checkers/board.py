import pygame
from constants.colors import (
    LIGHT_BROWN,
    BROWN,
    YELLOW,
    BLACK,
)
from constants.constants import SQUARE_SIZE, COLS, KING, PIECE, ROWS
from .piece import Piece


# handling the state of the game
class Board:
    def __init__(self):
        self.board = []
        # number of pieces for each player
        self.black_left = self.yellow_left = PIECE
        # king pieces
        self.black_kings = self.yellow_kings = KING
        # initialize the board

        self.create_board()

    def draw_squares(self, win):
        win.fill(LIGHT_BROWN)
        for row in range(ROWS):
            # if row = 0, 2, 4... use brown else use light brown
            # 0, 2, 4 % 2 = 0
            for col in range(row % 2, COLS, 2):
                # in pygame 0 position is top left corner
                pygame.draw.rect(
                    win,
                    BROWN,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    # evaluate the score (AI)
    def evaluate(self):
        # 1 ...
        # return self.yellow_left - self.black_left
        # 2 a better solution
        # handling score when we have kings
        return (
            self.yellow_left
            - self.black_left
            + (self.yellow_kings * 0.5 - self.black_kings * 0.5)
        )

    # visualizing the pieces
    # by color
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        # moving pieces from self.board[piece.row][piece.column]
        # to self.board[row][column] (swap)
        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )
        piece.move_piece(row, col)

        # making the piece king if its in the right position
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == YELLOW:
                self.yellow_kings += 1
            else:
                self.black_kings += 1

    # getting piece object for pass it to move function
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            # list for each row
            self.board.append([])
            for col in range(COLS):
                # drawing the pieces on board
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, YELLOW))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # removing pieces that we jumped from
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_left -= 1
                else:
                    self.yellow_left -= 1

    def winner(self):
        if self.black_left <= 0:
            return YELLOW
        elif self.yellow_left <= 0:
            return BLACK

        return None

    # all of the valid moves that a piece could move to
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLACK or piece.king:
            # starting at a row above that we selected piece
            # how far we can go (at max 3 rows or at min 1 row)
            # -1 is for move up when increment or decrement the for loop
            # left is for where we start our columns and tracks the left position
            # traverse right or left return dictionary
            moves.update(
                self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left)
            )
            moves.update(
                self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right)
            )
        if piece.color == YELLOW or piece.king:
            # row + 1 is for we going down this time
            moves.update(
                self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left)
            )
            moves.update(
                self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right)
            )

        return moves

    # for traverse to left or right
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        # what row we in and what are the steps
        for r in range(start, stop, step):
            if left < 0:
                break

            # tracking the left of what piece that we selected
            current = self.board[r][left]
            # if we have a empty square
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    # for removing the pieces that we jumped over
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, left - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, left + 1, skipped=last
                        )
                    )
                break
            # if the piece that we trying to move is equal to same color az we have then block and
            # we cant jump on it
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        # what row we in and what are the steps
        for r in range(start, stop, step):
            if right >= COLS:
                break

            # tracking the left of what piece that we selected
            current = self.board[r][right]
            # if we have a empty square
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    # for removing the pieces that we jumped over
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, right - 1, skipped=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, right + 1, skipped=last
                        )
                    )
                break
            # if the piece that we trying to move is equal to same color az we have then block and
            # we cant jump on it
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
