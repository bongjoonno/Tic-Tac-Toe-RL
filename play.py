from tic_tac_toe_board import Board

def play_tic_tac_toe():
    board = Board(0)
    
    while True:
        outcome = board.move('X', move_style='policy')
        
        if outcome != 'Game Continues':
            board = Board(0)
            print(outcome)
            continue
            
        outcome = board.move('O', move_style='choose')
        
        if outcome != 'Game Continues':
            board = Board(0)
            print(outcome)
    