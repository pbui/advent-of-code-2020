#!/usr/bin/env python3

import collections
import sys

# Functions

def play_game(numbers, limit=30000000):
    seen = collections.defaultdict(lambda: collections.deque(maxlen=2))

    for turn, number in enumerate(numbers, 1):
        seen[number].append(turn)

    last = 0
    for turn in range(len(numbers) + 1, limit):
        seen[last].append(turn)

        if len(seen[last]) == 1:
            last = 0
        else:
            last = seen[last][1] - seen[last][0]

    return last

# Main Execution

def main():
    for line in sys.stdin:
        numbers = [int(n) for n in line.split(',')]
        result  = play_game(numbers)

        print(result)

if __name__ == '__main__':
    main()
