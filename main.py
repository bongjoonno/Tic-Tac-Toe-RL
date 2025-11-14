from tic_tac_toe_board import Board
from constants import EPSILON
from train_test import train_test

epsilon = EPSILON

board = Board(epsilon)

epochs = 1_000_000

train_test(epochs, 'train')
train_test(epochs, 'play')