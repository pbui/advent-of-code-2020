#!/usr/bin/env python3

import collections
import copy
import sys

# Constants

EMPTY     = 'L'
OCCUPIED  = '#'
FLOOR     = '.'
THRESHOLD = 5

# Functions

def read_grid(stream=sys.stdin):
    grid = []

    for line in stream:
        grid.append([FLOOR] + list(line.strip()) + [FLOOR])

    grid.insert(0, list(FLOOR * len(grid[0])))
    grid.append(grid[0])

    return grid

def count_occupied(grid):
    return sum(row.count(OCCUPIED) for row in grid)

def count_neighbors(grid, row, col):
    count = 0

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx or dy) and search_direction(grid, row, col, dx, dy):
                count += 1

    return count

def search_direction(grid, row, col, dx, dy):
    width    = len(grid[0]) - 1
    height   = len(grid) - 1

    while (0 < row < height) and (0 < col < width):
        row += dx
        col += dy

        if grid[row][col] == OCCUPIED:
            return True
        elif grid[row][col] == EMPTY:
            return False

    return False

def simulate(old_grid):
    width    = len(old_grid[0]) - 1
    height   = len(old_grid) - 1
    new_grid = copy.deepcopy(old_grid)

    for row in range(1, height):
        for col in range(1, width):
            neighbors = count_neighbors(old_grid, row, col)
            if old_grid[row][col] == EMPTY and neighbors == 0:
                new_grid[row][col] = OCCUPIED
            elif old_grid[row][col] == OCCUPIED and neighbors >= THRESHOLD:
                new_grid[row][col] = EMPTY

    return new_grid

# Main Execution

def main():
    old_grid = read_grid()
    new_grid = simulate(old_grid)

    while count_occupied(old_grid) != count_occupied(new_grid):
        old_grid = new_grid
        new_grid = simulate(old_grid)

    print(count_occupied(new_grid))

if __name__ == '__main__':
    main()
