from imports import choice, sleep
from tic_tac_toe_board import Board

#q-table function system

q_table = {}
board = Board(q_table = q_table)

for _ in range(1_000_000):
    outcome = board.move('X')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table)
        continue
    
    outcome = board.move('X')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table)
        
    epsilon = max(0, epsilon*0.999)
    
    
print(len(q_table))
print(q_table)

# make policy function with available moves