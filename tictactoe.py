"""
Tic Tac Toe Player
"""

from cmath import inf
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    
    # Returns starting state of the board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    # Returns player who has the next turn on a board
    num_x = 0
    num_o = 0
    for row in board:
        for cell in row:
            if cell == "X":
                num_x += 1
            elif cell == "O":
                num_o += 1
    if num_x > num_o:
        return O
    else:
        return X


def actions(board):

    # Returns set of all possible actions (i, j) available on the board
    row_num = -1
    cell_num = -1
    actions = []
    for row in board:
        row_num += 1
        cell_num = -1
        for cell in row:
            cell_num += 1
            if cell == EMPTY:
                actions.append((row_num, cell_num))
    return actions


def result(board, action):

    # Returns the board that results from making move (i, j) on the board
    row = action[0]
    cell = action[1]
    current_player = player(board)
    if board[row][cell] == EMPTY:
        new_board = deepcopy(board)
        new_board[row][cell] = current_player
        return new_board
    else:
        raise NotImplementedError


def winner(board):

    # Returns the winner of the game, if there is one
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
    for j in range(3):
        if (board[0][j] == board[1][j] == board[2][j]) and board[0][j] != EMPTY:
            return board[0][j]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):

    # Returns True if game is over, False otherwise
    if winner(board) != None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):

    # Returns 1 if X has won the game, -1 if O has won, 0 otherwise
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):

    # Returns the optimal action for the current player on the board
    if terminal(board):
        return None
    elif player(board) == X:
        value, move = max_value(board)
        return move
    elif player(board) == O:
        value, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float("-inf")
    move = None
    for action in actions(board):
        score, act = min_value(result(board, action))
        if score > v:
            v = score
            move = action
            if v == 1:
                return v, move
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float("inf")
    move = None
    for action in actions(board):
        score, act = max_value(result(board, action))
        if score < v:
            v = score
            move = action
            if v == -1:
                return v, move
    return v, move