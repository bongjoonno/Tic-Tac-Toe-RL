from imports import choice, sleep
from tic_tac_toe_board import Board
from constants import EPSILON

#q-table function system

q_table = {}

epsilon = 1

board = Board(q_table = q_table, epsilon = epsilon)

epochs = 100_000

for _ in range(epochs // 2):
    outcome = board.move('X', random = False)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table, epsilon = epsilon)
        epsilon = max(0, epsilon ** 0.999)
        continue
    
    outcome = board.move('O', random = True)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = q_table, epsilon = epsilon)
        epsilon = max(0, epsilon ** 0.999)
        
    
    
print(len(q_table))