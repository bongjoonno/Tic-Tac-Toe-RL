from tic_tac_toe_board import Board
from constants import EPSILON
from train_test import train_test
from imports import plt
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 500_000
rewards_x, rewards_o = train_test(epochs, 'train')
train_test(epochs, 'play')