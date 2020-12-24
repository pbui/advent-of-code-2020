#!/usr/bin/env python3

import itertools
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

def flatten(iterable):
    return set(itertools.chain.from_iterable(iterable))

def neighbors(x, y, tiles):
    return [(x + dx, y + dy) for dx, dy in DIRECTIONS.values()]

def count_black_neighbors(x, y, tiles):
    return sum(tiles.get((nx, ny), WHITE) for nx, ny in neighbors(x, y, tiles))

def flip_tiles(tiles):
    new_tiles = {}
    old_tiles = flatten(neighbors(x, y, tiles) for x, y in tiles)

    for x, y in old_tiles:
        black_neighbors = count_black_neighbors(x, y, tiles)
        tile_color      = tiles.get((x, y), WHITE)

        if tile_color == BLACK and (black_neighbors == 0 or black_neighbors > 2):
            new_tiles[x, y] = WHITE
        elif tile_color == WHITE and (black_neighbors == 2):
            new_tiles[x, y] = BLACK
        else:
            new_tiles[x, y] = tile_color

    return new_tiles

# Main Execution

def main():
    tiles = make_tiles()

    for _ in range(100):
        tiles = flip_tiles(tiles)

    print(sum(tiles.values()))

if __name__ == '__main__':
    main()
