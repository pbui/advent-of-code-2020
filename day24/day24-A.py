#!/usr/bin/env python3

import pprint
import sys

# Constants

WHITE = 0
BLACK = 1

DIRECTIONS = {
    'w' : (-1, -1),
    'e' : ( 1,  1),
    'nw': (-2,  1),
    'ne': (-1,  2),
    'sw': ( 1, -2),
    'se': ( 2, -1),
}

# Functions

def make_tiles(stream=sys.stdin):
    tiles = {(0, 0): WHITE}

    for line in stream:
        flip_tile(line.strip(), tiles)

    return tiles

def flip_tile(steps, tiles):
    x, y = 0, 0

    while steps:
        if steps[0] in ('e', 'w'):
            direction, steps = steps[0] , steps[1:]
        else:
            direction, steps = steps[:2], steps[2:]

        dx, dy = DIRECTIONS[direction]
        x , y  = x + dx, y + dy

    if (x, y) in tiles:
        tiles[x, y] = (tiles[x, y] + 1) % 2
    else:
        tiles[x, y] = BLACK

# Main Execution

def main():
    tiles = make_tiles()
    print(sum(tiles.values()))

if __name__ == '__main__':
    main()
