from tic_tac_toe_board import Board
from imports import deepcopy

def minimax(board: Board, best_action = None):
    if best_action is not None and board.last_reward in [-10, 10]:
        return board.last_reward
    
    symbol_to_move = Board.opposite_symbol[board.last_move_player]
    
    if symbol_to_move == 'X':
        value = float('-inf')

        for a in board.spots_left:
            board_cop = deepcopy(board)
            board_cop.move(symbol_to_move, {'specific' : a})
            
            value = max(value, minimax(board_cop))
        
        return value

    if symbol_to_move == 'O':
        value = float('inf')

        for a in board.spots_left:
            board_cop = deepcopy(board)
            board_cop.move(symbol_to_move, {'specific' : a})
            
            value = min(value, minimax(board_cop))
        
        return value
    

board = Board(0)

res = minimax(board)
print(res)