from tic_tac_toe_board import Board
from constants import EPSILON
from train import train
from imports import plt
from play import play
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 100_000
train(epochs)
play()