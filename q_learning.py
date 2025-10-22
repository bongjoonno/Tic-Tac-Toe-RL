from tic_tac_toe_board import Board
from constants import ALPHA, GAMMA

def q_learning(board: Board):
    outcome = board.move('X', random = False)

    current_q_score = board.q_table[board.last_move_fen]

    board.q_table[board.last_move_fen] = ALPHA * (board.last_reward + (GAMMA * (max(future_moves)) - current_q_score))
    
    if 'WON!' in outcome or 'Draw' in outcome:
        board = Board(q_table = board.q_table, epsilon = epsilon)
        epsilon = max(0, epsilon ** 0.999)