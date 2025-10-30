from tic_tac_toe_board import Board
from q_learning import q_learning

def play():
    epsilon = 0

    board = Board(epsilon)

    play_again = 'yes'
    outcome = ''
    
    while play_again.lower() == 'yes':
        board = Board(epsilon)
        
        
        while 'WON!' not in outcome or outcome == 'Draw':
            q_learning(board)
            outcome = board.move('choose')
        print(outcome)
    
        play_again = input('Would you like to play again (yes/no)?: ')
        