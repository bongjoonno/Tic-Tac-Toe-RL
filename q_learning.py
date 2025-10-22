from tic_tac_toe_board import Board
from constants import ALPHA, GAMMA

def q_learning(board: Board):
    outcome = board.move('X', random = False)

    current_q_score = Board.q_table[board.last_move_fen]

    try:
        max_reward_move_q_score_for_next_state = board.q_learning_update()
    except ValueError:
        max_reward_move_q_score_for_next_state = 0
    
    Board.q_table[board.last_move_fen] += ALPHA * (board.last_reward + (GAMMA * max_reward_move_q_score_for_next_state) - current_q_score)
    
    return outcome