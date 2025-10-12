class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
    
    def move(self, y, x, symbol):
        self.board[y][x] = symbol