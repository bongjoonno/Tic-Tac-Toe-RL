from tic_tac_toe_board import Board
from constants import EPSILON
from train_test import train_test
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 50_000

train_test(epochs, 'minimax')