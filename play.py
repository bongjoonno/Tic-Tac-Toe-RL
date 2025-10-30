from tic_tac_toe_board import Board
from q_learning import q_learning

def play():
    epsilon = 0

    board = Board(epsilon)

    play_again = 'yes'
    outcome = ''
    
    while play_again.lower() == 'yes':
        board = Board(epsilon)
        
        player = input('which player do you want to choose (x/o): ').lower()
        
        
        while 'WON!' not in outcome or outcome == 'Draw':
            if player == 'x':
                outcome = board.move('choose')
                q_learning(board)
            else:
                q_learning(board)
                outcome = board.move('choose')
        print(outcome)
    
        play_again = input('Would you like to play again (yes/no)?: ')
        