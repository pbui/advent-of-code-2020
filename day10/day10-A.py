#!/usr/bin/env python3

import collections
import sys

# Functions

def count_differences(adapters):
    counts = collections.defaultdict(int)
    for index in range(1, len(adapters)):
        counts[adapters[index] - adapters[index - 1]] += 1
    return counts

# Main Execution

def main():
    adapters = [int(a) for a in sys.stdin]
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    differences = count_differences(adapters)
    print(differences[1] * differences[3])

if __name__ == '__main__':
    main()
