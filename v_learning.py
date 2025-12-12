from tic_tac_toe_board import Board
from constants import ALPHA, GAMMA

def v_learning(board: Board):
    outcome = board.move('X', move_style = 'policy')

    current_v_score = Board.v_table[board.last_move_fen_set]

    try:
        max_reward_position_v_score_for_next_state = board.v_learning_update()
    except ValueError:
        max_reward_position_v_score_for_next_state = 0
    
    Board.v_table[board.last_move_fen_set] += ALPHA * (board.last_reward + (GAMMA * max_reward_position_v_score_for_next_state) - current_v_score)
    
    return outcome