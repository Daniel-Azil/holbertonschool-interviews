#!/usr/bin/python3
'''Island Perimeter Calculation'''


def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid'''
    perimeter = 0
    num_rows = len(grid) - 1  # index of the last row in the grid
    num_cols = len(grid[0]) - 1  # index of the last column in the row

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                # Check left and right sides
                if col_idx == 0:
                    # Left side
                    perimeter += 1

                    # Right side
                    if row[col_idx + 1] == 0:
                        perimeter += 1
                elif col_idx == num_cols:
                    # Left side
                    if row[col_idx - 1] == 0:
                        perimeter += 1

                    # Right side
                    perimeter += 1
                else:
                    # Left side
                    if row[col_idx - 1] == 0:
                        perimeter += 1

                    # Right side
                    if row[col_idx + 1] == 0:
                        perimeter += 1

                # Check top and bottom sides
                if row_idx == 0:
                    # Top side
                    perimeter += 1

                    # Bottom side
                    if grid[row_idx + 1][col_idx] == 0:
                        perimeter += 1
                elif row_idx == num_rows:
                    # Top side
                    if grid[row_idx - 1][col_idx] == 0:
                        perimeter += 1

                    # Bottom side
                    perimeter += 1
                else:
                    # Top side
                    if grid[row_idx - 1][col_idx] == 0:
                        perimeter += 1

                    # Bottom side
                    if grid[row_idx + 1][col_idx] == 0:
                        perimeter += 1

    return perimeter
