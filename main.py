from imports import choice
from tic_tac_toe_board import Board
from random_move import random_move
#q-table function system

board = Board()

for _ in range(100):
    board = random_move(board, 'X')
    board = random_move(board, 'O')