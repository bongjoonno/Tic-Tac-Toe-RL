from tic_tac_toe_board import Board
from imports import deepcopy

def minimax(board: Board):
    if board.spots_left == []:
        return board.last_reward
    
    symbol_to_move = Board.opposite_symbol[board.last_move_player]
    
    if symbol_to_move == 'X':
        value = float('-inf')

        for a in board.spots_left:
            board_cop = deepcopy(board)
            board_cop.move(symbol_to_move, {'specific' : a})
            
            recursive_eval = minimax(board_cop)

            if recursive_eval > value:
                best_action = a
                value = recursive_eval
        
        return best_action

    
    if symbol_to_move == 'O':
        value = float('inf')

        for a in board.spots_left:
            board_cop = deepcopy(board)
            board_cop.move(symbol_to_move, {'specific' : a})
            
            recursive_eval = minimax(board_cop)

            if recursive_eval < value:
                best_action = a
                value = recursive_eval
        
        return best_action

def minimax_test():
    board = Board(0)

    symbol_to_move = Board.opposite_symbol[board.last_move_player]
    chosen_move = minimax(board)
    outcome = board.move(symbol_to_move, {'specific' : chosen_move})
        
    print(outcome)
    board.display_board()

    symbol_to_move = Board.opposite_symbol[board.last_move_player]
    chosen_move = minimax(board)
    outcome = board.move(symbol_to_move, {'specific' : chosen_move})
        
    print(outcome)
    board.display_board()

if __name__ == '__main__': minimax_test()
