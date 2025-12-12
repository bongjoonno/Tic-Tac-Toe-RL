from tic_tac_toe_board import Board
from v_learning import v_learning
from constants import EPSILON
from imports import plt

def train_model(epochs: int):
    epsilon = EPSILON
      
    board = Board(epsilon)
    
    for _ in range(epochs):
        outcome = v_learning(board)
        
        if outcome == 'X WON!' or outcome == 'Draw':
            board = Board(epsilon)
            epsilon = max(0.05, epsilon * 0.999)
            continue
        
        outcome = board.move('O', move_style = 'random')
        
        if outcome == 'O WON!' or outcome == 'Draw':
            board = Board(epsilon)
            epsilon = max(0.05, epsilon * 0.999)