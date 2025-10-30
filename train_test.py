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

    rewards_x = []
    rewards_o = []
    
    for _ in range(epochs):
        outcome = q_learning(board)
        
        if 'WON!' in outcome or 'Draw' in outcome:
            rewards_x.append(board.rewards['X'])
            rewards_o.append(board.rewards['O'])
            board = Board(epsilon)
            epsilon = max(0, epsilon ** 0.999)
            continue
    
    return rewards_x, rewards_o