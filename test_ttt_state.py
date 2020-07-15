from ttt_state import TicTacToeState
import unittest
import numpy

class TicTacToeStateTest(unittest.TestCase):

    def test_create_state_no_player(self):
        state = TicTacToeState()
        self.assertEqual(state._player, 1)
        self.assertIsNotNone(state._board)

    def test_next_state_from_action(self):
        state = TicTacToeState()
        action = (0,0)
        self.assertTrue(action in state.get_possible_actions())
        next_state = state.next_state_from_action((0,0))
        expected_board = numpy.array([[2,0,0],[0,0,0],[0,0,0]])
        self.assertTrue(next_state._board.shape == expected_board.shape)
        self.assertTrue((next_state._board == expected_board).all())
        self.assertTrue(next_state._player == 2)

    def test_is_terminal_true(self):
        board = numpy.array([[2,2,2],
                             [1,1,0],
                             [0,0,1]])

        state = TicTacToeState(board=board)
        self.assertTrue(state.is_terminal())

    def test_is_terminal_false(self):
        board = numpy.array([[2,2,1],
                             [1,2,0],
                             [0,0,1]])

        state = TicTacToeState(board=board)
        self.assertFalse(state.is_terminal())

    def test_calculate_reward_winner(self):
        board = numpy.array([[2,2,1],
                             [2,1,0],
                             [1,0,0]])
        state = TicTacToeState(board=board)
        self.assertTrue(state.calculate_reward() == 1)

    def test_calculate_reward_loser(self):
        board = numpy.array([[1,1,2],
                             [1,2,0],
                             [2,0,0]])
        state = TicTacToeState(board=board)
        self.assertTrue(state.calculate_reward() == -1)

    def test_calculate_reward_tie(self):
        board = numpy.array([[2,1,2],
                             [1,2,1],
                             [1,1,2]])
        state = TicTacToeState(current_player=2,board=board)
        self.assertTrue(state.calculate_reward() == 0)





