from tic_tac_toe_board import Board
from constants import EPSILON
from train_test import train_test

epsilon = EPSILON

board = Board(epsilon)

epochs = 1_250_000

total_rewards, games = train_test(epochs, 'train')
percentage_of_games_won = total_rewards['X'] / games

print(percentage_of_games_won, total_rewards)
train_test(epochs, 'play')