from tic_tac_toe_board import Board

def play():
    epsilon = 0

    board = Board(epsilon)

    play_again = 'yes'
    
    while play_again.lower() == 'yes':
        board = Board(epsilon)
        
        outcome = q_learning(board)
        
        while 'WON!' not in outcome or outcome == 'Draw':
        if 'WON!' in outcome or 'Draw' in outcome:
            board = Board(epsilon)
            continue
    
        play_again = input('Would you like to play again (yes/no)?: ')
        