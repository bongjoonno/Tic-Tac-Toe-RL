from imports import choice, choices

class Board:
    winning_position_pairs = [[(0, 0), (0, 1), (0, 2)],
                              [(1, 0), (1, 1), (1, 2)],
                              [(2, 0), (2, 1), (2, 2)],
                              [(0, 0), (1, 0), (2, 0)],
                              [(0, 1), (1, 1), (2, 1)],
                              [(0, 2), (1, 2), (2, 2)],
                              [(0, 0), (1, 1), (2, 2)],
                              [(0, 2), (1, 1), (2, 0)]]
    v_table = {}

    opposite_symbol = {'X' : 'O', 'O' : 'X'}

    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.max_v_score_move_greedy_prob = 1 - self.epsilon
        self.board = [['0', '0', '0'],
                      ['0', '0', '0'],
                      ['0', '0', '0']]
        
        self.last_move_player = 'O'
        
        self.rewards = {'X' : 0, 'O' : 0}
        self.spots_left = list(range(9))
        self.last_reward = 0
        
    def display_board(self):
        for row in self.board:
            print(row)
        print('\n')
        
    def move(self, symbol, move_style):
        self.last_move_player = symbol

        move = self.get_next_move(move_style)

        self.spots_left.remove(move)

        if symbol == "X":
            self.update_v_table(move)

        self.update_board(move, symbol)
        
        outcome = self.check_win(symbol)
        
        if outcome == 'No win...':
            if self.spots_left == []:
                outcome = 'Draw'
                
            self.last_reward = 0
        
        else:
            self.last_reward = 1
            self.rewards[symbol] += self.last_reward
            self.rewards[Board.opposite_symbol[symbol]] -= self.last_reward
            
            
        return outcome

    def get_next_move(self, move_style):
        self.next_possible_position_fens = [self.make_fen(spot) for spot in self.spots_left]
        self.next_possible_position_fens_dict = {position: Board.v_table.get(position, 0) for position in self.next_possible_position_fens}

        if len(self.next_possible_position_fens) == 1:
            return self.spots_left[0]
        
        elif move_style == "choose":
            move = ''
            
            self.display_board()
            
            while move not in set(self.spots_left):
                move = int(input("Type in your move (0-8): ")) 
            return move

        elif not all(self.next_possible_position_fens_dict.values()) or move_style == "random":
            return choice(self.spots_left)
        
        elif move_style == 'policy':
            return self.policy()
        else:
            raise ValueError("Invalid move style, must be 'random', 'choose', or 'policy'")

    def make_fen(self, spot):
        fen = []
        
        for row in self.board:
            for item in row:
                fen.append(item)
        
        fen.append(self.last_move_player)
        fen[spot] = Board.opposite_symbol[self.last_move_player]
        return ''.join(fen)  
    
    def update_v_table(self, move):
        self.last_move_fen = self.make_fen(move)
        
        Board.v_table[self.last_move_fen] = Board.v_table.get(self.last_move_fen, 0)
        
    def update_board(self, move, symbol):
        y, x = (move // 3, move % 3)
        self.board[y][x] = symbol
    
    
    def check_win(self, symbol):
        for winning_position in Board.winning_position_pairs:
            slot1 = winning_position[0]
            slot2 = winning_position[1]
            slot3 = winning_position[2]
            
            if self.board[slot1[0]][slot1[1]] == symbol:
                if self.board[slot2[0]][slot2[1]] == symbol:
                    if self.board[slot3[0]][slot3[1]] == symbol:
                        return f'{symbol} WON!'
        return 'No win...'
    
        
    def policy(self):
        random_move_prob = self.epsilon / len(self.next_possible_position_fens)
        max_v_score_position = max(self.next_possible_position_fens_dict, key = self.next_possible_position_fens_dict.get)
        
        probs = []
        
        for position in self.next_possible_position_fens:
            if position == max_v_score_position:
                probs.append(random_move_prob + self.max_v_score_move_greedy_prob)
            else:
                probs.append(random_move_prob)
                
        return choices(self.spots_left, weights = probs)[0]
    
    def v_learning_update(self):
        self.next_possible_position_fens = [self.make_fen(spot) for spot in self.spots_left]
        self.next_possible_position_fens_dict = {position: Board.v_table.get(position, 0) for position in self.next_possible_position_fens}
        return max(self.next_possible_position_fens_dict.values())