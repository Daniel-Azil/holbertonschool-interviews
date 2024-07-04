
#!/usr/bin/python3
"""challenge of placing N non-attacking queens on an N×N chessboard"""
import sys


def nonAttack(brd, ln, i):
    '''checks a place is not attacked by queens'''
    for j in range(ln):
        if(brd[j] == i or brd[j] + ln - j == i or brd[j] + j - ln == i):
            return False
    return True


def fillBoard(brd, ln):
    '''finds the next safe posn to land the queen'''
    for i in range(len(brd)):
        if nonAttack(brd, ln, i):
            brd[ln] = i
            if ln < len(brd) - 1:
                fillBoard(brd, ln + 1)
            else:
                print([[i, brd[i]] for i in range(len(brd))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
brd = [-1 for i in range(n)]
fillBoard(brd, 0)
