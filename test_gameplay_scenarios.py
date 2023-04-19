import unittest
from uct import uct_decision
from tic_tac_toe import *
import numpy as np

class TicTacToePlayTestCase(unittest.TestCase):

    def test_blocks_winning_move(self):
        board = np.array([[0, 0, 0],
                          [0, 2, 2],
                          [0, 1, 0]])
        move = uct_decision(TicTacToeState(board=board), num_iterations=500)
        board[move[0], move[1]] = 1
        self.assertEquals(board[1,0], 1)