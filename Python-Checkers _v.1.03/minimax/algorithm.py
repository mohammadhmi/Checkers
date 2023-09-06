import pygame
from copy import deepcopy
from constants.colors import (
    BROWN,
    YELLOW,
    BLACK,
    GREEN,
)
from constants.constants import (
    DELAY,
    RADIUS,
    THICKNESS,
    SHOW_MOVES,
)

x = []
y = x


# position is a board object that represents current state of the game
# max_player is for are we max the score or min the score if true means we max
def minimax_algorithm(position, depth, max_player, game):
    # returning the evaluation if we dont have a winner or we are in depth 0
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        # means we dont have any score so set it to -infinity
        maxEval = float("-inf")
        best_move = None
        for move in get_all_moves(position, YELLOW, game):
            # recursive for going down of depth to evaluate nodes until reaches end and then back
            # [0] is for only return the path
            evaluation = minimax_algorithm(move, depth - 1, False, game)[0]
            # check if is it better that we already have?
            maxEval = max(maxEval, evaluation)
            # if this move is the best move store it
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move

    else:
        # means we dont have any score so set it to infinity
        minEval = float("inf")
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            # recursive for going down of depth to evaluate nodes until reaches end and then back
            # [0] is for only return the path
            evaluation = minimax_algorithm(move, depth - 1, True, game)[0]
            # check if is it better that we already have?
            minEval = min(minEval, evaluation)
            # if this move is the best move store it
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    # move piece to 0 and 1 row column
    board.move(piece, move[0], move[1])
    # if we jumped over a piece
    if skip:
        board.remove(skip)
    return board


# get all moves from the current position
def get_all_moves(board, color, game):
    moves = [board]
    # loop over all pieces with same color and get all valid moves for them
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # using draw_moves to visualize all moves for AI
            if SHOW_MOVES:
                draw_moves(game, board, piece)
            # taking a copy of board for running algorithm
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            # simulate the new board if we make this move the new board look like this
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


# drawing every move then make a decision to move to best position
def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, GREEN, (piece.x, piece.y), RADIUS, THICKNESS)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()

    # delay for moves
    pygame.time.delay(DELAY)
