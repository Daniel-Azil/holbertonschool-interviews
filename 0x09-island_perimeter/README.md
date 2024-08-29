# Island Perimeter Calculation

## Overview

This project includes a function named `island_perimeter(grid)` that calculates and returns the perimeter of a single island within a given grid. The grid is a 2D list of integers where:

- `0` represents water.
- `1` represents land.
- Each cell in the grid is a square with a side length of 1 unit.
- Land cells are connected horizontally or vertically but not diagonally.

## Grid Specifications

- The grid is a rectangular matrix, with both its width and height not exceeding 100 cells.
- The grid is entirely surrounded by water, meaning there are no boundaries where land cells are adjacent to the edge of the grid without water.
- The grid contains exactly one island, or it could be empty (all cells are water).
- The island is guaranteed to be a continuous landmass with no "lakes" or areas of water within the island itself.

## Function Details

The function `island_perimeter(grid)` processes the grid to calculate the total perimeter of the island. The perimeter is determined by examining each land cell and checking its adjacent cells (left, right, top, bottom). For each land cell, the function increases the perimeter count based on whether adjacent cells are water or out of bounds.

### Usage

```python
def island_perimeter(grid):
    '''Returns the perimeter of the island described in grid'''
    perimeter = 0
    num_rows = len(grid) - 1  # Index of the last row in the grid
    num_cols = len(grid[0]) - 1  # Index of the last column in the grid

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
```

This function is designed to handle grids of varying sizes, adhering to the constraints provided. Ensure to provide a valid grid as input to accurately compute the island's perimeter.