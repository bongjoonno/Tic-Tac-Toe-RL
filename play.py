from tic_tac_toe_board import Board

def play_tic_tac_toe():
    board = Board(0)
    
    while True:
        board.move('X', move_style='policy')
        board.move('O', move_style='choose')