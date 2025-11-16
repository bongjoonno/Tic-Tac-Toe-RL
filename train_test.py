from tic_tac_toe_board import Board
from v_learning import v_learning
from constants import EPSILON
from imports import plt

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
    games = 0
    epsilons  = []
    
    for _ in range(epochs):
        epsilons.append(epsilon)
        outcome = v_learning(board)
        
        if outcome == 'X WON!' or outcome == 'Draw':
            board = Board(epsilon)
            if train_or_test == 'train':
                epsilon = max(0.05, epsilon * 0.9999)
                games += 1
            continue
        
        outcome = board.move('O', move_style = move_style)
        
        if outcome == 'O WON!' or outcome == 'Draw':
            board = Board(epsilon)
            if train_or_test == 'train':
                epsilon = max(0.05, epsilon * 0.9999)
                games += 1
    
    plt.plot(range(len(epsilons)), epsilons)
    plt.show()
    return Board.total_rewards, games