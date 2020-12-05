#!/usr/bin/env python3

import sys

# Constants

WIDTH   = 8
MAPPING = {
    'F': '0',
    'B': '1',
    'L': '0',
    'R': '1',
}


# Functions

def parse_barcode(s):
    barcode = ''.join(MAPPING.get(c, c) for c in s)
    return int(barcode[:7], 2), int(barcode[7:], 2)

# Main Execution

def main():
    seats = []
    for line in sys.stdin:
        row, col = parse_barcode(line)
        seat_id  = row * WIDTH + col

        seats.append(seat_id)

    print(max(seats))

if __name__ == '__main__':
    main()
