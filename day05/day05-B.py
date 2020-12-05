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

def find_missing_seat(seats):
    for seat in range(min(seats), max(seats) + 1):
        if seat not in seats:
            return seat
    return None

# Main Execution

def main():
    seats = set()
    for line in sys.stdin:
        row, col = parse_barcode(line)
        seat_id  = row * WIDTH + col

        seats.add(seat_id)

    print(find_missing_seat(seats))

if __name__ == '__main__':
    main()
