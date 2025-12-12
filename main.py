from tic_tac_toe_board import Board
from constants import EPSILON
from train_model import train_model
from play import play_tic_tac_toe

epsilon = EPSILON

board = Board(epsilon)

epochs = 100_000

train_model(epochs)
play_tic_tac_toe()