#!/usr/bin/env python3

import sys

# Functions

def list_rindex(data, target):
    for index, value in enumerate(reversed(data)):
        if value == target:
            return len(data) - index
    return None

def play_game(numbers, limit=2020):
    turns = numbers[:]

    while len(turns) < limit:
        prev = list_rindex(turns[:-1], turns[-1])

        if prev is None:
            turns.append(0)
        else:
            turns.append(len(turns) - prev)

    return turns[-1]

# Main Execution

def main():
    for line in sys.stdin:
        numbers = [int(n) for n in line.split(',')]
        result  = play_game(numbers)

        print(result)

if __name__ == '__main__':
    main()
