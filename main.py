from tic_tac_toe_board import Board

board = Board()

board.display_board()



# move functions

board.move(0, 2, 'X')
board.move(1, 1, 'X')
board.move(1, 0, 'X')
board.display_board()