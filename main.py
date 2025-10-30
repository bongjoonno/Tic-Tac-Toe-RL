from tic_tac_toe_board import Board
from constants import EPSILON
from train import train
from imports import plt
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 500_000
rewards_x, rewards_o = train(epochs, 'train')
print(len(board.q_table))
train(epochs, 'play')