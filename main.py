from tic_tac_toe_board import Board
from constants import EPSILON
from train import train
from imports import plt
from play import play
#q-table function system

epsilon = EPSILON

board = Board(epsilon)

epochs = 1_000_000
rewards_x, rewards_o = train(epochs)
play()