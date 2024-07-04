#!/usr/bin/python3
"""
    A module that solves the N queens problem
"""
import sys


def check_attack(board, arg1, i):
    """
        A function that checks if a position is not
        attacked by queens in the previous rows
    """
    for each_arg in range(arg1):
        if(board[each_arg] == i or board[each_arg] + arg1 - each_arg == i or board[each_arg] + each_arg - arg1 == i):
            return False
    return True


def safe_pos(board, arg1):
    """
        A function that checks for safe postions
    """
    for i in range(len(board)):
        if check_attack(board, arg1, i):
            board[arg1] = i
            if arg1 < len(board) - 1:
                safe_pos(board, arg1 + 1)
            else:
                print([[i, board[i]] for i in range(len(board))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    val = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if val < 4:
    print("N must be at least 4")
    sys.exit(1)
board = [-1 for i in range(val)]
safe_pos(board, 0)
