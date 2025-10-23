from tic_tac_toe_board import Board
from q_learning import q_learning
from constants import EPSILON

def train_test(epochs: int, train_or_test = 'train'):
    if train_or_test == 'train':
        move_style = 'random'
        epsilon = EPSILON
    elif train_or_test == 'play':
        move_style = 'choose'
        epsilon = 0
    else:
        raise ValueError("Invalid model-style, choose 'train', or 'play'")
        
    board = Board(epsilon)

    for _ in range(epochs):
        outcome = q_learning(board)
        
        if 'WON!' in outcome or 'Draw' in outcome:
            board = Board(epsilon)
            epsilon = max(0, epsilon ** 0.999)
            continue
        
        outcome = board.move('O', move_style = move_style)
        
        if 'WON!' in outcome or 'Draw' in outcome:
            board = Board(epsilon)
            epsilon = max(0, epsilon ** 0.999)