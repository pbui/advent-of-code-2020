#!/usr/bin/env python3

import collections
import sys

# Functions

def count_differences(adapters):
    return collections.Counter(
        adapters[i] - adapters[i - 1] for i in range(1, len(adapters))
    )

# Main Execution

def main():
    adapters    = [int(a) for a in sys.stdin]
    adapters    = sorted([0] + adapters + [max(adapters) + 3])
    differences = count_differences(adapters)

    print(differences[1] * differences[3])

if __name__ == '__main__':
    main()
