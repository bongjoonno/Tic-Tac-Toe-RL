from tic_tac_toe_board import Board
from constants import EPSILON
from train import train
from imports import plt
from play import play
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 250_000
rewards_x, rewards_o = train(epochs, training_mode = 'random')
print(Board.policy_count)
play()
#self: 170,151
#random: 89,367