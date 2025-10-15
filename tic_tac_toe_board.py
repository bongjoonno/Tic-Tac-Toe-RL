class Board():
    def __init__(self, q_table = {}):
        self.q_table = q_table
        self.board = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]
        
        self.available_boxes = set((i, j) for i in range(3) for j in range(3))

        self.winning_position_pairs = [[(0, 0), (0, 1), (0, 2)],
                                      [(1, 0), (1, 1), (1, 2)],
                                      [(2, 0), (2, 1), (2, 2)],
                                      [(0, 0), (1, 0), (2, 0)],
                                      [(0, 1), (1, 1), (2, 1)],
                                      [(0, 2), (1, 2), (2, 2)],
                                      [(0, 0), (1, 1), (2, 2)],
                                      [(0, 2), (1, 1), (2, 0)]]
        
        self.last_move_player = 'X'
        
        self.rewards = {'X' : 0, 'O' : 0}
        self.opposite_symbol = {'X' : 'O', 'O' : 'X'}
        self.last_move = 'None'
        self.spots_left = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
    def display_board(self):
        for row in self.board:
            print(row)
        print('\n')
        
    def move(self, y, x, symbol):
        if (y, x) in self.available_boxes:
            self.last_move_player = symbol
            self.last_move = str((y * 3) + (x + 1))
            self.spots_left.remove(self.last_move)
            
            self.update_q_table()
            self.board[y][x] = symbol
            self.available_boxes.remove((y, x))
            outcome = self.check_win(symbol)
            
            if outcome == 'No win...':
                if self.spots_left == []:
                    outcome = 'Draw'
                else:
                    self.rewards[symbol] -= 0.1
            
            else:
                self.rewards[symbol] += 10
                self.rewards[self.opposite_symbol[symbol]] -= 10
                
                
            return outcome
    
    def update_q_table(self):
        self.q_table[self.make_fen(self.last_move)] = 0
    
    def check_win(self, symbol):
        for winning_position in self.winning_position_pairs:
            slot1 = winning_position[0]
            slot2 = winning_position[1]
            slot3 = winning_position[2]
            
            if self.board[slot1[0]][slot1[1]] == symbol:
                if self.board[slot2[0]][slot2[1]] == symbol:
                    if self.board[slot3[0]][slot3[1]] == symbol:
                        return f'{symbol} WON!'
        return 'No win...'

    def make_fen(self, move):
        fen = []
        for row in self.board:
            for item in row:
                fen.append(item)
        
        fen.append(self.last_move_player)
        fen.append(move)
        return ''.join(fen)  
    
    def calculate_possible_moves_fen(self):
        possible_moves_fens = []
        
        for spot in self.spots_left:
            possible_moves_fens.append(self.make_fen(spot))
        
        return possible_moves_fens