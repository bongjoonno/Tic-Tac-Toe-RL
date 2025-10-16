from imports import choice, sleep
from tic_tac_toe_board import Board
from constants import EPSILON

#q-table function system

q_table = {}

epsilon = EPSILON

board = Board(q_table = q_table, epsilon = epsilon)

for _ in range(1_000_000):
    outcome = board.move('X')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table, epsilon = epsilon)
        continue
    
    outcome = board.move('X')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table, epsilon = epsilon)
        
    epsilon = max(0, epsilon*0.999)
    
    
print(len(q_table))
print(q_table)