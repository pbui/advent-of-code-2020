#!/usr/bin/env python3

import sys

# Functions

def read_busses():
    _    = sys.stdin.readline()
    data = sys.stdin.readline().strip().split(',')
    return [(int(b), i) for i, b in enumerate(data) if b != 'x']

def find_next_timestamp(start, increment, bus_id, offset):
    while ((start + offset) % bus_id) != 0:
        start += increment
    return start

# Main Execution

def main():
    busses    = read_busses()
    timestamp = busses[0][0]
    increment = timestamp

    for bus_id, offset in busses[1:]:
        timestamp  = find_next_timestamp(timestamp, increment, bus_id, offset)
        increment *= bus_id

    print(timestamp)

if __name__ == '__main__':
    main()
