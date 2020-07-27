from uct import uct_decision
from tic_tac_toe import *
import numpy

def play_move(x,y, player):
    global board

    board[x,y] = player
    print(board)
    winner = evaluate(board)
    if winner != 0:
        print('Winner: ', winner)
        board = create_board()
        print(board)

# def survival_instinct():
#     state = TicTacToeState(board=board)
#     actions = state.get_possible_actions()

#     for a in actions:
#         board[a[0], a[1]] = 1
#         winner = evaluate(state)
#         if winner == 2


def uct():
    move = uct_decision(TicTacToeState(board=board), num_iterations=8000)
    play_move(move[0], move[1], 1)

def play(x,y):
    play_move(x,y,2)
    uct()

def new():
    global board
    board = create_board()
    print(board)

if __name__ == "__main__":
    global board 
    board = create_board()
    board = numpy.array([[0, 0, 0],
                         [0, 2, 2],
                         [0, 1, 0]])
    print(board)
    uct()