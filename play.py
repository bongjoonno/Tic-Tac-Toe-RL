from tic_tac_toe_board import Board
from q_learning import q_learning

def play():
    Board.epsilon = 0

    play_again = 'yes'
    outcome = ''
    
    while play_again.lower() == 'yes':
        board = Board()
        
        player = input('which player do you want to choose (x/o): ').lower()
        
        
        while 'WON!' not in outcome or outcome != 'Draw':
            if player == 'x':
                outcome = board.move('choose')
                if outcome == 'No win...':
                    outcome = q_learning(board)
                else: break
            else:
                outcome = q_learning(board)
                if outcome == 'No win...':
                    outcome = board.move('choose')
                else: break
        print(outcome)
    
        play_again = input('Would you like to play again (yes/no)?: ')

#current bug play, while loop doesn't check second move