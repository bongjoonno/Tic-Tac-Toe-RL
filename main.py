from imports import choice, sleep
from tic_tac_toe_board import Board
from constants import EPSILON
from q_learning import q_learning
from train_test import train_test
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 50_000

print(len(Board.q_table))
train_test(epochs, 'train')
print(len(Board.q_table))
train_test(epochs, 'play')