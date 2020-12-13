#!/usr/bin/env python3

import math
import sys

# Constants

# Functions

def read_input():
    departure = int(sys.stdin.readline())
    busses    = [int(b) for b in sys.stdin.readline().strip().split(',') if b != 'x']

    return departure, busses

# Main Execution

def main():
    arrival, busses   = read_input()
    bus_departures    = [math.ceil(arrival / b) * b for b in busses]
    departure, bus_id = min(zip(bus_departures, busses))

    print((departure - arrival) * bus_id)

if __name__ == '__main__':
    main()
