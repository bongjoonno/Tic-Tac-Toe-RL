from tic_tac_toe_board import Board
from q_learning import q_learning
from imports import tqdm


def train(epochs: int, training_mode): 
    if training_mode not in ['self', 'random']:
        raise ValueError('Please give "self" or "random"')

    board = Board()

    rewards_x = []
    rewards_o = []
    
    for _ in tqdm(range(epochs)):
        Board.epsilon = max(0, Board.epsilon * 0.999)
        outcome = q_learning(board)
        
        if 'WON!' in outcome or outcome == 'Draw':
            rewards_x.append(board.rewards['X'])
            rewards_o.append(board.rewards['O'])
            board = Board()
            continue

        if training_mode == 'self':
            outcome = q_learning(board)
        
            if 'WON!' in outcome or outcome == 'Draw':
                rewards_x.append(board.rewards['X'])
                rewards_o.append(board.rewards['O'])
                board = Board()
                continue
            
        elif training_mode == 'random':
            outcome = board.move('random')
        
            if 'WON!' in outcome or outcome == 'Draw':
                rewards_x.append(board.rewards['X'])
                rewards_o.append(board.rewards['O'])
                board = Board()
            continue
            
    
    return rewards_x, rewards_o


def reset_board(outcome, board, epsilon, rewards_x, rewards_o):
    if 'WON!' in outcome or outcome == 'Draw':
        rewards_x.append(board.rewards['X'])
        rewards_o.append(board.rewards['O'])
        epsilon = max(0, epsilon ** 0.999)
        board = Board(epsilon)
        return board, epsilon
    return False
        