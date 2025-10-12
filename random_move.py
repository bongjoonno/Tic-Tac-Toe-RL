from tic_tac_toe_board import Board
from imports import choice

def random_move(board: Board, symbol):
    y, x = choice(list(board.available_boxes))
    outcome = board.move(y, x, symbol)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        print(board.display_board())
        board = Board()
    
    return board