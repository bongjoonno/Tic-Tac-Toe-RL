class Board():
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        
        self.available_boxes = set((i, j) for i in range(3) for j in range(3))
    
    def display_board(self):
        for row in self.board:
            print(row)
        
    def move(self, y, x, symbol):
        if (y, x) in self.available_boxes:
            self.board[y][x] = symbol
            self.available_boxes.remove((y, x))
        else:
            print('Invalid move')