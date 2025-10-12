from tic_tac_toe_board import Board
#q-table function system

board = Board()
for _ in range(10):
    random_move = choice()
    outcome = board.move(0, 2, 'X')
    
    if outcome == 'X WON!':
        board = Board()