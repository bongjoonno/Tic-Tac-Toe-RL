from tic_tac_toe_board import Board
from imports import choice

def random_move(board: Board, symbol, q_table):
    y, x = choice(list(board.available_boxes))
    q_table[board.make_fen()] = 0
    outcome = board.move(y, x, symbol)
    q_table[board.make_fen()] = 0
    
    return board, q_table, outcome