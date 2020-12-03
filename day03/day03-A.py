#!/usr/bin/env python3

import collections
import re
import sys

# Constants

TREE = '#'

# Functions

def read_grid():
    return [line.strip() for line in sys.stdin]

def walk_grid(grid, dx, dy):
    width  = len(grid[0])
    height = len(grid)
    x, y   = 0, 0
    trees  = 0

    while y < height:
        trees += int(grid[y][x % width] == TREE)
        x += dx
        y += dy

    return trees

# Main Execution

def main():
    grid  = read_grid()
    trees = walk_grid(grid, 3, 1)

    print(trees)

if __name__ == '__main__':
    main()
