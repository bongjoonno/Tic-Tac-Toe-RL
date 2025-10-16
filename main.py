from imports import choice, sleep
from tic_tac_toe_board import Board
from random_move import random_move
#q-table function system

q_table = {}
board = Board(q_table = q_table)

for _ in range(1_000_000):
    board.calculate_possible_moves_fen()
    
    board, q_table, outcome = random_move(board, 'X', q_table)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table)
        continue
    
    board.calculate_possible_moves_fen()
    
    board, q_table, outcome = random_move(board, 'O', q_table)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table)
    
    
print(len(q_table))
print(q_table)

# make policy function with available moves