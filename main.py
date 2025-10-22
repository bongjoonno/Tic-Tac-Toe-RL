from imports import choice, sleep
from tic_tac_toe_board import Board
from constants import EPSILON
from q_learning import q_learning

#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 50_000

for i in range(epochs):
    outcome = q_learning(board)
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(epsilon)
        epsilon = max(0, epsilon ** 0.999)
        continue
    
    outcome = board.move('O', move_style = 'choose')
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(epsilon)
        epsilon = max(0, epsilon ** 0.999)