#!/usr/bin/env python3

import collections
import functools
import operator
import re
import sys

# Functions

def read_tile(stream=sys.stdin):
    try:
        number = int(re.findall(r'Tile (\d+):', stream.readline())[0])
    except IndexError:
        return None, None

    tile = []
    while line := stream.readline().strip():
        tile.append(line)

    return number, tile

def read_tiles(stream=sys.stdin):
    tiles = {}
    while (tile := read_tile(stream)) and tile[0]:
        tiles[tile[0]] = tile[1]
    return tiles

def hash_edges(tiles):
    edges = collections.defaultdict(list)

    for number, tile in tiles.items():
        tile_edges = (
            tile[0],                            # Top
            tile[-1],                           # Bottom
            ''.join(r[0]  for r in tile),       # Left
            ''.join(r[-1] for r in tile),       # Right
        )

        for edge in tile_edges:
            edges[edge      ].append(number)
            edges[edge[::-1]].append(number)    # Flipped

    return edges

def find_sides(edges):
    sides = collections.defaultdict(set)

    for edge, tiles in edges.items():
        for tile1 in tiles:
            for tile2 in tiles:
                if tile1 != tile2:
                    sides[tile1].add(tile2)

    return sides

# Main Execution

def main():
    tiles   = read_tiles()
    edges   = hash_edges(tiles)
    sides   = find_sides(edges)
    corners = [tile for tile, neighbors in sides.items() if len(neighbors) == 2]
    result  = functools.reduce(operator.mul, corners)

    print(result)

if __name__ == '__main__':
    main()
