from tic_tac_toe_board import Board
from constants import EPSILON
from train_model import train_model

epsilon = EPSILON

board = Board(epsilon)

epochs = 100

train_model(epochs)
