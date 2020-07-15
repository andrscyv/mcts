from uct import uct_decision
from ttt_state import TicTacToeState

if __name__ == "__main__":
    initial_state = TicTacToeState()
    uct_decision(initial_state, num_iterations=10)