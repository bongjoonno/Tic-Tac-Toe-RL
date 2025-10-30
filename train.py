from tic_tac_toe_board import Board
from q_learning import q_learning
from constants import EPSILON

def train(epochs: int):
    epsilon = EPSILON

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