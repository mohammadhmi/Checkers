import pygame
from constants.colors import (
    BROWN,
    YELLOW,
    BLACK,
)
from constants.constants import (
    WIDTH,
    HEIGHT,
    SQUARE_SIZE,
    FPS,
    ACCURACY,
    WIN,
)
from checkers.game_logic import Game_Logic
from minimax.algorithm import minimax_algorithm

#
from winner_windows import *


# getting position of pieces by mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    ROW = y // SQUARE_SIZE
    COL = x // SQUARE_SIZE
    row = ROW
    col = COL
    return row, col


def main():
    run = True
    # for fps
    clock = pygame.time.Clock()
    game = Game_Logic(WIN)

    while run:
        clock.tick(FPS)

        # using AI
        if game.turn == YELLOW:
            # more depth means ai gets better but need more computation
            value, new_board = minimax_algorithm(
                game.get_board(), ACCURACY, YELLOW, game
            )
            # update board based of ai moves
            game.ai_move(new_board)

        # printing winner
        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            # closing game
            if event.type == pygame.QUIT:
                run = False
                # moving pieces by clicking on them
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            # creating window of the game
        # board.draw(WIN)
        # updating window
        # pygame.display.update()
        # updating via game class

        game.update()

    pygame.quit()


main()
