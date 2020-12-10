#!/usr/bin/env python3

import collections
import sys

# Functions

def count_arrangements(adapters):
    counts = {0: 1}

    for adapter in adapters[1:]:
        counts[adapter] = sum(counts.get(adapter - d, 0) for d in (1, 2, 3))

    return counts

# Main Execution

def main():
    adapters     = [int(a) for a in sys.stdin]
    adapters     = sorted([0] + adapters + [max(adapters) + 3])
    arrangements = count_arrangements(adapters)

    print(arrangements[max(adapters)])

if __name__ == '__main__':
    main()
