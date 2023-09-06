import pygame

# Board
WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# circle of show moves
RADIUS = 50
THICKNESS = 8

#
RADIUS_PIECE = 15

# Victory picture
VICTORY = "images/victory-resize.png"

# Delay time
SHOW_MOVES = False
DELAY = 10


# Game rules
PIECE = 12
KING = 0
FPS = 60
ACCURACY = 2
