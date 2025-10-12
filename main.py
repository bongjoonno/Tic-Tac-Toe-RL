from imports import choice
from tic_tac_toe_board import Board
from random_move import random_move
#q-table function system

board = Board()
q_table = {}

for _ in range(100_000_000):
    board, q_table = random_move(board, 'X', q_table)
    board, q_table = random_move(board, 'O', q_table)

print(len(q_table))

#for pos, val in q_table.items():
    #print(pos, val)