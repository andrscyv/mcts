from .util import *

class TicTacToeState:

    def __init__(self, current_player = 1, board = None):
        if board is not None:
            self._board = board
        else:
            self._board = create_board()
        self._player =  current_player 

    def get_possible_actions(self):
        if self.is_terminal():
            return []

        return possibilities(self._board)

    def next_state_from_action(self, action):
        next_board = np.copy(self._board)
        self._play_move(self._player, action, next_board)
        player = self._next_player()
        return TicTacToeState(current_player=player, board = next_board)

    def calculate_reward(self):
        winner = evaluate(self._board)
        assert winner != 0 

        if winner == -1:
            return 0.5
        else:
            if winner == 1:
                return 1 
            else:
                return 0

    def is_terminal(self):
        return evaluate(self._board) != 0

    def _play_move(self, player, move, board):
        #move is a tuple of (x,y) coordinates
        board[move[0], move[1]] = player

    def _next_player(self):
        if self._player == 1:
            return 2
        else:
            return 1


if __name__ == "__main__":
    # state = TicTacToeState()
    # print(state._board)
    board = create_board()
    print(board)
    print(possibilities(board))
