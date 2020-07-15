from tic_tac_toe import *

class TicTacToeState:

    def __init__(self, current_player = 1, board = None):
        if board is not None:
            self._board = board
        else:
            self._board = create_board()
        self._player =  current_player 

    def get_possible_actions(self):
        return possibilities(self._board)

    def next_state_from_action(self, action):
        player = self._next_player()
        next_board = np.copy(self._board)
        self._play_move(player, action, next_board)
        return TicTacToeState(current_player=player, board = next_board)

    def calculate_reward(self):
        assert self.is_terminal()
        winner = evaluate(self._board)

        if winner == -1:
            return 0
        else:
            if winner == 1:
                return 1
            else:
                return -1

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
