from imports import choice, choices

class Board():
    def __init__(self, q_table = {}, epsilon = 1):
        self.q_table = q_table
        self.epsilon = epsilon
        
        self.board = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]

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
        self.spots_left = list(range(0, 9))
        self.possible_moves = []
        self.possible_moves_fen_dict = {}
        
    def display_board(self):
        for row in self.board:
            print(row)
        print('\n')
        
    def move(self, symbol):
        self.last_move_player = symbol
        
        move = self.get_next_move()
        
        self.spots_left.remove(move)
        self.update_q_table(move)
        
        y, x = (move // 3, move % 3)
        self.board[y][x] = symbol
        
        
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
    
    def update_q_table(self, move):
        self.q_table[self.make_fen(move)] = 0
    
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
        fen.append(str(move))
        return ''.join(fen)  
    
    def calculate_possible_moves_fen(self):
        possible_moves_fens = []
        
        for spot in self.spots_left:
            possible_moves_fens.append(self.make_fen(spot))
        
        return possible_moves_fens

    def get_next_move(self):
        self.possible_moves = self.calculate_possible_moves_fen()
        self.possible_moves_fen_dict = {move_fen: self.q_table.get(move_fen, 0) for move_fen in self.possible_moves}
        
        if len(self.possible_moves) == 1:
            move = self.possible_moves[0]

        elif not all(self.possible_moves_fen_dict.values()):
            move = choice(self.spots_left)
        
        else:
            self.policy()

        
        return move

    def policy(self):
        random_move_prob = 1 / len(self.possible_moves)
        max_q_score_move = max(self.possible_moves_fen_dict, key = self.possible_moves_fen_dict.get)
        
        probs = []
        
        for move in self.possible_moves_fen_dict.keys():
            if move == max_q_score_move:
                probs.append(random_move_prob + self.epsilon)
            else:
                probs.append(random_move_prob)
                
        
        return choices(self.possible_moves, weights = probs)        