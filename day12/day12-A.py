#!/usr/bin/env python3

import sys

# Constants

ORIENTATIONS = (
    ( 1,  0),   # E
    ( 0, -1),   # S
    (-1,  0),   # W
    ( 0,  1),   # N
)

# Functions

def manhattan_distance(x, y):
    return abs(x) + abs(y)

def navigate_ship():
    x, y, orientation = 0, 0, 0

    for line in sys.stdin:
        direction, magnitude = line[0], int(line[1:].strip())
        
        if direction == 'N':
            y += magnitude
        elif direction == 'S':
            y -= magnitude
        elif direction == 'E':
            x += magnitude
        elif direction == 'W':
            x -= magnitude
        elif direction == 'R':
            orientation = (orientation + magnitude // 90) % len(ORIENTATIONS)
        elif direction == 'L':
            orientation = (orientation - magnitude // 90) % len(ORIENTATIONS)
        elif direction == 'F':
            x += magnitude * ORIENTATIONS[orientation][0]
            y += magnitude * ORIENTATIONS[orientation][1]

    return x, y

# Main Execution

def main():
    x, y     = navigate_ship()
    distance = manhattan_distance(x, y)

    print(distance)

if __name__ == '__main__':
    main()
