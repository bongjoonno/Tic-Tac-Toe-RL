class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
    
    def display_board(self):
        for row in self.board:
            print(row)
        
    def move(self, y, x, symbol):
        self.board[y][x] = symbol