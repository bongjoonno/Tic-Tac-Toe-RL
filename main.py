from imports import choice, sleep
from tic_tac_toe_board import Board
from random_move import random_move
#q-table function system

board = Board()
q_table = {}

for _ in range(10_000_000):
    board, q_table, outcome = random_move(board, 'X', q_table)
    board.display_board()
    sleep(2)
    print(f'{board.rewards}\n')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board()
        continue
        


    board, q_table, outcome = random_move(board, 'O', q_table)
    board.display_board()
    sleep(2)
    print(f'{board.rewards}\n')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board()
    


print(len(q_table))

#for pos, val in q_table.items():
    #print(pos, val)
    

#add reward for winning
# add reward for losing
# add reward for draw
# add reward for each move 