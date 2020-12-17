#!/usr/bin/env python3

import itertools
import sys

# Constants

ACTIVE   = '#'
INACTIVE = '.'

# Classes

class SparseSpace:
    def __init__(self, layer):
        self.actives = set([
            (x, y, 0, 0)
            for y, row in enumerate(layer) for x, cube in enumerate(row)
            if cube == ACTIVE
        ])

    def count_neighbors(self, x, y, z, w):
        return sum(1 for neighbor in neighbors(x, y, z, w) if neighbor in self.actives)

    def cycle(self):
        new_actives = set()
        candidates  = list(self.actives) + flatten(
            neighbors(*cube) for cube in self.actives
        )

        for candidate in candidates:
            count = self.count_neighbors(*candidate)
            if candidate in self.actives and (count == 2 or count == 3):
                new_actives.add(candidate)
            elif candidate not in self.actives and (count == 3): 
                new_actives.add(candidate)

        self.actives = new_actives

# Functions

def read_layer(stream=sys.stdin):
    return [line.strip() for line in sys.stdin]

def flatten(iterable):
    return list(itertools.chain.from_iterable(iterable))

def neighbors(x, y, z, w):
    return (
        (x + dx, y + dy, z + dz, w + dw)
        for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4)
        if dx or dy or dz or dw
    )

# Main Execution

def main():
    layer = read_layer()
    space = SparseSpace(layer)

    for cycle in range(1, 7):
        space.cycle()

    print(len(space.actives))

if __name__ == '__main__':
    main()
