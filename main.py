from tic_tac_toe_board import Board
from constants import EPSILON
from train_test import train_test

epsilon = EPSILON

board = Board(epsilon)

epochs = 600_000

total_rewards = train_test(epochs, 'train')
print(total_rewards)
train_test(epochs, 'play')