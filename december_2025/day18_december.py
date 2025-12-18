"""Checkerboard

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

    The characters should alternate like a checkerboard.
    The top-left cell must always be "X".

For example, given [3, 3], return:"""

def create_board(dimensions):
    rows, cols = dimensions
    board = []

    for r in range(rows):
        row = []
        for c in range(cols):
            if (r + c) % 2 == 0:
                row.append("X")
            else:
                row.append("O")
        board.append(row)

    return board