from tic_tac_toe_board import Board
from constants import ALPHA, GAMMA

def q_learning(board: Board):
    current_q_score = board.q_table[board.last_move_fen]
    max_reward_move_q_score_for_next_state = board.q_learning_update()
    board.q_table[board.last_move_fen] += ALPHA * (board.last_reward + (GAMMA * (max_reward_move_q_score_for_next_state)) - current_q_score)