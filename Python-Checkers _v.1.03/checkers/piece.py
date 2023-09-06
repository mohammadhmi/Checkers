from constants.colors import BROWN, YELLOW, GREY, BLACK
from constants.constants import SQUARE_SIZE
from constants.crown import CROWN
import pygame


class Piece:
    BORDER = 2
    PADDING = 15

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # initialize king piece
        self.king = False
        self.x = 0
        self.y = 0
        self.position_calculate()

    def position_calculate(self):
        # middle of the square when we defining the position
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # making piece king
    def make_king(self):
        self.king = True

    # creating pieces
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            # setting the crown picture in middle of piece
            win.blit(
                CROWN,
                (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2),
            )

    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.position_calculate()

    # for debugging
    def __repr__(self):
        return str(self.color)
