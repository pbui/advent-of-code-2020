#!/usr/bin/env python3

import collections
import itertools
import sys

# Constants

WINDOW_SIZE = 25

# Functions

def combinations(numbers):
    return [sum(c) for c in itertools.combinations(numbers, 2)]

# Main Execution

def main():
    numbers = collections.deque(maxlen=WINDOW_SIZE)
    for index, number in enumerate(map(int, sys.stdin)):
        if index >= WINDOW_SIZE and number not in combinations(numbers):
            print(number)
        numbers.append(number)

if __name__ == '__main__':
    main()
