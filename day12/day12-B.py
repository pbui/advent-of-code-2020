#!/usr/bin/env python3

import sys

# Functions

def manhattan_distance(x, y):
    return abs(x) + abs(y)

def navigate_ship():
    sx, sy, wx, wy = 0, 0, 10, 1

    for line in sys.stdin:
        direction, magnitude = line[0], int(line[1:].strip())
        
        if direction == 'N':
            wy += magnitude
        elif direction == 'S':
            wy -= magnitude
        elif direction == 'E':
            wx += magnitude
        elif direction == 'W':
            wx -= magnitude
        elif direction == 'R':
            for _ in range(magnitude // 90):
                wx, wy =  wy, -wx   # Flip and negate new y
        elif direction == 'L':
            for _ in range(magnitude // 90):
                wx, wy = -wy, wx    # Flip and negate new x
        elif direction == 'F':
            sx += magnitude * wx
            sy += magnitude * wy

    return sx, sy

# Main Execution

def main():
    x, y     = navigate_ship()
    distance = manhattan_distance(x, y)

    print(distance)

if __name__ == '__main__':
    main()
